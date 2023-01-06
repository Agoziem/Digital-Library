from django.db import models

Level = (
			('100', '100'),
			('200', '200'),
			('300', '300'),
            ('400', '400'),
            ('500', '500'),

			)


class department(models.Model):
    Name =models.CharField(max_length=100, blank = False, null=True)
    thumbnail = models.ImageField(upload_to='assets', blank=True)
    
    def __str__(self):
        return str(self.Name)

    @property  
    def imageURL(self):
        try:
            url= self.thumbnail.url
        except:
            url=''
        return url

class Textbook(models.Model):
    Title= models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='assets', blank=False)
    level =models.CharField(max_length=200, null=True, choices=Level , blank=False)
    Department =models.ForeignKey(department, on_delete= models.SET_NULL,blank=True, null=True,)
    File=models.FileField(upload_to='media' ,blank = False)
    
    def __str__(self):
        return str(self.Title)

    @property
    def TextbookimageURL(self):
        try:
            url= self.thumbnail.url
        except:
            url=''
        return url

class PastQuestion(models.Model):
    course= models.CharField(max_length=100, blank = False, null=True)
    File=models.FileField(upload_to = 'media' ,blank = False)
    year=models.CharField(max_length=100, blank = False, null=True)
    level =models.CharField(max_length=200, null=True, choices=Level , blank=False)
    Department =models.ForeignKey(department, on_delete= models.SET_NULL,blank = False, null=True,)
    
    def __str__(self):
        return str(self.course)
        
class Material(models.Model):
    Title= models.CharField(max_length=100, blank = False, null=True)
    course= models.CharField(max_length=100, blank = False, null=True)
    File=models.FileField(upload_to = 'media' ,blank = False)
    level =models.CharField(max_length=200, null=True, choices=Level , blank=False)
    Department =models.ForeignKey(department, on_delete= models.SET_NULL,blank = False, null=True,)
   
    def __str__(self):
        return str(self.Title)



