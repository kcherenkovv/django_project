from django.db import models

class Notes(models.Model):
    title = models.CharField('Название', max_length= 50)
    description = models.CharField('Описание', max_length = 250)
    full_text = models.TextField('Заметка')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Заметка: {self.title}'
    
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'