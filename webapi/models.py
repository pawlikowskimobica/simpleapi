from django.db import models
import hashlib
import random,string

class Client(models.Model):
    token=models.CharField(max_length=64,unique=True,default=''.join(random.choice(string.ascii_letters + string.digits) for i in range(64)))


class Pair(models.Model):
    client = models.ForeignKey(Client)
    key=models.CharField(max_length=20)
    value=models.CharField(max_length=100)

    class Meta:
        unique_together = ("client", "key")

    def clean(self):
        """This method checks if key length is less than 1. If True raises ValidationError"""
        if len(self.key)<1:
            raise ValidationError('Key should be between 1 and 20 characters long')

    def save(self, *args,**kwargs):
        self.clean()
        return super(Pair, self).save(*args, **kwargs)