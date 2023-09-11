from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    """
    Это модель постов
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',verbose_name='Владелец поста ' 
    )
    title = models.CharField('Название', max_length=70)
    description = models.TextField('Описание',blank=True,null=True)
    image = models.ImageField('Изображение',upload_to='images')
    count_views = models.PositiveIntegerField('Количество просмотров',default=0)
    created_at = models.DateField('Дата создания',auto_now_add=True)
    updated_at = models.DateField('Дата обновления',auto_now=True)


    def __str__(self):
        return f'{self.title}'
    
