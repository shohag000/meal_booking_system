from django.shortcuts import render,redirect,get_object_or_404
from .models import Border,Daily_meal,User_information,Shopping_date
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


def get_login(request):
     if request.user.is_authenticated:
          return redirect("meal_sheet")
     else:
          if request.method == "POST":
               username = request.POST.get("username")
               password = request.POST.get("password")
               if username and password:
                    auth = authenticate(request,username=username, password=password)
                    if auth is not None:
                         login(request, auth)
                         return redirect("meal_sheet")
                    else:
                         return render(request, "login.html")

     return render(request, "login.html")


def get_logout(request):
    logout(request)
    return redirect("login")


@login_required
def chart(request):
     borders = Border.objects.all()
     today = datetime.date.today()
     number = -7
     my_list = []

     '''
     If we need to access daily_meal property of a specific  border
     then 
     my_2nd_list = []
     for border in borders:
          my_2nd_list.append(border.daily_meal_set.all())
     If we need to eliminate duplicate property of daily_meal object 
     then 
     meal_dates = Daily_meal.objects.order_by('meal_date').distinct('meal_date')
     
     '''

     for x in range(10):

          one_day = datetime.timedelta(days=number)
          before_date = today + one_day
          my_list.append(before_date)
          number += 1

     in_range_meal = Daily_meal.objects.filter(meal_date__range=[str(my_list[0]), str(my_list[9])])
     my_list_new = list(my_list)
     if request.user.is_authenticated:
          user_id = request.user.id
          user_full_name = User_information.objects.get(id=user_id)
          print(user_full_name.full_name)
          for user_daily_meal in in_range_meal:
               if user_daily_meal.name.user.full_name == user_full_name.full_name and user_daily_meal.meal_date in my_list:
                    my_list_new.remove(user_daily_meal.meal_date)
                    #print(user_daily_meal.meal_date)
          orderable_date_list = list(my_list_new)
          for var in my_list_new:
               if var <= today:
                    orderable_date_list.remove(var)
                    #print(var)


     context = {
          'borders' : borders,
          'daily_meals' : in_range_meal,
          'today' : today,
          'my_list' : my_list,
          'orderable_date_list': orderable_date_list,
          'user_full_name': user_full_name.full_name,
     }

     print("New line")
     print(orderable_date_list)
     print("New line")
     print(my_list)

     return render(request,"meal_sheet.html",context)


def order(request,date):
     if request.user.is_authenticated:
          user_id = request.user.id
          user_information = User_information.objects.get(pk=user_id)
          border = Border.objects.get(pk=user_information.id)
     if request.method == "POST":
          breakfast = request.POST.get("breakfast")
          lunch = request.POST.get("lunch")
          dinner = request.POST.get("dinner")
          if breakfast== "on":
               breakfast= True
          else:
               breakfast= False
          if lunch== "on":
               lunch= True
          else:
               lunch= False
          if dinner== "on":
               dinner= True
          else:
               dinner= False
          daily_meal_object = Daily_meal.objects.create(meal_date=date,breakfast=breakfast,lunch=lunch,dinner=dinner,name=border)
          daily_meal_object.save()
          #print(daily_meal_object)
     context = {
          'date': date,
     }
     return render(request,"order.html",context)


@login_required
def shopping_date(request):
     today = datetime.date.today()
     user_id = request.user.id
     user_information = User_information.objects.get(pk=user_id)
     border = Border.objects.get(pk=user_information.id)
     shopping_dates = Shopping_date.objects.filter(name=border,allotted_date__month=today.month)
     context={
          'today':today,
          'shopping_dates':shopping_dates,
     }
     return render(request,"shopping_date.html",context)