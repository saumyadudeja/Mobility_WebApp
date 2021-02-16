from django.http.response import Http404
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from .forms import UseCaseForm, AttributeValueForm,CreateUserForm
from .models import *
'''use this later'''


def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')

    context ={}
    return render(request,'maas/login.html',context)

def registerPage(request):
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+user)
            return redirect('login')

    context ={'form':form}
    return render(request,'maas/register.html',context)

def logoutUser(request):
    logout(request)

    return redirect('login')
    context ={}
    return render(request,'maas/logout.html',context)

@login_required(login_url='login')
def home(request):
    # form_class = UseCaseForm
    # context = {'form_class':form_class}

    # if request.method=='POST':
    #     form = UseCaseForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    context = {}
    return render(request,'maas/dashboard.html',context)

#@login_required
class UseCaseClass(View):
    form_class = UseCaseForm
    initial = {'key':'value'}
    template_name = 'maas/home.html'

    
    def get(self,request,*args,**kwargs):
        form = self.form_class(initial=self.initial)
        context = {'form':form}
        return render(request,self.template_name,context)

    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        context = {'form':form}
        #use_case = UseCase.objects.get(pk=pk)
        if form.is_valid():
            name = form.cleaned_data['name']
            try:
                form.save()
            except:
                raise Http404("This Use Case cannot be saved.")
        return render(request, self.template_name,context)

def technology(request):
    template = 'maas/technology.html'
    context = {}
    category_list = Category.objects.all()
    attribute_list = Attribute.objects.all()
    
    context = {'attribute_list':attribute_list,'category_list':category_list}

    return render(request,template,context)



'''later'''
# class Technology(View):
#     form_class = AttributeValueForm
#     initial = {'key':'value'}
#     template_name = 'maas/technology.html'

#     def get(self,request,*args,**kwargs):
#         form = self.form_class(initial=self.initial)
#         context = {'form':form}
#         return render(request,self.template_name,context)

#     def post(self,request,*args,**kwargs):
#         form = self.form_class(request.POST)
#         context = {'form':form}
#         if form.is_valid():
#             form.save()
#         return render(request,self.template_name,context)


