from django.db import models

class MyModel(models.Model):
    content = models.CharField(max_length=200)
    date_pub = models.DateTimeField("My datetime")

    def __str__(self):
        return self.content,self.date_pub