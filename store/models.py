from django.db import models

class Address(models.Model):
    """
    Define address object
    """
    city = models.CharField(max_length=200, null=False, blank=False)
    state = models.CharField(max_length=200, null=False, blank=False)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.city + ' ' + self.state + ', ' + str(self.zipcode)
    


class Store(models.Model):
    """
    Define Store object
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.OneToOneField(Address, related_name="address", on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class OpeningHours(models.Model):
    """
    Define Opening Hours object
    """
    day = models.CharField(max_length=100, null=False, blank=False)
    open_at = models.TimeField(blank=False)
    store = models.ForeignKey(Store, related_name="openingHours" , on_delete=models.CASCADE)
    branch = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.day + ' at ' + str(self.open_at)
    

class Foods(models.Model):
    """
    Define Food object
    """
    foodName = models.CharField(max_length=100, default= 'not-specified',  null=False, blank=False)
    salesPerDay = models.IntegerField()
    returnedItemsPerDay = models.IntegerField()
    store = models.ForeignKey(Store, related_name="foods" , on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.salesPerDay} item have sold today, but {self.returnedItemsPerDay} are considered as waste'
    
