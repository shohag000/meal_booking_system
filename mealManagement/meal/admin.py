from django.contrib import admin
from .models import User_information,Personal_deposit,Daily_meal,Daily_cost,Shopping_date,Border


class Shopping_date_admin(admin.ModelAdmin):
    list_display = ('allotted_date',)

    class Meta:
        Model = Shopping_date


class Personal_deposit_admin(admin.ModelAdmin):
    list_display = ('deposit_amount','deposit_date','deposit_updated_on',)

    class Meta:
        Model = Personal_deposit


class Daily_meal_admin(admin.ModelAdmin):
    list_display = ('meal_date','name','breakfast_','lunch_','dinner_',)

    class Meta:
        Mpdel = Daily_meal


admin.site.register(Personal_deposit,Personal_deposit_admin)
admin.site.register(Daily_meal,Daily_meal_admin)
admin.site.register(Daily_cost)
admin.site.register(Shopping_date,Shopping_date_admin)
admin.site.register(Border)
admin.site.register(User_information)