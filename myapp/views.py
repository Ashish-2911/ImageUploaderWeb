from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            form = ImageForm()   
            return redirect('/')    
    form = ImageForm() 
    img = Image.objects.all()          
    return render(request,'myapp/home.html',{'form':form,'img':img})


def photoShow(request,id):
    images = Image.objects.get(pk=id)
    return render(request,'myapp/photoshow.html',{'img':images})

#website to be continue......


from django.http import HttpResponse
from django.views.decorators.cache import cache_page
import datetime

@cache_page(60 * 2)  # 2 minutes ke liye cache
def my_cached_view(request):
    now = datetime.datetime.now()
    return HttpResponse(f"Cached Time: {now}")
