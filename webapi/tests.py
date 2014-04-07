from django.test import TestCase
from models import *

class PairTest(TestCase):

    def test_client_validation(self):
        c=Client(token="aa")
        c.save()
        self.assertIsNotNone(c.pk)
        self.assertEqual(c.token,"aa")
        c2=Client()
        self.assertIsNotNone(c2.token)
        try:
            c2.save()
        except:
            pass
        self.assertIsNotNone(c2.pk)

    def test_pair_validation(self):
        c=Client()
        c.save()
        p=Pair(client=c,key="key1",value="value1")
        p.save()
        self.assertIsNotNone(p.pk)
        self.assertEqual(p.key,"key1")
        self.assertEqual(p.value,"value1")
        self.assertIsNotNone(p.client)
        p.key=""
        try:
            p.save()
            saved=True
        except:
            saved=False
        self.assertFalse(saved)
        
        p.key="asdfghjkl;asdfghjkl;1234567890"#more than 20 characters long, save should fail
        try:
            p.save()
            saved=True
        except:
            saved=False
        self.assertFalse(saved)
