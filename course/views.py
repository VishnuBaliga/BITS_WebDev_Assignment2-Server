from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auth.serializers import UserProfileSerializer
from course.models import Course, CourseModules, CourseEvaluations, CourseEnrolments
from course.serializers import CourseSerializer, CourseModuleSerializer, CourseEvaluationsSerializer, \
    CourseEnrolmentSerializer

# Create your views here.


class ListAndCreateCourse(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(is_active=True)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(is_active=True)


class ListAndCreateCourseModule(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CourseModuleSerializer
    queryset = CourseModules.objects.filter(is_active=True)

    def filter_queryset(self, queryset):
        return queryset.filter(course_id=self.kwargs.get('course_id'))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return CourseModules.objects.create(course_id=self.kwargs.get('course_id'), **serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveUpdateDestroyCourseModule(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CourseModuleSerializer
    queryset = CourseModules.objects.filter(is_active=True)

    def filter_queryset(self, queryset):
        return queryset.filter(course_id=self.kwargs.get('course_id'))


class ListAndCreateCourseEvaluations(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CourseEvaluationsSerializer
    queryset = CourseEvaluations.objects.filter(is_active=True)

    def filter_queryset(self, queryset):
        return queryset.filter(course_id=self.kwargs.get('course_id'))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return CourseEvaluations.objects.create(course_id=self.kwargs.get('course_id'), **serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveUpdateDestroyCourseEvaluations(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CourseEvaluationsSerializer
    queryset = CourseEvaluations.objects.filter(is_active=True)

    def filter_queryset(self, queryset):
        return queryset.filter(course_id=self.kwargs.get('course_id'))


class ListAndCreateCourseStudents(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CourseEnrolmentSerializer
    queryset = CourseEnrolments.objects.filter(is_active=True)

    def filter_queryset(self, queryset):
        return queryset.filter(course_id=self.kwargs.get('course_id'))

    def create(self, request, *args, **kwargs):
        enrolment_ob, _ = self.perform_create(request.data)
        return Response(self.get_serializer(instance=enrolment_ob).data, status=status.HTTP_201_CREATED)

    def perform_create(self, data):
        return CourseEnrolments.objects.get_or_create(
            course_id=self.kwargs.get('course_id'), **{'user_id': data.get('user')})

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        user_list = [x.user for x in queryset]
        serializer = UserProfileSerializer(user_list, many=True)
        return Response(serializer.data)


class RetrieveUpdateDestroyCourseStudents(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CourseEnrolmentSerializer
    queryset = CourseEnrolments.objects.filter(is_active=True)

    def filter_queryset(self, queryset):
        return queryset.filter(course_id=self.kwargs.get('course_id'))
