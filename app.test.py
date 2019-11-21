import unittest

from hello import app

class BasicTestCase(unittest.TestCase):

    def test_pages(self):
        tester = app.test_client(self)
        pages = ['/', 'about', 'register', 'login']
        for page in pages:
            response = tester.get(page, content_type='html/text')
            self.assertEqual(response.status_code, 200)
    
    def test_other_page(self):
        tester = app.test_client(self)
        response = tester.get('test', content_type='html/text')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()