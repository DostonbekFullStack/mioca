from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

# HOME 1

class User(AbstractUser):
    type =  models.IntegerField(choices=(
        (1, 'admin'),
        (2, 'seller'),
        (3, 'client')
    ), default=3)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Logo(models.Model):
    image = models.ImageField(upload_to='media/')

class Info(models.Model):
    address = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()

class Slider(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=255)
    oldprice = models.DecimalField(max_digits=6, decimal_places=2)
    newprice = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class Categorie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Production(models.Model):
    quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/products/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)


class Product(models.Model):
    production = models.ForeignKey(Production, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(default=1,
        validators=[MinValueValidator(1),
        MaxValueValidator(5)
    ])
    discount = models.IntegerField(default=0,
        validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class Card(models.Model):
    purchased = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True,null=True)
    quantity = models.IntegerField(default=0)


class Purchase(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    summa = models.IntegerField(default=0)


class Facilities(models.Model):
    image = models.ImageField(upload_to='media/facilities/')
    title = models.CharField(max_length=255)
    para = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Forsale(models.Model):
    image = models.ImageField(upload_to='media/forsale/')
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    oldprice = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class Latestblog(models.Model):
    author = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

# About
class TeamMembers(models.Model):
    image = models.ImageField(upload_to='media/team_members/')
    fullname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
    
class Client(models.Model):
    image = models.ImageField(upload_to='media/client/')
    fullname = models.CharField(max_length=255)
    paragraph = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname

class Sponsor(models.Model):
    image = models.ImageField(upload_to='media/sponsor/')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#Contact

class LeaveMsg(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2500)

class Map(models.Model):
    link = models.CharField(max_length=500)


# Casa

class Casa(models.Model):
    casa = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)