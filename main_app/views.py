from django.shortcuts import render , redirect #21
from django.http import HttpResponse
from . models import Cat , Toy # 2-6
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.views.generic import ListView , DetailView #2-7
from .forms import FeedingForm #11
from django.contrib.auth.forms import UserCreationForm #3-9
from django.contrib.auth import login #3-11
from django.contrib.auth.decorators import login_required #3-15 and apply in each def is need
from django.contrib.auth.mixins import LoginRequiredMixin #3-17 and apply in each class is need 

# Create your views here.

class CatCreate(LoginRequiredMixin,CreateView):
    model = Cat
    fields = ['name' , 'breed' , 'description' , 'age' , 'image']
    # fields = '__all__'
    # success_url = '/cats/'
    #3-7
    def form_valid(self , form):
       form.instance.user = self.request.user
       return super().form_valid(form)


class CatUpdate(LoginRequiredMixin,UpdateView):
    model = Cat
    fields=[ 'breed' , 'description' , 'age']  

class CatDelete(LoginRequiredMixin,DeleteView):
    model = Cat
    success_url = '/cats/'      

def home(request):
    return render(request , 'home.html')

def about(request):
    return render(request , 'about.html')

@login_required #3-16
def cats_index(request):
    
    # SELECT * FROM 'main_app_cat;'
    # cats = Cat.objects.all() # .find()
    #3-14
    cats = Cat.objects.filter(user=request.user)
    return render(request, 'cats/index.html', { 'cats': cats })

@login_required
def cats_detail(request , cat_id):
    cat=Cat.objects.get(id=cat_id)
    #2-21 // Get the toys , Cat doesn't have
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
    feeding_form = FeedingForm() #12
    return render(request,'cats/detail.html',{'cat':cat , 'feeding_form':feeding_form , 'toys':toys_cat_doesnt_have}) #13  // #2-22

@login_required
def add_feeding(request , cat_id): #20
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail' , cat_id=cat_id)    
        




class ToyList(LoginRequiredMixin,ListView):#2-5
  model = Toy#2-8

#2-9  
class ToyDetail(LoginRequiredMixin,DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin,CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin,UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin,DeleteView):
  model = Toy
  success_url = '/toys/'

#2-17
@login_required
def assoc_toy(request , cat_id,toy_id):
   Cat.objects.get(id=cat_id).toys.add(toy_id)
   return redirect('detail' , cat_id = cat_id)

@login_required
def unassoc_toy(request , cat_id,toy_id):
   Cat.objects.get(id=cat_id).toys.remove(toy_id)
   return redirect('detail' , cat_id = cat_id)


#3-10
def Signup(request):
   error_message =''
   if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request,user)
         return redirect('index')
      else:
         error_message = 'Invalid Signup - Try Again...'

   form = UserCreationForm()
   context ={'form':form , 'error_message': error_message}
   return render(request , 'registration/signup.html' , context)      

