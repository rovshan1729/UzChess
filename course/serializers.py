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
        fields = (
            "id",
            "title",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
        )


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = (
            "id",
            "title",
        )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            "id",
            "title",
        )


class LessonUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = LessonUser
        fields = ("id", "lesson", "user", "watching_at", "is_complete")


class LessonSerializer(serializers.ModelSerializer):
    lesson_users = LessonUserSerializer(many=True)

    class Meta:
        model = Lesson
        fields = (
            "id",
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


class LessonRetriveSerializer(serializers.ModelSerializer):
    lesson_users = LessonUserSerializer(many=True)
    # prev = LessonSerializer()
    # next = LessonSerializer()

    class Meta:
        model = Lesson
        fields = (
            "id",
            "title",
            "content",
            "banner",
            "video",
            "video_duration",
            "unit",
            # "prev",
            # "next",
            "lesson_users",
            "created_at",
            "updated_at",
        )

    # def to_representation(self, instance):
    #     lessons = list(
    #         Lesson.objects.all().filter(unit=instance.unit).order_by("-created_at")
    #     )

    #     json = super().to_representation(instance)
    #     prev = ""
    #     next = ""

    #     if lessons.index(instance) != 0:
    #         prev = lessons[lessons.index(instance) - 1]

    #     if lessons.index(instance) != len(lessons) - 1:
    #         next = lessons[lessons.index(instance) + 1]

    #     json.prev = prev
    #     json.next = next

    #     return json


class UnitSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Unit
        fields = ("id", "title", "course", "lessons")


class FeedBackSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = FeedBack
        fields = (
            "id",
            "user",
            "course",
            "stars",
            "content",
            "created_at",
            "updated_at",
        )


class CourseUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = CourseUser
        fields = (
            "id",
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
            "id",
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
            "id",
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
        fields = ("id", "subject", "content", "user", "feedback")
