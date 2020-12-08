from django.db import models
import datetime

# Create a Blog models
class Blog(models.Model):
    #title
    Title=models.CharField(max_length=255)
    #Publication_date
    Publication_date=models.DateTimeField()
    #Blog_Body
    Body=models.TextField()
    #Blog_Images
    Image=models.ImageField(upload_to='images/')

    def __str__(self):
        x=self.Title
        y=str(self.Publication_date.strftime('%c'))
        return x+"  -  "+y

    def Publication_date_pretty(self):
        return self.Publication_date.strftime('%c')





#Add the Blog app to the settings

#Create the Migrations

#migrate

#Add to the admin
