from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Tweet(models.Model):
    class Meta(object):
        db_table = 'tweet'
    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=14, db_index=True
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True, null=True
    )
    like = models.PositiveBigIntegerField('like', default=0, blank=True
    )
    image = CloudinaryField('image', blank=True, null=True
    )
