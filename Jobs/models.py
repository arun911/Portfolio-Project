from django.db import models

class Job(models.Model):
    image =models.ImageFeild(uploaded_to="images/")
    summary=models.CharField(max_length=200)
    ```````````````````````
