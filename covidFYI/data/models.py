from django.db import models
from datetime import datetime

# Create your models here.
class InfoType(models.Model):

    name = models.CharField(max_length = 128, null=False)

    def __str__(self):

        return self.name

class Location(models.Model):

    state = models.CharField(max_length = 64, null=False)
    district = models.CharField(max_length = 64, null=False, blank=True)

    def __str__(self):

        return f'{self.state} - {self.district}'

class Entry(models.Model):

    location    = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='entries')
    # user_id     = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    infotype    = models.ForeignKey(InfoType, on_delete=models.CASCADE, related_name='entries')
    name        = models.CharField(max_length=128, null=False)
    dr_name     = models.CharField(max_length=128, null=True)
    email_id_1  = models.EmailField(max_length=128, null=True)
    email_id_2  = models.EmailField(max_length=128, null=True)
    phone_1     = models.EmailField(max_length=128, null=True)
    phone_2     = models.EmailField(max_length=128, null=True)
    extension   = models.EmailField(max_length=128, null=True)
    source_link = models.EmailField(max_length=128, null=True)
    source      = models.EmailField(max_length=128, null=True)
    details     = models.EmailField(max_length=1024, null=True)
    # added_on    = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    added_on    = models.DateTimeField(default=datetime.now, null=False)

    def __str__(self):

        return f'{self.name}'