from authentication.models import User

from authentication.renderers import UserJSONRenderer

from rest_framework import serializers, status, mixins
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveUpdateAPIView, ListAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile, UserType
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer, UserTypeSerializer, ProfileSerializer1, MentorSerializer


class ProfileRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Profile.objects.select_related('user')
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def retrieve(self, request, username, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            profile = self.queryset.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username does not exist.')

        serializer = self.serializer_class(profile, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileFollowAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def post(self, request, username=None):
        follower = self.request.user.profile

        try:
            followee = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username was not found.')

        serializer = self.serializer_class(followee, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserTypeList(ListCreateAPIView):
    pagination_class = None
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class UserTypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class UserProfile(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(user_id=pk)
        except Profile.DoesNotExist:
            return False

    def put(self, request, pk, *args, **kwargs):
        profile = self.get_object(request.data.get('user', None))
        serializer = ProfileSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.data.get('user'), mentor_id=request.data.get('mentor'), updated_by_id=pk)
            return Response(serializer.data)
        else:
            serializer = ProfileSerializer1(instance=profile, data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=request.data.get('user'), mentor_id=request.data.get('mentor'))
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import mixins
from rest_framework import generics


class MentorRetrieveAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Profile.objects.filter(user_type_id__in=[1,2,3])
    serializer_class = MentorSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
