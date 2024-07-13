from django.db import models
from django.core.validators import RegexValidator

class Test(models.Model):
    city = models.CharField(max_length=200, validators=[RegexValidator(r'^[\w\d]+$')], blank=True,null=True)
    code = models.IntegerField(null=True,blank=True,default=0)
    year = models.IntegerField(null=True,blank=True)
    month = models.IntegerField(null=True,blank=True)
    in_process = models.IntegerField(null=True,blank=True)
    condition1 = models.IntegerField(null=True,blank=True)
    condition2 = models.IntegerField(null=True,blank=True)
    Condition3 = models.IntegerField(null=True,blank=True )
    total_condition = models.IntegerField(null=True,blank=True)
    

    def save(self, *args, **kwargs):
        self.total_condition = self.condition1 + self.condition2 + self.Ccondition3
        super().save(*args, **kwargs)
