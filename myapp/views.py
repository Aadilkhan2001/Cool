from itertools import product
from unicodedata import name
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages
from myapp.form import ChangePassForm, CustomerAddressForm, LogInForm, UserCForm, UserProfileChangeForm
from django.shortcuts import redirect, render
from .models import Cart, MaincategoryModel, ProductModels, SubcategoryModel
from django.core.paginator import Paginator
from myapp.context_processor import data
import razorpay


# Rendering Home Page
def HomeView(request):
    all_product = ProductModels.objects.all()
    context = {'all_prod': all_product}
    return render(request, 'index.html', context)

# product detail page rendering


def Product_detail(request, id):
    get_product = ProductModels.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST['name']
        review=request.POST['text']
        rates=request.POST['rating']
        ReviewModel(
            user=request.user,
            product=get_product,
            name=name,
            review=review,
            review_status=rates
        ).save()
    # total_review=0
    # get_review=ReviewModel.objects.filter(product=id)
    # count_review=get_review.count()
    # for i in get_review:
    #     total_review+=i.review_status
    # average_review=round(total_review/count_review)
    context = {'get_product': get_product}
    return render(request, 'product_detail_page.html', context)


# shop page rendering
def ShopView(request):
    all_product = ProductModels.objects.all()
    if request.method == 'GET':
        get_sort= request.GET.get('sort')
        if get_sort == 'name_asc':
            all_product = all_product.order_by('name')
        elif get_sort== 'name_dsc':
            all_product = all_product.order_by('name').reverse()
        elif get_sort == 'price_asc':
            all_product = all_product.order_by('sell_price')
        elif get_sort == 'price_dsc':
            all_product = all_product.order_by('sell_price').reverse()
    count=all_product.count()
    paginator = Paginator(all_product, 8)
    page_number = request.GET.get('page')
    all_product = paginator.get_page(page_number)
    context = {
        'all_prod': all_product,
        'page_number': page_number,
        'pro_count': count
    }
    return render(request, 'shop.html', context)

# filtering product by maincategory


def FilterMainCategoryView(request, id):
    all_product = ProductModels.objects.filter(m_cate=id)
    if request.method == 'GET':
        get_sort=request.GET.get('sort')
        if get_sort == 'name_asc':
            all_product = all_product.order_by('name')
        elif get_sort== 'name_dsc':
            all_product = all_product.order_by('name').reverse()
        elif get_sort == 'price_asc':
            all_product = all_product.order_by('sell_price')
        elif get_sort == 'price_dsc':
            all_product = all_product.order_by('sell_price').reverse()
    count=all_product.count()
    paginator = Paginator(all_product, 8, orphans=0)
    page_number = request.GET.get('page')
    all_product = paginator.get_page(page_number)
    context = {
        'all_prod': all_product,
        'page_number': page_number,
        'pro_count': count
    }
    return render(request, 'shop.html', context)

# filtering product by sub category
def FilterSubCategoryView(request, id):
    all_product = ProductModels.objects.filter(s_cate=id)
    if request.method == 'GET':
        get_sort=request.GET.get('sort')
        if get_sort == 'name_asc':
            all_product = all_product.order_by('name')
        elif get_sort== 'name_dsc':
            all_product = all_product.order_by('name').reverse()
        elif get_sort == 'price_asc':
            all_product = all_product.order_by('sell_price')
        elif get_sort == 'price_dsc':
            all_product = all_product.order_by('sell_price').reverse()
    count=all_product.count()        
    paginator = Paginator(all_product, 8, orphans=0)
    page_number = request.GET.get('page')
    all_product = paginator.get_page(page_number)
    context = {
        'all_prod': all_product,
        'page_number': page_number,
        'pro_count': count
    }
    return render(request, 'shop.html', context)

# Rendering Cart Pagea


