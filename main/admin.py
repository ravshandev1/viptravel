from django.contrib import admin
from django.utils.html import format_html
from .translations import CustomAdmin
from .models import Award, About, Advantage, Contact, Tour


@admin.register(About)
class AboutAdmin(CustomAdmin):
    list_display = ('text', 'display_image')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Contact)
class ContactAdmin(CustomAdmin):
    list_display = ('phone', 'email', 'address')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_image')

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Tour)
class TourAdmin(CustomAdmin):
    list_display = ('name', 'price', 'display_image')

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Advantage)
class AdvantageAdmin(CustomAdmin):
    list_display = ('name', 'display_image')

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)
