from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Employee, Product,UserProfile
from .forms import CreateEmployeeForm, CreateUserForm
# Create your views here.

#test
def testPage(request):
    return render(request,'mainapp/base.html')

#registratsya
def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login_user')
        
    context = {
        'form': form
    }       
    
    return render(request,'mainapp/registrations.html')


#loginUser
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, "Username or password was incorrect")
            
    context = {
        
    }   
    
    return render(request, 'mainapp/login.html') 


#Logout
def logoutUser(request):
    logout(request)
    return redirect('login_user')


#UserProfile
@login_required(login_url='login_user')
def user_profile(request):
    profiles = UserProfile.objects.all()
    context = {
        'username': request.user,
        'profiles': profiles
    }
    
    return render(request, 'mainapp/user_profile.html',context) 


#Asosiy
@login_required(login_url='login_user')
def dashboard(request):
    return render(request,'mainapp/dashboard.html')


#Employee table
@login_required(login_url='login_user')
def employee_table(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request,'mainapp/tables.html',context)


#Product table
@login_required(login_url='login_user')
def product_table(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request,'mainapp/p_table.html',context)


#Create Emp    
@login_required(login_url='login_user')
def createEmployee(request):
    if request.user.is_superuser or request.user.is_staff:
            form = CreateEmployeeForm()
            if request.method == "POST":
                form = CreateEmployeeForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('e-table')
                else:
                    form = CreateEmployeeForm()
                    
                    
            contex = {
                'form':form
            }
            return render (request, 'mainapp/e_create.html', contex)

    else:
        return redirect('e-table')


#Update Emp
@login_required(login_url='login_user')
def updateEmployee(request,pk):
    if request.user.is_superuser or request.user.is_staff:
        employee = Employee.objects.get(id=pk)
        form = CreateEmployeeForm(instance=employee)
        if request.method == "POST":
                form = CreateEmployeeForm(request.POST,instance=employee)
                if form.is_valid():
                    form.save()
                    return redirect('e-table')
                
        context = { 
            'form': form
        }
        return render (request, 'mainapp/e_create.html', context)

    else:
        return redirect('e-table')


#delete emp
@login_required(login_url='login_user')
def deleteEmployee(request,pk):
    if request.user.is_superuser:
        employee = Employee.objects.get(id=pk)
        if request.method == "POST":
            employee.delete()
            return redirect  ('e-table')
        
        
        context = {
            'employee': employee
        }          
        return render (request, 'mainapp/e_delete.html', context)
    else:
        return redirect('e-table')