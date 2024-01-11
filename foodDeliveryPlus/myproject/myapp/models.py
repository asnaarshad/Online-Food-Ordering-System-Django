from django.db import models
# from django.contrib.auth.models import User


class FoodCategory(models.Model):
    Id = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryName


class FoodType(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class About(models.Model):
    Id = models.AutoField(primary_key=True)
    Desc = models.CharField(max_length=1000)
    Image = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.Desc


class FoodItem(models.Model):
    Id = models.AutoField(primary_key=True)
    FoodName = models.CharField(max_length=100)
    ExpiryTime = models.TimeField(auto_now=True)
    Image = models.ImageField(upload_to='static/img/')
    Price = models.IntegerField()
    Category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    Type = models.ForeignKey(FoodType, on_delete=models.CASCADE)

    def __str__(self):
        return self.FoodName


class Order(models.Model):
    Id = models.AutoField(primary_key=True)
    Status = models.CharField(max_length=100,default="Pending")
    OrderTime = models.TimeField(auto_now=True)
    # User = models.ForeignKey(User, on_delete=models.CASCADE)
    Item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    TotalBill = models.CharField(max_length=30)
    Quantity = models.IntegerField(default=1)
    Name = models.CharField(max_length=100,default="abc")
    Phone = models.CharField(max_length=150,default="12345678")
    Address = models.CharField(max_length=350,default="abc")

    def __str__(self):
        return self.Status


class Contact(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=150)
    Subject = models.CharField(max_length=250)
    Message = models.CharField(max_length=800)

    def __str__(self):
        return self.Name


