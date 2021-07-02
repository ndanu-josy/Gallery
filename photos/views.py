from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def my_gallery(request):
    return render(request, 'gallery.html')


