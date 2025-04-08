from django.shortcuts import render,redirect, get_object_or_404
from .forms import SignupForm, CustomerForm, SubscriptionForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Order, DeeceCategory, DeeceCategory2, Product, Product2, CartItem, Cart, CustomerDetails, Subscription
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.http import HttpResponse
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .models import Payment
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def u_signup(request):
    if request.method == 'POST':
        lg = SignupForm(request.POST)
        if lg.is_valid():
            lg.save()
            return redirect('login')
    else:
        lg = SignupForm()
    return render(request, 'core/signup.html', {'lg':lg})


def u_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf=AuthenticationForm(request,data=request.POST)
            if mf.is_valid():
                u_username = mf.cleaned_data['username']
                u_password = mf.cleaned_data['password']
                user = authenticate(username=u_username,password=u_password)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            mf=AuthenticationForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request,'core/profile.html')
    else:
        return redirect('login')
    
def u_logout(request):
    logout(request)
    return redirect('login')
  

def men_category(request):
    men = DeeceCategory2.objects.filter(category='MEN')
    colors = DeeceCategory2.objects.values_list('color', flat=True).distinct()
    sizes = DeeceCategory2.objects.values_list('size', flat=True).distinct()

    # Get selected filter values
    selected_color = request.GET.get('color')
    selected_size = request.GET.get('size')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Apply filters
    if selected_color:
        men = men.filter(color=selected_color)
    if selected_size:
        men = men.filter(size=selected_size)
    if min_price:
        men = men.filter(price__gte=min_price)
    if max_price:
        men = men.filter(price__lte=max_price)
    return render(request, 'core/men_category.html', {'men': men,
        'color': colors,
        'size': sizes,
        'selected_color': selected_color,
        'selected_size': selected_size,
        'min_price': min_price,
        'max_price': max_price,
        })


def women_category(request):
    women = DeeceCategory2.objects.filter(category='WOMEN')
    colors = DeeceCategory2.objects.values_list('color', flat=True).distinct()
    sizes = DeeceCategory2.objects.values_list('size', flat=True).distinct()

    # Get selected filter values
    selected_color = request.GET.get('color')
    selected_size = request.GET.get('size')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Apply filters
    if selected_color:
        women = women.filter(color=selected_color)
    if selected_size:
        women = women.filter(size=selected_size)
    if min_price:
        women = women.filter(price__gte=min_price)
    if max_price:
        women = women.filter(price__lte=max_price)
    return render(request, 'core/women_category.html', {'women':women,
        'color': colors,
        'size': sizes,
        'selected_color': selected_color,
        'selected_size': selected_size,
        'min_price': min_price,
        'max_price': max_price,
        })


def kids_category(request):
    kids = DeeceCategory2.objects.filter(category='KIDS')
    colors = DeeceCategory2.objects.values_list('color', flat=True).distinct()
    sizes = DeeceCategory2.objects.values_list('size', flat=True).distinct()

    # Get selected filter values
    selected_color = request.GET.get('color')
    selected_size = request.GET.get('size')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Apply filters
    if selected_color:
        kids = kids.filter(color=selected_color)
    if selected_size:
        kids = kids.filter(size=selected_size)
    if min_price:
        kids = kids.filter(price__gte=min_price)
    if max_price:
        kids = kids.filter(price__lte=max_price)
    return render(request, 'core/kids_category.html', {'kids':kids,
        'color': colors,
        'size': sizes,
        'selected_color': selected_color,
        'selected_size': selected_size,
        'min_price': min_price,
        'max_price': max_price,
        })


def hoodjack_category(request):
    hood = DeeceCategory2.objects.filter(category='HOODJACK')
    colors = DeeceCategory2.objects.values_list('color', flat=True).distinct()
    sizes = DeeceCategory2.objects.values_list('size', flat=True).distinct()

    # Get selected filter values
    selected_color = request.GET.get('color')
    selected_size = request.GET.get('size')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Apply filters
    if selected_color:
        hood = hood.filter(colors=selected_color)
    if selected_size:
        hood = hood.filter(sizes=selected_size)
    if min_price:
        hood = hood.filter(price__gte=min_price)
    if max_price:
        hood = hood.filter(price__lte=max_price)
    return render(request, 'core/hoodjack_category.html', {'hood':hood,  'color': colors,
        'size': sizes,
        'selected_color': selected_color,
        'selected_size': selected_size,
        'min_price': min_price,
        'max_price': max_price,})


