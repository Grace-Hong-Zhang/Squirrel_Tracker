from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):

    x = models.FloatField(help_text = _('Longititude'))
    y = models.FloatField(help_text = _('Latititude'))
    unique_squirrel_id = models.CharField(max_length = 32, help_text=_('Unique Squirrel ID'),
                            primary_key=True)
    hectare = models.CharField(max_length = 32, help_text = _('Hectare'))
    shift = models.CharField(max_length = 32, help_text = _('Time of day'), 
                            choices = (('AM', 'AM'), ('PM', 'PM')))
    date = models.CharField(max_length = 32, help_text = _('Date'))
    age = models.CharField(max_length = 32, help_text = _('Age of squirrel'),
                            choices = (('Juvenile', 'Juvenile'), ('Adult', 'Adult')))
    primary_fur_color = models.CharField(max_length = 32, help_text = _('primary fur color'),
                            choices = (('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')))
    highlight_fur_color = models.CharField(max_length = 32, help_text = _('highlight fur color'),
                            choices = (('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')))
    location = models.CharField(max_length = 32, help_text = _('location'),
                            choices = (('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')))
    specific_location = models.CharField(max_length = 32, help_text = _('Specific location'))
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length = 32)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()
    other_interactions = models.CharField(max_length = 32, null=True)

    def __str__(self):
        return self.unique_squirrel_id
