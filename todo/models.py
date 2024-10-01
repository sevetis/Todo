from django.db import models

# Create your models here.

class Status(models.TextChoices):
    PENDING = 'p', "Pending"
    DONE = 'd', 'Done'

class Todo(models.Model):
    name = models.CharField(
        verbose_name = "Todo Name",
        max_length = 32,
        unique = True
    )

    description = models.CharField(
        verbose_name = "Todo Description",
        max_length = 128,
        unique = False,
        blank=True,
        null=True,
    )

    status = models.CharField(
        verbose_name = "Todo Status",
        max_length = 1,
        choices = Status.choices
    )

    def __str__(self):
        return self.name
