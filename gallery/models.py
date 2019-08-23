from django.db import models
from django.urls import reverse

class Style(models.Model):
    name = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'style'
        verbose_name_plural = 'styles'
    
    def get_url(self):
        return reverse('gallery:paintings_by_style', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Painting(models.Model):
    title = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, unique=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
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
    
    def get_url(self):
        return reverse('gallery:paintStyDetail', args=[self.style.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.title)