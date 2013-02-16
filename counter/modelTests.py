from counter.models import *
import unittest

class TestModels(unittest.TestCase):
    def setUp(self):
        TESTAPI_resetFixture()
        self.a = UserModel(user='a', password='', count=1)
        self.a.save()
        self.b = UserModel(user='b', password='', count=1)
        self.b.save()
        self.c = UserModel(user='c', password='a', count=1)
        self.c.save()
        self.d = UserModel(user='d', password='p', count=1)
        self.d.save()
    
    def tearDown(self):
        TESTAPI_resetFixture()
        
    def test_login1(self):
        r = login('a', '')
        self.asserEqual(2, r)
        
    def test_login2(self):
        r = login('a', '')
        self.asserEqual(3, r)
    
    def test_login3(self):
        r = login('a', 'b')
        self.assertEqual(-1, r)
        
    def test_login4(self):
        r = login('c', '')
        self.assertEqual(-1, r)
    
    def test_login5(self):
        r = login('', 'foo')
        self.assertEqual(-1, r)
        
    def test_add1(self):
        r = add('e', 'foo')
        self.assertEqual(1, r)
    
    def test_add2(self):
        r = add('a', '')
        self.assertEqual(-2, r)
    
    def test_add3(self):
        r = add('', '')
        self.assertEqual(-3, r)
    
    def test_add4(self):
        r = add('e', 'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop')
        self.assertEqual(-4, r)
    
    def test_reset1(self):
        r = TESTAPI_resetFixture()
        self.assertEqual(1, r)
    
    def test_reset2(self):
        r = TESTAPI_resetFixture()
        u = add('a', '')
        self.assertEqual(1, u)
        