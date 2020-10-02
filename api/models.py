from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class MovieModel(models.Model):
    class Meta:
        db_table = 'movie'
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'

    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.title}'


class RatingModel(models.Model):
    class Meta:
        db_table = 'rating'

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE, related_name='ratings')
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return f'{self.star}'
