from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.
class User(AbstractUser):
    usertype = models.CharField(max_length=50,null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

class User_tbl(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    bio=models.CharField(max_length=500)
    image = models.ImageField(null=True)

class Artist_tbl(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    bio=models.CharField(max_length=500)
    image = models.ImageField(null=True)

class Gallery_tbl(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    galleryname = models.CharField(max_length=100)
    owner = models.CharField(max_length=50)
    manager=models.CharField(max_length=50)
    launch_date=models.DateField()
    gallery_type=models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    bio=models.CharField(max_length=500)
    image = models.ImageField(null=True)

class GalleryImages(models.Model):
    gallery = models.ForeignKey(Gallery_tbl,on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.CharField(max_length=500)
    date=models.DateField(null=True)
    posted=models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    user = models.ForeignKey(Artist_tbl,on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.CharField(max_length=800)
    status = models.CharField(max_length=50,default='not sold')
    posted=models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True)
    sold_to = models.ForeignKey(User_tbl,on_delete=models.CASCADE,null=True)
    sold_date = models.DateTimeField(null=True)
    start_amount = models.FloatField(null=True)


class Likes(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User_tbl,on_delete=models.CASCADE)
    posted=models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User_tbl,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    reply = models.CharField(max_length=500,null=True)
    posted=models.DateTimeField(auto_now_add=True)

class Auction(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User_tbl,on_delete=models.CASCADE)
    bid_amount = models.FloatField()
    bid_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default='not accepted')

class Vlogs(models.Model):
    user = models.ForeignKey(Artist_tbl,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    video = models.FileField()
    posted=models.DateTimeField(auto_now_add=True)

class Events(models.Model):
    user = models.ForeignKey(Gallery_tbl,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(null=True)
    posted=models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True)
    max_participants = models.IntegerField(null=True)
    participants = models.IntegerField(null=True)
    type = models.CharField(max_length=50,default='event')

class Bookslot(models.Model):
    user = models.ForeignKey(Artist_tbl,on_delete=models.CASCADE)
    event = models.ForeignKey(Events,on_delete=models.CASCADE)
    participants = models.IntegerField(null=True)
    booked_date = models.DateTimeField(auto_now_add=True)

class User_Artist_Chat(models.Model):
    user = models.ForeignKey(User_tbl,on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist_tbl,on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

class Artist_Gallery_Chat(models.Model):
    artist = models.ForeignKey(Artist_tbl,on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery_tbl,on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)