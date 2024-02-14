from rest_framework.generics import ListAPIView, RetrieveAPIView
from course import serializers
from course import models


class CourseListAPIView(ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseRetriveAPIView(RetrieveAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSingleSerializer
