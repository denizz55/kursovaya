from django.db import models

class Clock(models.Model):

    SORT = {
            "new": "Новые",
            "popular": "Популярные",
            "Beggar": "Бюджетные",
        }

    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    price = models.IntegerField()
    name = models.CharField('Наименование часов', max_length = 200)
    category = models.CharField(choices=SORT,max_length = 200)
    description = models.TextField(default='')
    
    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'Записи'


    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    def __str__(self):
        return self.name
