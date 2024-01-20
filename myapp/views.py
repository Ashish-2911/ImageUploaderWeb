from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()       
    form = ImageForm() 
    img = Image.objects.all()          
    return render(request,'myapp/home.html',{'form':form,'img':img})


def photoShow(request,id):
    # if request.method == 'POST':
    images = Image.objects.get(pk=id)
    return render(request,'myapp/photoshow.html',{'img':images})

#website to be continue......
