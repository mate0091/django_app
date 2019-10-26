from django.db import models

# Create your models here.
class Actor(models.Model):

    actor_id = models.PositiveSmallIntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actor'
