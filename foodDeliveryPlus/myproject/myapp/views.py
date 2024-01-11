import datetime

from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from .models import FoodItem, Contact, FoodCategory, FoodType, About, Order


def register(request):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            message = "Data saved successfully"
            return render(request, "signup.html", {"form": f, "m": message})
        else:
            message = "Something went wrong"
            return render(request, "signup.html", {"form": f, "m": message})
    else:
        f = UserCreationForm()
        return render(request, "signup.html", {"form": f})


def login(request):
    if request.method == "POST":
        log = AuthenticationForm(request, data=request.POST)
        if log.is_valid():
            name = log.cleaned_data["username"]
            pas = log.cleaned_data["password"]
            check = authenticate(username=name, password=pas)
            if check is not None:
                login(request)
                return redirect("/dash")
            else:
                message = "Something went wrong"
                return render(request, "login.html", {"log": log, "m": message})
        else:
            message = "Invalid credentials"
            return render(request, "login.html", {"log": log, "m": message})
    else:
        log = AuthenticationForm(request)
        return render(request, "login.html", {"log": log})


def welcome(request):
    if request.user.is_authenticated:
        a = request.user
        return render(request, "welcome.html", {"userinfo": a})
    else:
        return redirect("/login")


def logoutuser(request):
    logout(request)
    return redirect("/login")


def index(request):
    return render(request, 'index.html')


def about(request):
    desc = About.objects.all()
    return render(request, 'about.html', {"aboutDesc": desc})


def menu(request):
    item = FoodItem.objects.all()
    # item2 = FoodItem.objects.all().filter(Category=2)
    # item3 = FoodItem.objects.all().filter(Category=3)
    type = FoodType.objects.all()
    return render(request, 'menu.html', {"fItem": item, "ftype": type})


def booking(request):
    item = FoodItem.objects.all()
    if request.method == "POST":
        n = request.POST["orderName"]
        p = request.POST["orderPhone"]
        a = request.POST["orderAddress"]
        q = request.POST["orderQuantity"]
        OrderTimes = datetime.datetime.now()
        # t = request.POST["total"]
        i = request.POST["type"]
        fetchfood = FoodItem.objects.filter(Id=i).values_list('Price')
        # food_Price = fetchfood.Price
        fetchfoods = "".join(map(str, fetchfood[0]))
        TotalBill = q * int(fetchfoods)
        print(fetchfood)
        print(TotalBill)

        # for a in fetchfood:
            # print(a.Price)
            # food_Price = a.Price
            # TotalBill = q * food_Price
        datasave = Order.objects.create(Name=n, Phone=p, Address=a, Quantity=q, TotalBill = TotalBill, Item = fetchfood, OrderTime = OrderTimes)

        message = "Your order has been received , Your Total Bill is " + str(TotalBill)
        return render(request, 'booking.html', {"m": message, "fItem": item})

    return render(request, 'booking.html', {"fItem": item})


def contact(request):
    if request.method == "POST":
        a = request.POST["name"]
        e = request.POST["email"]
        s = request.POST["subject"]
        m = request.POST["message"]
        datasave = Contact.objects.create(Name=a,Email=e,Subject=s,Message=m)

        message = "Thankyou for contacting us"
        return render(request, 'contact.html', {"m": message})

    return render(request, 'contact.html')
