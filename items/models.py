from django.db import models

class Item(models.Model):
    Item_ID = models.AutoField(primary_key=True)
    Item_Name = models.CharField(max_length=255)
    Type = models.CharField(max_length=100)
    Unit = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Item_Name
