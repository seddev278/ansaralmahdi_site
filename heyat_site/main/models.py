from django.db import models

class afrad(models.Model):
    name=models.CharField(max_length=100)
    masoliat=models.CharField(max_length=100)
    bio=models.TextField(blank=True,null=True)
    aks=models.ImageField(upload_to='aks_afrad/',blank=True,null=True)

    def __str__(self):
        return self.name
