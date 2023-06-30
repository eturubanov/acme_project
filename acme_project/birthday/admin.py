from django.contrib import admin

from birthday.models import Birthday


@admin.register(Birthday)
class Birthday(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday'
    )
