from django.db import models

# Create your models here.
# model -> table

# Syntax class <tableName(models.Model)> -> creating a table(sql) collection(nosql)

class ContactTable(models.Model):
    email = models.EmailField(max_length=150, null=False)   # column 1
    description = models.TextField()  

    def __str__(self) -> str:
        return self.email   

class TestModel(models.Model):
    name= models.TextField()
    img = models.ImageField(upload_to="images")


# select * from contact:
    # -> ContactTable.objects.all()        

class Places(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="pictures")

    def __str__(self) -> str:
        return self.title

class PlacesDetail(models.Model):
    country = models.ForeignKey(Places, on_delete=models.CASCADE)
    img3d = models.FileField(upload_to="panpictures")
    img3dname = models.CharField(max_length=200, default=None)
    desc = models.TextField()
    cust_trad = models.TextField(default=None)   
    lang_name = models.CharField(max_length=200, default=None)       
    lang_culture = models.TextField(default=None)
    famous_spots = models.TextField(default=None)
    tips_recom = models.TextField(default=None)
    img1 = models.FileField(upload_to="pictures", default=None)
    img2 = models.FileField(upload_to="pictures", default=None)

    def __str__(self) -> str:
        return self.img3dname
    
