from django.db import models

class Posts(models.Model):
    Posts=models.CharField(max_length=1000)

    def __str__(self):
        return self.Posts  

