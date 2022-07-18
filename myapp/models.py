from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class MaincategoryModel(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='macteimage',blank=True,null=True)

    def __str__(self):
        return self.name

class SubcategoryModel(models.Model):
    mcate=models.ForeignKey(MaincategoryModel,on_delete=CASCADE)
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='scateimage',blank=True,null=True)

    def __str__(self):
        return self.name

pstatus=(('Fresh','Fresh'),('New Arrival','New Arrival'),('Trending','Trending'),('OutofStock','OutofStock'))

class ProductModels(models.Model):
    name=models.CharField(max_length=100)
    s_cate=models.ForeignKey(SubcategoryModel,on_delete=CASCADE)
    m_cate=models.ForeignKey(MaincategoryModel,on_delete=CASCADE)
    og_price=models.FloatField(default=0)
    discount=models.FloatField(default=0)
    sell_price=models.FloatField(default=0)

    description_para=models.CharField(max_length=200,default=1)
    description_para1=models.CharField(max_length=200,default=1)
    description_para2=models.CharField(max_length=200,default=1)
    description_para3=models.CharField(max_length=200,default=1)
    description_para4=models.CharField(max_length=200,default=1)

    discounted_price=models.FloatField(default=0)

    image=models.ImageField(upload_to='ptimage',blank=True,null=False)
    image1=models.ImageField(upload_to='ptimage',blank=True,null=False)
    image2=models.ImageField(upload_to='ptimage',blank=True,null=False)
    image3=models.ImageField(upload_to='ptimage',blank=True,null=False)
    
    status=models.CharField(choices=pstatus,max_length=50,default='New Arrival')


    def __str__(self):
        return self.name

    def d_price(self):
        return round(((self.og_price)*(self.discount)/100))
    def s_price(self):
        return round(((self.og_price)-(self.discounted_price)))

    def save(self,*args,**kwargs):
        self.discounted_price=self.d_price()
        self.sell_price=self.s_price()
        super().save(*args,*kwargs)     

    @property
    def All_product(self):
        return ProductModels.objects.all().count()


class CustomerModel(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.IntegerField()
    add1=models.CharField(max_length=200)
    add2=models.CharField(max_length=200)
    ccname=models.CharField(max_length=200)
    cc_add=models.CharField(max_length=200)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=70)
    city=models.CharField(max_length=50)
    zip_code=models.IntegerField()

    def __str__(self):
        return self.first_name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    product=models.ForeignKey(ProductModels,on_delete=CASCADE)
    quantity=models.IntegerField(default=1)

    @property
    def product_total(self):
        return (self.product.sell_price)*(self.quantity)

orderstatus=(('pending','pending'),('Accepted','Accepted'),('Packing','Packing'),('Shipping','Shipping'),('Delevered','Delevered'))
class Order(models.Model):
    customer=models.ForeignKey(CustomerModel,on_delete=CASCADE)
    user=models.ForeignKey(User,on_delete=CASCADE)
    product=models.ForeignKey(ProductModels,on_delete=CASCADE)
    date=models.DateField(auto_now_add=True)
    quantity=models.PositiveBigIntegerField()
    status=models.CharField(choices=orderstatus,max_length=30,default='pending')

 
    @property
    def product_total(self):
        return (self.product.sell_price)*(self.quantity)

review_choice=((1,1),(2,2),(3,3),(4,4))

class ReviewModel(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    product=models.ForeignKey(ProductModels,on_delete=CASCADE)
    name=models.CharField(max_length=50)
    review=models.CharField(max_length=250)
    review_status=models.IntegerField(choices=review_choice,default=1)    

    @property 
    def total_review(self):
        total_review=0
        get_review=ReviewModel.objects.filter(product=self.product.id)
        count_get_review=get_review.count()
        for i in get_review:
            total_review += i.review_status
        average_review=total_review/count_get_review
        return average_review
        
        


