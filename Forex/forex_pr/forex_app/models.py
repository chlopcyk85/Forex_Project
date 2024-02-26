from django.db import models


class ForexResult(models.Model):
    currency_pair = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.currency_pair} - {self.description}"
