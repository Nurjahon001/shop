from django.db import models

# Create your models here.
class Phone(models.Model):
    name=models.CharField(max_length=20)
    model_p=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    image=models.ImageField(upload_to='media/')
    phone_number=models.IntegerField()
    at_data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}. {self.name}   {self.phone_number} "