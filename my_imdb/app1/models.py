from django.db import models

class User(models.Model):
    username=models.SlugField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=254, null = True,blank = True)
    profile_pic=models.ImageField(upload_to='photos/%Y/%m/%d/', null = True,blank = True)

    def __str__(self):
        return self.username



class Genre(models.Model):
    genre_name=models.CharField(max_length=200,primary_key=True)   
    
    def __str__(self):
        return self.genre_name

class Comments(models.Model):
    comment=models.TextField(primary_key=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
