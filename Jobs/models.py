from django.db import models

class Job(models.Model):
    Image =models.ImageField(upload_to="images/")

    Title=models.CharField(max_length=200)

    Summary=models.CharField(max_length=200)
