from django.contrib import admin
from myapp.models import *




@admin.register(MaincategoryModel)
class MaincategoryModelAdmin(admin.ModelAdmin):
    list_display = ["image", "name"]
    list_display.reverse()

@admin.register(SubcategoryModel)
class SubcategoryModelAdmin(admin.ModelAdmin):
    list_display = [ "image", "name", "mcate"]
    list_display.reverse()




@admin.register(CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["zip_code", "city", "state", "country", "cc_add", "ccname", "add2", "add1", "mobile", "email", "last_name", "first_name", "user"]
    list_display.reverse()


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["quantity", "product", "user"]
    list_display.reverse()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["status", "quantity", "date", "product", "user", "customer"]
    list_display.reverse()




@admin.register(ProductModels)
class ProductModelsAdmin(admin.ModelAdmin):
    list_display = ["name","status", "image3", "image2", "image1", "image", "discounted_price", "description_para4", "description_para3", "description_para2", "description_para1", "description_para", "sell_price", "discount", "og_price", "m_cate", "s_cate"]

@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ["review_status", "review", "name", "product", "user"][::-1]
