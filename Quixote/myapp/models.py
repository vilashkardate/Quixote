from email.policy import default
from statistics import mode
from django.db import models

# Create your models here.
class Image_Model(models.Model):
    size            = models.CharField(max_length=50,default="")
    resolution      = models.CharField(max_length=100,default="")
    timestamp       = models.CharField(max_length=100,default="")
    filename        = models.CharField(max_length=100,default="")
    file_extension  = models.CharField(max_length=100,default="")
    image_id        = models.CharField(max_length=100,default="")

    def __str__(self) -> str:
        return self.image_id