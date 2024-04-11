from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


# Create your models here.
class Pet(models.Model):
    """The pet model."""

    name = models.CharField(
        max_length=45,
        validators=[MinLengthValidator(2, "Name must be at least two characters.")],
    )
    type = models.CharField(
        max_length=45,
        validators=[MinLengthValidator(2, "Type must be at least two characters.")],
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0, "Age must be at least zero.")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
