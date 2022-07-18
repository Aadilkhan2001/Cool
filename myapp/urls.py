from myapp.views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from .form import *


urlpatterns = [
    path('',HomeView),
    path('checkout/',CheckoutView),
    path('order/',OrderView),
    path('about/',AboutView),
   

    #Shop Related urls
    path('shop/',ShopView,name='shop'),
    path('filter_mcat/<int:id>',FilterMainCategoryView,name='filter_mcat'),
    path('filter_scat/<int:id>',FilterSubCategoryView,name='filter_scat'),
    path('proddetail/<int:id>/',Product_detail,name='proddata'),

    #cart Related urls
    path('cart/',CartView),
    path('add_to_cart/<int:id>/',Add_to_cart,name='add_cart'),
    path('update_cart/<int:id>',updte_cart,name='update_quantity'),
    path('remove_cart/<int:id>',remove_cart,name='remove_cart'),
    
   
    path('register/',RegisterView),
    path('login/',LoginPageView),
    path('edit/',EditPageView),
    path('changepass/',PassChangeView), 
    path('logout/',LogOutView),
    path('address/',AdressView),
    path('onlinepay/',OnlinePaymentView),



    #Password Reset
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=PassReset),name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=PassSet),name='password_reset_confirm'),
    
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),


] 