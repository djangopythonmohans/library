from django.db import models

# Create your models here.


class Library(models.Model):
    """
    
    subid 
    sub name
    senmister name
    
    yearname
    branchname
    regno
    
    

    """

    subjectid=models.IntegerField(primary_key=True)
    subname= models.CharField(max_length=60)
    senmister=models.CharField(max_length=60)
    year=models.CharField(max_length=60)
    branch=models.CharField(max_length=60)
    reg=models.CharField(max_length=60)
    docfile= models.FileField(upload_to='documents/')


    def __str__(self):
        return self.subname