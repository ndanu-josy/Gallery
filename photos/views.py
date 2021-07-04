from django.shortcuts import render
from . models import Image,Location
# Create your views here.
def home(request):
    return render(request, 'home.html')

def my_gallery(request):
    return render(request, 'gallery.html')

def search_images(request):

    if 'category' in request.GET and request.GET["category"]:
        images = request.GET.get("category")
        searched_images = Image.search_images(images)
        message = f"{images}"

        return render(request, 'search.html',{"message":message,"photos": searched_images})

    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html',{"message":message})    
        
def image(request,image_id):

    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})

def gallery(request):
    images=Image.objects.all()
    locations=Location.objects.all()
    return render (request, 'gallery.html', {'images':images,'locations':locations})
    
def locations(request,location):
    locations = Image.get_image_by_location(location)
    return render(request,'locations.html',{'locations':locations})