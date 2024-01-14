from .models import Post, Comment
from modeltranslation.translator import register, TranslationOptions # импортируем декоратор для перевода 
#и класс настроек, от которого будем наследоваться
 
# регистрируем наши модели для перевода
@register(Post)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text', ) # указываем, какие именно поля надо переводить в виде кортежа
 
@register(Comment)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('text', )