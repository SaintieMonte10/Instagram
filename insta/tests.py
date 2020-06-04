from django.test import TestCase
from . models import *

# Create your tests here.
class ImageTestClass(TestCase):
    '''
    This is a class that perform unnittest  behaviour on the Image Model.
    '''
    
    def setUp(self):
        
        self.image_one = Image(image='images/lagoon.jpeg',image_name='dan', image_caption='lacasa de papel',likes=40, id=1)
        
    def test_instance(self):
        Image.objects.all().delete()
        self.assertTrue(isinstance(self.image_one,Image)) 

    def test_save_method(self):
        
        self.image_one.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.image_one.save_image()
        self.image_one.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) is 0)
        
    def test_update_method(self):
        self.image_one.save()
        new_caption = 'That image is cool'
        done = self.image_one.update_caption(self.image_one.id,new_caption)
        self.assertEqual(done,new_caption)
        
    def tearDown(self):
        Image.objects.all().delete()
