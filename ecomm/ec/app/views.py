from django.db.models import Count 
from django.shortcuts import render,redirect
from django.views import View 
from .models import Product, Customer
from .forms import CustomerRegistrationForm,CustomerProfileForm, PasswordChangeForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")



class CategoryView(View):  
    def get(self, request, val):
        # Filter products based on the category slug
        products = Product.objects.filter(category=val)
        # Pass products to the template as context
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/Category.html",locals()) 

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())

class CategoryTitle(View):
    def get(self,request,val):
        products = Product.objects.filter(title=val)
        title = Product.objects.filter(category=products[0].category).values('title') 
        return render(request,"app/Category.html",locals()) 

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/customerregistration.html', locals())


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',locals())  

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcod']  

            # Create or update the customer instance
            reg, created = Customer.objects.update_or_create(
                user=user,
                defaults={
                    'name': name,
                    'locality': locality,
                    'city': city,
                    'mobile': mobile,
                    'state': state,
                    'zipcod': zipcode,  
                }
            )
            if created:
                messages.success(request, "Congratulations! Profile saved successfully.")
            else:
                messages.info(request, "Profile updated successfully.")
        else:
            messages.warning(request, "Invalid input data.")
        return render(request, 'app/profile.html',locals()) 


# to view the address filter user name 
def address(request):
    add =Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',locals()) 

#update address
class updateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/updateAddress.html', locals()) 

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            # Corrected 'Cleaned_data' to 'cleaned_data'
            add.name = form.cleaned_data['name']  
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcod = form.cleaned_data['zipcod']
            add.save()
            messages.success(request, 'Congratulations! Profile Updated Successfully')
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('address')


def add_to_cart(request):
    pass

