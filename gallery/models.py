from django.db import models

class Style(models.Model):
    name = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ( 'name', )
        verbose_name = 'style'
        verbose_name_plural = 'styles'

    def __str__(self):
        return '{}'.format(self.name)

class Painting(models.Model):
    title = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, unique=True)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='Painting')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'painting'
        verbose_name_plural = 'paintings'

    def __str__(self):
        return '{}'.format(self.title)