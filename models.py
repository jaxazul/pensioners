# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PensionersDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    date_of_birth = models.CharField(max_length=256)
    status = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    service_begin = models.CharField(max_length=256)
    service_ends = models.CharField(max_length=256)
    last_assignment = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'pensioners_details'
