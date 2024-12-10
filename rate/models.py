from django.db import models


# Create your models here.
class Birga(models.Model):
    dollar = models.FloatField()
    eBro = models.FloatField()
    tenge = models.FloatField()
    som = models.FloatField()    
    time = models.DateTimeField()
    class Meta:
         ordering = ("time",) 

    def __str__(self):
            return f"Доллар {self.dollar} Евро {self.eBro} Тенге {self.tenge} Сом {self.som} Время и дата {self.time}"    
