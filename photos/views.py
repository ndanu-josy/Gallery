from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def my_gallery(request):
    return render(request, 'gallery.html')

def search_images(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_image = Image.search_by_category(categoey)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html',{"message":message})    
        