def footwear_category(request):
    access = DeeceCategory2.objects.filter(category='FOOTWEAR')
    colors = DeeceCategory2.objects.values_list('color', flat=True).distinct()
    sizes = DeeceCategory2.objects.values_list('size', flat=True).distinct()

    # Get selected filter values
    selected_color = request.GET.get('color')
    selected_size = request.GET.get('size')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Apply filters
    if selected_color:
        access = access.filter(color=selected_color)
    if selected_size:
        access = access.filter(size=selected_size)
    if min_price:
        access = access.filter(price__gte=min_price)
    if max_price:
        access = access.filter(price__lte=max_price)
    return render(request, 'core/footwear_category.html', {'access':access,
        'color': colors,
        'size': sizes,
        'selected_color': selected_color,
        'selected_size': selected_size,
        'min_price': min_price,
        'max_price': max_price,})


def clothe_details(request, id):
    cd = DeeceCategory.objects.get(pk=id)
    return render(request, 'core/clothe_details.html', {'cd':cd})


def product_list(request):
    products = Product.objects.all()
    
    # Filter by price (if provided)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Filter by color (if provided)
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)

    # Filter by size (if provided)
    size = request.GET.get('size')
    if size:
        products = products.filter(size=size)


    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

  

    return render(request, 'core/product_list.html', {'products': products, 'products':page_obj, 'page_obj':page_obj})


def product_details(request, id):
    cd = Product.objects.get(pk=id)
    return render(request, 'core/product_details.html', {'cd':cd})


def product_list2(request):
    products = Product2.objects.all()
    
    # Filter by price (if provided)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Filter by color (if provided)
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)

    # Filter by size (if provided)
    size = request.GET.get('size')
    if size:
        products = products.filter(size=size)

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/product_list2.html', {'products': products, 'products':page_obj, 'page_obj':page_obj})


def product2_details(request, id):
    cd = Product2.objects.get(pk=id)
    return render(request, 'core/product2_details.html', {'cd':cd})



def clothe2_details(request, id):
    cd = DeeceCategory2.objects.get(pk=id)
    return render(request, 'core/clothe2_details.html', {'cd':cd})





def add_to_cart(request, model_type, id):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user) 

    if model_type == 'product':
        product = get_object_or_404(Product, pk=id)
        CartItem.objects.create(cart=cart, product=product) 
    elif model_type == 'product2':
        product2 = get_object_or_404(Product2, pk=id)
        CartItem.objects.create(cart=cart, product2=product2)  
    elif model_type == 'deece_category':
        deece_category = get_object_or_404(DeeceCategory2, pk=id)
        CartItem.objects.create(cart=cart, deece_category=deece_category) 
    else:
        raise Http404("Product not found.") 

    return redirect('view_cart')  

def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first() 
    if not cart:
        cart = None 

    cart_items = cart.items.all() if cart else []

    return render(request, 'core/view_cart.html', {'cart': cart, 'cart_items': cart_items})


def add_quantity(request, id):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, pk=id)
        item.quantity += 1
        item.save()
        return redirect('view_cart')
    else:
        return redirect('login')


def delete_quantity(request, id):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, pk=id)
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
        return redirect('view_cart')
    else:
        return redirect('login')
    

def delete_cart(request, id):
   if request.user.is_authenticated:
        del_cart = CartItem.objects.get(pk=id)
        del_cart.delete()
        return redirect('view_cart')
   else:
       return redirect('login')
   

def address(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mf = CustomerForm(request.POST)
            if mf.is_valid():
                # Save the valid form data
                user = request.user
                name = mf.cleaned_data['name']
                address = mf.cleaned_data['address']
                phone = mf.cleaned_data['phone']
                state = mf.cleaned_data['state']
                city = mf.cleaned_data['city']
                pincode = mf.cleaned_data['pincode']
                CustomerDetails(
                    user=user, 
                    name=name, 
                    address=address, 
                    phone=phone, 
                    state=state, 
                    city=city, 
                    pincode=pincode
                ).save()
                return redirect('address')
            else:
                # If form is not valid, display the form with errors
                address = CustomerDetails.objects.filter(user=request.user)
                return render(request, 'core/address.html', {'mf': mf, 'address': address})
        else:
            # Handle GET request, display the form and user's address data
            mf = CustomerForm()
            address = CustomerDetails.objects.filter(user=request.user)
            return render(request, 'core/address.html', {'mf': mf, 'address': address})

    else:
        # If user is not authenticated, redirect to login page
        return redirect('login')



def delete_address(request, id):
    if request.method == 'POST':
        da = CustomerDetails.objects.get(pk=id)
        da.delete()
    return redirect('address')




client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()

    if not cart:
        return render(request, 'core/checkout.html', {
            'cart_items': [],
            'total': 0,
            'delivery_charge': 0,
            'grand_total': 0
        })

    cart_items = cart.items.all()
    total = sum(getattr(item.product_instance, 'price', 0) * item.quantity for item in cart_items if item.product_instance)
    delivery_charge = 0
    grand_total = total + delivery_charge

    # Create Razorpay order
    razorpay_order = client.order.create({
        'amount': int(grand_total * 100),
        'currency': 'INR',
        'payment_capture': '1'
    })

    addresses = CustomerDetails.objects.filter(user=request.user)

    context = {
        'cart_items': cart_items,
        'total': total,
        'delivery_charge': delivery_charge,
        'grand_total': grand_total,
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'addresses':addresses,
    }
    return render(request, 'core/checkout.html', context)



@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        try:
            razorpay_payment_id = request.POST.get('razorpay_payment_id')
            razorpay_order_id = request.POST.get('razorpay_order_id')
            razorpay_signature = request.POST.get('razorpay_signature')

            # Log received data for debugging
            print("Received from Razorpay:")
            print(f"Payment ID: {razorpay_payment_id}")
            print(f"Order ID: {razorpay_order_id}")
            print(f"Signature: {razorpay_signature}")

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }

            # Initialize Razorpay client
            razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            # Verify the signature
            razorpay_client.utility.verify_payment_signature(params_dict)

            # If no exception, verification passed
            return render(request, 'core/payment_success.html')

        except razorpay.errors.SignatureVerificationError as e:
            print("Signature verification failed:", str(e))
            return render(request, 'core/payment_failed.html', {'error': 'Payment verification failed. Please contact support.'})

    return HttpResponse("Invalid request", status=400)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Payment, Cart, Order, CustomerDetails
