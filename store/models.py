from django.db import models

OpeningHours = [
  ("00:06 AM", "00:06 AM"),
  ("00:09 AM", "00:09 AM"),
  ("00:12 PM", "00:12 PM"),
]

class Address(models.Model):
    """
    Define address object
    """
    city = models.CharField(max_length=200, null=False, blank=False)
    state = models.CharField(max_length=200, null=False, blank=False)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.city + ' ' + self.state + ', ' + str(self.zipcode)

    """ def save(self, *args, **kwargs):
        super().save()"""
    

class Store(models.Model):
    """
    Define Store object
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.OneToOneField(Address, related_name="address", on_delete=models.CASCADE)
    openingHours = models.CharField(max_length=200,choices=OpeningHours)

    def __str__(self):
        return self.name

    """def save(self, *args, **kwargs):
        super().save()"""


