from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']
  
class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finchs/'

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  
 

# Create your views here.
def home(request):
  return render(request, 'home.html')
def about(request): 
  return render(request, 'about.html')

def finchs_index(request): 
  finchs = Finch.objects.all()
  return render(request, 'finchs/index.html', {'finchs': finchs})

def finchs_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  feeding_form = FeedingForm()
  return render(request, 'finchs/detail.html', {
    'finch': finch, 'feeding_form': feeding_form})
  
def add_feeding(request, finch_id): 
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)