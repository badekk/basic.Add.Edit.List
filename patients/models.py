from django.db import models
from django.utils import timezone
import uuid


class Patients(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    pesel = models.CharField(max_length=11)
    date_now = models.DateTimeField(default=timezone.now)
    info = models.TextField(blank=True)