import json
import razorpay

@csrf_exempt
def save_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        payment_id = data.get('payment_id')
        order_id = data.get('order_id')
        signature = data.get('signature')
        amount = data.get('amount')
        address_id = data.get('address_id')  # ✅ get selected address

        if not all([payment_id, order_id, signature, amount, address_id]):
            return JsonResponse({'status': 'failure', 'message': 'Missing required data'})

        try:
            amount = float(amount) / 100  # Razorpay sends amount in paisa

            # Verify payment signature
            client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })

           
            try:
                address = CustomerDetails.objects.get(id=address_id, user=request.user)
            except CustomerDetails.DoesNotExist:
                return JsonResponse({'status': 'failure', 'message': 'Invalid address selected'})

       
            payment = Payment.objects.create(
                user=request.user,
                order_id=order_id,
                payment_id=payment_id,
                payment_status='Success',
                amount=amount,
            )

            # Fetch user's cart
            cart = Cart.objects.get(user=request.user)
            cart_items = cart.items.all()

            if not cart_items.exists():
                return JsonResponse({'status': 'failure', 'message': 'Cart is empty!'})

            # Create order and save selected address
            order = Order.objects.create(
                user=request.user,
                cart=cart,
                payment=payment,
                address=address, 
                status="Confirmed"
            )


            # Clear cart items after successful order
            cart_items.delete()

            return JsonResponse({'status': 'success', 'payment_id': payment_id})

        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({'status': 'failure', 'message': 'Payment verification failed'})

        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': str(e)})

    return JsonResponse({'status': 'failure', 'message': 'Invalid request method'})



from django.core.mail import send_mail
from django.contrib import messages

def subscribe(request):
    if request.method == 'POST':
        mf = SubscriptionForm(request.POST)
        if mf.is_valid():
            email = mf.cleaned_data['email']
            send_mail(
                'subscription confirmation',
                'Thankyou 4 Subscribing DEECEMEN!',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False
            )
            messages.success(request, 'Thankyou for subscribing!')
            return redirect('subscribe')
    else:
        mf = SubscriptionForm()
    return render(request, 'core/subscribe.html', {'mf':mf})





def dashboard(request):
    if request.user.is_superuser:
        customer = CustomerDetails.objects.all()
        orders = Order.objects.select_related('user', 'payment').all()
        
        context = {
            'customer': customer,
            'ord': orders
        }
        return render(request, 'core/dashboard.html', context)
    else:
        messages.error(request, 'Access Denied: Superuser Only')
        return render(request, 'core/home.html')
    


def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('dashboard')  # or wherever you want

    return render(request, 'core/update_order.html', {'order': order})


def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('dashboard')




def order_success(request):
    payment_id = request.GET.get('payment_id')
    try:
        payment = Payment.objects.get(payment_id=payment_id, user=request.user)
        order = Order.objects.get(payment=payment, user=request.user)
        address = order.address  # assuming ForeignKey to CustomerDetails
    except (Payment.DoesNotExist, Order.DoesNotExist):
        payment = None
        address = None

    return render(request, 'core/order_success.html', {
        'payment': payment,
        'address': address
    })



from django.contrib.auth.decorators import login_required

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'core/my_orders.html', {'orders': orders})


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')