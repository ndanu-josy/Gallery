from django.test import TestCase
# Create your tests here.
from .models import Image, Category, Location

class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='nairobi')
        self.location.save_location()

    def test_instance(self):
        self.location.save()
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        location_test = Location.get_image_locations()
        self.assertTrue(len(location_test) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location_test = Location.objects.all()
        self.assertTrue(len(location_test) == 0) 
    

    def test_get_image_locations(self):
        self.location.save_location()
        self.location.save_location()
        location_test = Location.get_image_locations()
        self.assertFalse(len(location_test) > 1)

class TestCategory(TestCase):
    def setUp(self):
        self.category = Category(name='nature')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='nairobi')
        self.location.save_location()

        self.category = Category(name='nature')
        self.category.save_category()

        self.testInstance = Image(id=1, name='img', description=' my image', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.testInstance, Image))

    def test_save_image(self):
        self.testInstance.save_image()
        filterImage= Image.objects.all()
        self.assertTrue(len(filterImage) > 0)

    def test_delete_image(self):
        self.testInstance.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.testInstance.save_image()
        self.testInstance.update_image(self.testInstance.id, 'images/img.jpg')
        imgUpdt = Image.objects.filter(image='images/test.jpg')
        self.assertFalse(len(imgUpdt) > 0)

    def test_get_image_by_id(self):
        imageF = self.testInstance.get_image_by_id(self.testInstance.id)
        image = Image.objects.filter(id=self.testInstance.id)
        self.assertFalse(imageF, image)

    def test_search_image_by_location(self):
        self.testInstance.save_image()
        foundImages = self.testInstance.get_image_by_location(location='nairobi')
        self.assertTrue(len(foundImages) == 1)

    def test_search_image_by_category(self):
        category = 'food'
        foundImages = self.testInstance.search_images(category)
        self.assertFalse(len(foundImages) > 1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


     
   