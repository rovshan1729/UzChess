from rest_framework import serializers
from django.contrib.auth.models import User
from course.models import (
    Author,
    Category,
    Level,
    Language,
    Course,
    CourseUser,
    Unit,
    Lesson,
    LessonUser,
    FeedBack,
    Report,
)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("title",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title",)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ("title",)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("title",)


class LessonUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = LessonUser
        fields = ("lesson", "user", "watching_at", "is_complete")


class LessonSerializer(serializers.ModelSerializer):
    lesson_users = LessonUserSerializer(many=True)

    class Meta:
        model = Lesson
        fields = (
            "title",
            "content",
            "banner",
            "video",
            "video_duration",
            "unit",
            "lesson_users",
            "created_at",
            "updated_at",
        )


class UnitSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Unit
        fields = ("title", "course", "lessons")


class FeedBackSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = FeedBack
        fields = ("user", "course", "stars", "content", "created_at", "updated_at")


class CourseUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = CourseUser
        fields = (
            "course",
            "user",
            "is_complete",
            "is_favorite",
            "created_at",
            "updated_at",
        )


class CourseSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    language = LanguageSerializer()
    level = LevelSerializer()
    category = CategorySerializer()
    units = UnitSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            "title",
            "price",
            "author",
            "language",
            "level",
            "category",
            "rating",
            "units",
            "created_at",
            "updated_at",
        )


class CourseSingleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    language = LanguageSerializer()
    level = LevelSerializer()
    category = CategorySerializer()
    units = UnitSerializer(many=True)
    feedbacks = FeedBackSerializer(many=True)
    course_users = CourseUserSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            "title",
            "price",
            "author",
            "language",
            "level",
            "category",
            "rating",
            "feedbacks",
            "units",
            "course_users",
            "created_at",
            "updated_at",
        )


class ReportSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)
    feedback = FeedBackSerializer()

    class Meta:
        model = Report
        fields = ("subject", "content", "user", "feedback")
