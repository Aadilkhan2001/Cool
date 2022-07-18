from .models import *
def data(request):
    all_category = MaincategoryModel.objects.all()
    all_subcategory = SubcategoryModel.objects.all()
    sub_total = 0
    shipping_charge = 70
    GST = 10
    grand_total = 0
    GST_price = 0
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = Cart.objects.filter(user=request.user).count()
        if cart_items:
            for i in cart_items:
                GST_price += ((i.product_total*GST)/100)
                sub_total += (i.product_total)

            grand_total += ((sub_total+shipping_charge+GST_price))



        return {'cart_items': cart_items,
                        'sub': sub_total,
                        'grand': grand_total,
                        'ship': shipping_charge,
                        'gst': GST_price,
                        'cart_count': cart_count,
                        'all_mcat': all_category,
                        'all_scat': all_subcategory, 
                        }

    else:
        return{'sub': sub_total,
                'grand': grand_total,
                'ship': shipping_charge,
                'gst': GST_price,        
                'all_mcat': all_category,
                'all_scat': all_subcategory, }
