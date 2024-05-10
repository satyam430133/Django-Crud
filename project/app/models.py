from django.db import models

# Create your models here.

class InfoModel(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    def __str__(self):
        return str(self.Name)
    class Meta():
        verbose_name_plural = 'Student_List'