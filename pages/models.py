from django.db import models
from users.models import User

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # Рейтинг от 1 до 5
    comment = models.TextField()

    def __str__(self):
        return self.user.image.url