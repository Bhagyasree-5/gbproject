from django.db import models
from django.utils import timezone
# Create your models here.
# models.py


class Chemicals(models.Model):
    chemical_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.chemical_name

class PurchasedDetails(models.Model):
    chem_name = models.ForeignKey(Chemicals,on_delete=models.CASCADE)
    Purchased_date = models.DateField(null=True,blank=True)
    Bill_no = models.CharField(max_length=100,null=True,blank=True)
    Rate = models.IntegerField(null=True,blank=True)
    Quantity_purchased = models.IntegerField(null=True,blank=True)
    Balance =  models.IntegerField(null=True,blank=True)
    
class Utensils(models.Model):
    uten_name = models.CharField(max_length=100, unique=True)
    uten_location = models.SmallIntegerField(null=True)
    price = models.IntegerField(default=0)  
    quantity = models.IntegerField(default=0) 

    def __str__(self):
        return self.uten_name

class Fine(models.Model):
    dept = [
        ('chemistry', 'Chemistry'),
        ('physics', 'Physics'),
        ('zoology', 'Zoology'),
        ('botony', 'Botony')
    ]
    yr = [
        (1, 'I year'),
        (2, 'II year'),
        (3, 'III year')
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('received', 'Received'),
    ]
    admn_no = models.IntegerField(null=False)
    Date = models.DateField(null=True, blank=True,default=timezone.now)
    Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100, choices=dept)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    Year = models.SmallIntegerField(choices=yr, null=True, blank=True)
    Item = models.ForeignKey(Utensils, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)


    def __str__(self):
        return self.Name

    @property
    def Price(self):
        return self.Item.price
    
    def save(self, *args, **kwargs):
        # Check if the instance is new
        if not self.pk:
            # Decrease the quantity of the related utensil if it's a new instance
            if self.Item.quantity > 0:
                self.Item.quantity -= 1
                self.Item.save()
        
        super(Fine, self).save(*args, **kwargs)

class UtensilsStock(models.Model):
    utensil =  models.ForeignKey("Utensils", on_delete=models.CASCADE)
    purchased_date = models.DateField(null=True, default=timezone.now)
    rate = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Update the quantity of the related utensil
        self.utensil.quantity += self.quantity
        self.utensil.save()
        super(UtensilsStock, self).save(*args, **kwargs)