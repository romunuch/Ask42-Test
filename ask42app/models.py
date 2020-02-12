from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Data_jsonb(models.Model):
	some_element=JSONField()
