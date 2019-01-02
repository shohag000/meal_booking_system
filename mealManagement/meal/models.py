from django.db import models
from django.contrib.auth.models import User


class User_information(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='User Name')
    full_name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Border(models.Model):
    user = models.OneToOneField(User_information,on_delete=models.CASCADE)
    phone_number = models.CharField(unique=True,max_length=11)
    email = models.EmailField()
    photo = models.FileField()

    def __str__(self):
        return self.user.full_name


class Personal_deposit(models.Model):
    deposit_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    deposit_updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    deposit_amount = models.IntegerField(default=0)

    def __str__(self):
        amount = str(self.deposit_amount)
        return amount


class Daily_meal(models.Model):
    meal_date = models.DateField(null=True)
    order_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    order_updated_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    name = models.ForeignKey(Border, on_delete=models.CASCADE)

    def breakfast_(self):
        if self.breakfast :
            return "Yes"
        else:
            return "No"

    def lunch_(self):
        if self.lunch :
            return "Yes"
        else:
            return "No"

    def dinner_(self):
        if self.dinner :
            return "Yes"
        else:
            return "No"

    def date_str(self):
        return str(self.meal_date)


class Daily_cost(models.Model):
    purchased_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    purchased_updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    purchased_by = models.ForeignKey(User_information,on_delete=models.CASCADE)
    purchased_amount = models.IntegerField(default=0)

    def __str__(self):
        amount = str(self.purchased_amount)
        return amount


class Shopping_date(models.Model):
    allotted_date = models.DateField(blank=True,null=True)
    name = models.ForeignKey(Border , on_delete=models.CASCADE)

    def __str__(self):
        date = str(self.allotted_date)
        return date




