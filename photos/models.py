from django.db import models

# Create your models here.
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