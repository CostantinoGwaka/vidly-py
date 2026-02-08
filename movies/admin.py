from django.contrib import admin
from .models import Genre, Movies

# Register your models here.

# customize table in django admin


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    # fields = ('title',)
    exclude = ('date_created',)
    list_display = ('id', 'title', 'number_in_stock', 'daily_rate')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MovieAdmin)
