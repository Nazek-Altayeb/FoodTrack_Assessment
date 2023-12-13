from django.db import models

BusinessDays = [
  ("Monday", "Monday"),
  ("Tuesday", "Tuesday"),
  ("Wednesday", "Wednesday"),
  ("Thursday", "Thursday"),
  ("Friday", "Friday"),
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



class OpeningHours(models.Model):
    """
    Define Opening Hours object
    """
    day = models.CharField(max_length=200,choices=BusinessDays)
    open_at = models.TimeField()
    close_at = models.TimeField()

    class Meta:
        ordering = ('day', 'open_at')
    
    def __str__(self):
        return f"The opening hours at {self.day} are from  {self.open_at} to {self.close_at}"
    

class Store(models.Model):
    """
    Define Store object
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    openingHours = models.ForeignKey(OpeningHours, related_name="opening_hours", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

