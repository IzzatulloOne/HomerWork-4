from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)  # Поле для изображения

    def __str__(self):
        return self.title