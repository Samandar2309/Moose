from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=212)
    message = models.TextField()

    def __str__(self):
        return self.name


class Contact2(models.Model):
    address = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.address
