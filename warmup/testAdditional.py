"""
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""

import unittest
import os
import testLib


class TestAdd(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def test_Adding1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        self.assertResponse(respData, count = 1)
        
    def test_Adding2(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        self.assertResponse(respData, count = None, errCode = -2)
    
    def test_Adding3(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'b'} )
        self.assertResponse(respData, count = None, errCode = -3)
    
    def test_Adding4(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop', 'password' : 'b'} )
        self.assertResponse(respData, count = None, errCode = -3)
    
    def test_Adding5(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'b', 'password' : 'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop'} )
        self.assertResponse(respData, count = None, errCode = -4)

class TestLogin(testLib.RestTestCase):
    """Test logging users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def test_Logging1(self):
        respData0 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        self.assertResponse(respData, count = 2)
    
    def test_Logging2(self):
        respData0 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        respData01 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        self.assertResponse(respData, count = 3)
        
    def test_Logging3(self):
        respData0 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : '', 'password' : 'b'} )
        self.assertResponse(respData, count = None, errCode = -1)
    
    def test_Logging4(self):
        respData0 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'a', 'password' : ''} )
        self.assertResponse(respData, count = None, errCode = -1)
    
    def test_Logging5(self):
        respData0 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'c', 'password' : 'd'} )
        self.assertResponse(respData, count = None, errCode = -1)

class TestReset(testLib.RestTestCase):
    """Test resetting users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def test_Resetting1(self):
        respData0 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a', 'password' : 'b'} )
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST")
        self.assertResponse(respData, count = None)
    
    def test_Resetting2(self):
        respData0 = self.makeRequest("/TESTAPI/resetFixture", method="POST")
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST")
        self.assertResponse(respData, count = None)