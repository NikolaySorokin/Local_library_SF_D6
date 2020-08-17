from django.contrib import admin
from .models import Author, Publisher, Book, Friend

class MembershipInline(admin.TabularInline):
    model = Book.took_copy.through
    verbose_name = "взятые книги"
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ("took_copy",)
    list_display = ("title", "author")
