from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from .models import Customer
from .models import Restaurent

# Create your views here.
def index(request):
    return render(request,'index.html')

def open_signin(request):
    return render(request,'signin.html')

def open_signup(request):
    return render(request,'signup.html')

def signup(request):
    #return HttpResponse("recived")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

    try:
        Customer.objects.get(username=username)
        return HttpResponse("duplicate names not allowed")
    except:

        # creating customer object tabel
        Customer.objects.create(username = username,
                                password = password,
                                email = email,
                                mobile = mobile,
                                address = address)
        return render(request,'signin.html')
    
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  

    try:
        Customer.objects.get(username=username,
                               password = password)

            
        if username == 'admin':
                return render(request,'admin_home.html')
        else:
               return render(request,'customer_home.html')
            
    except Customer.DoesNotExist:
            return render(request,'fail.html')      

def add_restaurent_page(request):
     return render(request,'add_restaurent.html')

# add restaurent
def add_restaurent(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          picture = request.POST.get('picture')
          cuisine = request.POST.get('cuisine')
          rating = request.POST.get('rating')

          Restaurent.objects.create(name=name,
                                    picture=picture,
                                    cuisine=cuisine,
                                    rating=rating)

          restaurants = Restaurent.objects.all()
          return render(request, 'show_restaurants.html',{'restaurants':restaurants})
     return HttpResponse("Invalid Request")

# show reataurant
def open_show_restaurant(request):
     restaurants = Restaurent.objects.all()
     return render(request,'display_restaurant.html',{'restaurants':restaurants})

# update
def open_update_restaurant(request, id):
    restaurant = get_object_or_404(Restaurent, id=id)

    if request.method == 'POST':
        restaurant.name = request.POST.get('name')
        restaurant.picture = request.POST.get('picture')
        restaurant.cuisine = request.POST.get('cuisine')
        restaurant.rating = request.POST.get('rating')
        restaurant.save()

        restaurants = Restaurent.objects.all()

        return render(request, 'show_restaurants.html', {
            'restaurants': restaurants
        })

    return render(request, 'update_restaurant.html', {
        'restaurant': restaurant
    })

# delete
def delete_restaurant(request,id):
     restaurant = get_object_or_404(Restaurent,id=id)

     if request.method == 'POST':
          restaurant.delete()
          return redirect('open_show_restaurant')