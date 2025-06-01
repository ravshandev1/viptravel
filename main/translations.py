from modeltranslation.translator import register, TranslationOptions
from modeltranslation.admin import TranslationAdmin
from .models import Contact, About, Tour, Advantage


class CustomAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@register(About)
class ItemTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Contact)
class ItemTranslationOptions(TranslationOptions):
    fields = ('address',)


@register(Tour)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'price')


@register(Advantage)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'text')
