from django.db import models


# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната TicTacToe'
        verbose_name_plural = 'Комнаты TicTacToe'
