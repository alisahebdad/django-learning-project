from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_url = models.CharField(max_length=700,default='https://canape.cdnflexcatering.com/themes/frontend/default/images/img-placeholder.png')
    def __str__(self) -> str:
        return f'{self.item_name} ({self.item_price})'