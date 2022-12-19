from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product, product_photo


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1,
            created_by_id=1,
            title='django beginners',
            slug='django-beginners',
            price='20.00',
            image='product/django/bike.jpg',
        )

    def test_product_model_entry(self):
        """
        Test product model data
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')

    def test_image_path(self):

        data = self.data1
        path = data.image.url
        fun = '/media/' + product_photo(data, 'bike.jpg')
        self.assertEqual(path, fun)
