from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Сохранить')
    class Meta:
        model = Post
        fields = ['author', 'title', 'category', 'text', 'post_type', 'check_box']
