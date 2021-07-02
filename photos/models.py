from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)        

    def __str__(self):
        return self.name

    def save_location(self):
        self.save() 

    def delete_location(self):
        self.delete()         

    @classmethod
    def get_image_locations(cls):
        locations = Location.objects.all()
        return locations      


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()  

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    description = models.TextField()  
    location = models.ForeignKey(Location ,on_delete=models.CASCADE,default='0')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='0')

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, image):
        cls.objects.filter(id = id).update(image=image)
        self.update()

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod  
    def search_image(cls, category):
        image = cls.objects.filter(category__icontains=category)
        return news   
      





        
                  