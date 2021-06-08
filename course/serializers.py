from rest_framework import serializers

from auth.serializers import UserProfileSerializer
from course.models import Course, CourseModules, CourseEvaluations, CourseEnrolments



class CourseModuleSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = CourseModules
        fields = ['id', 'name', 'description']


class CourseEvaluationsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = CourseEvaluations
        fields = ['id', 'name', 'description', 'type', 'evaluation_on']


class CourseEnrolmentSerializer(serializers.ModelSerializer):
    enrolment_id = serializers.CharField(read_only=True, source='id')
    name = serializers.CharField(read_only=True, source='user.name')
    email = serializers.CharField(read_only=True, source='user.email')

    class Meta:
        model = CourseEnrolments
        fields = ['enrolment_id', 'user', 'name', 'email']


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    students = serializers.SerializerMethodField()
    modules = serializers.SerializerMethodField()
    evaluations = serializers.SerializerMethodField()

    def get_students(self, obj):
        return CourseEnrolmentSerializer(obj.enrolments.filter(is_active=True), many=True).data

    def get_modules(self, obj):
        return CourseModuleSerializer(obj.modules.filter(is_active=True), many=True).data

    def get_evaluations(self, obj):
        return CourseEvaluationsSerializer(obj.evaluations.filter(is_active=True), many=True).data

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'starts_on', 'ends_on', 'students', 'modules', 'evaluations']