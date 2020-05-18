from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArtistImages(models.Model):
    user=models.CharField(default='Surya Vamshi',max_length=20)
    img=models.ImageField(default='default.jpg',upload_to='pictures')
    caption=models.TextField(null=False,default='Beyond Beautiful')
    dateposted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.caption} taken by {self.user}'
    class Meta:
        db_table='ArtistImages'
