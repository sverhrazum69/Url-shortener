from django.db import models

class StoreURL(models.Model):
    url = models.CharField(max_length = 300)
    def __str__(self):
        return self.url