from django.contrib import admin
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


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

    class Meta:
        abstract = True


@admin.register(Author)
class AuthorAdmin(BaseAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    pass


@admin.register(Level)
class LevelAdmin(BaseAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(BaseAdmin):
    pass


@admin.register(Course)
class CourseAdmin(BaseAdmin):
    readonly_fields = ("rating", "created_at", "updated_at")


@admin.register(CourseUser)
class CourseUserAdmin(BaseAdmin):
    pass


@admin.register(Unit)
class UnitAdmin(BaseAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(BaseAdmin):
    pass


@admin.register(LessonUser)
class LessonUserAdmin(BaseAdmin):
    pass


@admin.register(FeedBack)
class FeedBackAdmin(BaseAdmin):
    pass


@admin.register(Report)
class ReportAdmin(BaseAdmin):
    pass
