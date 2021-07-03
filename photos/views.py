from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def my_gallery(request):
    return render(request, 'gallery.html')

def search_images(request):

    if 'category' in request.GET and request.GET["category"]:
        images = request.GET.get("category")
        searched_images = Image.search_by_category(images)
        message = f"{images}"

        return render(request, 'search.html',{"message":message,"photos": searched_images})

    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html',{"message":message})    
        