def CartView(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_count = Cart.objects.filter(user=request.user).count()
    all_category = MaincategoryModel.objects.all()
    all_subcategory = SubcategoryModel.objects.all()

    sub_total = 0
    shipping_charge = 70
    GST = 10
    grand_total = 0
    GST_price = 0

    if cart_items:
        for i in cart_items:
            GST_price += ((i.product_total*GST)/100)
            sub_total += (i.product_total)

        grand_total += ((sub_total+shipping_charge+GST_price))

        context = {'cart_items': cart_items,
                   'sub': sub_total,
                   'grand': grand_total,
                   'ship': shipping_charge,
                   'gst': GST_price,
                   'cart_count': cart_count,
                   'all_mcat': all_category,
                   'all_scat': all_subcategory, }

        return render(request, 'cart.html', context)
    else:
        context = {'cart_count': 0,
                   'all_mcat': all_category,
                   'all_scat': all_subcategory, }
        return render(request, 'cart.html', context)

# Add To Cart Page


def Add_to_cart(request, id):
    if request.user.is_authenticated:
        get_product = ProductModels.objects.get(id=id)
        Cart(
            user=request.user,
            product=get_product,
        ).save()
        return redirect('/cart/')

    else:
        return redirect('/login/')


def updte_cart(request, id):
    update_quan = request.GET.get('quantity')
    get_product = Cart.objects.filter(user=request.user, id=id)
    if update_quan:
        for i in get_product:
            i.quantity = update_quan
            i.save()
    return redirect('/cart/')


def remove_cart(request, id):
    if id:
        get_cart = Cart.objects.filter(user=request.user, id=id)
        get_cart.delete()
    return redirect('/cart/')


def CheckoutView(request):
    address = CustomerModel.objects.filter(user=request.user)
    form = CustomerAddressForm()
    if request.method == 'POST':
        cust_id = request.POST['customer']
        cart_items = Cart.objects.filter(user=request.user)
        customer_data = CustomerModel.objects.get(id=cust_id)
        for i in cart_items:
            item = i.product
            qua = i.quantity
            Order(user=request.user, product=item,
                  quantity=qua, customer=customer_data).save()
        cart_items.delete()
    context = {'address': address, 'form1': form}
    return render(request, 'checkout.html', context)


def OnlinePaymentView(request):
    form=CustomerModel.objects.filter(user=request.user)
    if request.method == 'POST':
        cust_id = request.POST['customer']
        cart_items = Cart.objects.filter(user=request.user)
        customer_data = CustomerModel.objects.get(id=cust_id)
        sub_total = 0
        shipping_charge = 70
        GST = 10
        grand_total = 0
        GST_price = 0

        for i in cart_items:
            GST_price += ((i.product_total*GST)/100)
            sub_total += (i.product_total)

        grand_total += ((sub_total+shipping_charge+GST_price))

        for i in cart_items:
            item = i.product
            qua = i.quantity
            Order(user=request.user, product=item,
                      quantity=qua, customer=customer_data).save()
        client = razorpay.Client(auth=("rzp_test_0gGp3unTKlboNp", "RkJWX03vTlvcfsRF9R56ahj4"))
        payment = client.order.create({'amount':(grand_total)*100, 'currency': 'INR','payment_capture': '1'})
        cart_items.delete()
    else:
        cart_items = Cart.objects.filter(user=request.user)
        sub_total = 0
        shipping_charge = 70
        GST = 10
        grand_total = 0
        GST_price = 0
        for i in cart_items:
            GST_price += ((i.product_total*GST)/100)
            sub_total += (i.product_total)

        grand_total += ((sub_total+shipping_charge+GST_price))
        client = razorpay.Client(auth=("rzp_test_0gGp3unTKlboNp", "RkJWX03vTlvcfsRF9R56ahj4"))
        payment = client.order.create({'amount':(grand_total)*100, 'currency': 'INR','payment_capture': '1'})
    context = {'form1': form,'payment':payment}
    return render(request,'onlinepay.html',context)

def OrderView(request):
    order=Order.objects.filter(user=request.user).reverse()
    context={'order':order}
    return render(request,'order.html',context)

# Login Logic


def LoginPageView(request):
    form = LogInForm()
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname, password=upass)
        if user is None:
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'login.html', {'form1': form})


# Edit Profile Logic
def EditPageView(request):
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/edit/')
    else:
        form = UserProfileChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'edit.html', context)

# Register Logic


def RegisterView(request):
    if request.method == 'POST':
        form = UserCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCForm()
    return render(request, 'signup.html', {'form': form})


# Logout Logic
def LogOutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/login/')


# Password Change Through Old Password


def PassChangeView(request):
    if request.method == 'POST':
        form = ChangePassForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ChangePassForm(user=request.user)
    context = {'form': form}
    return render(request, 'changepassword.html', context)


def AdressView(request):
    if request.method == 'POST':
        form = CustomerAddressForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            ccname = form.cleaned_data['ccname']
            ccadd = form.cleaned_data['cc_add']
            country = form.cleaned_data['country']
            add1 = form.cleaned_data['add1']
            add2 = form.cleaned_data['add2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zip_code']
            add_data = CustomerModel(
                user=request.user,
                first_name=fname,
                last_name=lname,
                email=email,
                mobile=mobile,
                ccname=ccname,
                cc_add=ccadd,
                country=country,
                add1=add1,
                add2=add2,
                city=city,
                state=state,
                zip_code=zipcode,
            )
            add_data.save()
            messages.info(request, 'YOUR ADDRESS SUCCESSFULLY ADDED !!!')
            return redirect('/checkout/')
    else:
        form = CustomerAddressForm()
    context = {'form1': form}
    return render(request, 'address.html', context)

#Rendering About Page
def AboutView(request):
    return render(request,'about.html')
