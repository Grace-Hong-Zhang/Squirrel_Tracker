from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):

    x = models.FloatField(help_text = _('Longitude'))
    y = models.FloatField(help_text = _('Latitude'))
    unique_squirrel_id = models.CharField(max_length = 32, help_text=_('Unique Squirrel ID'),
                            primary_key=True)
    # hectare = models.CharField(max_length = 32, help_text = _('Hectare'))
    shift = models.CharField(max_length = 32, help_text = _('Time of day'), 
                            choices = (('AM', 'AM'), ('PM', 'PM')))
    date = models.CharField(max_length = 32, help_text = _('The format is in yyyy-mm-dd'))
    Unknown = '?'
    age = models.CharField(max_length = 32, help_text = _('Age of squirrel'),
                            choices = (('Juvenile', 'Juvenile'), ('Adult', 'Adult'), (Unknown, '?')), blank = True)
    primary_fur_color = models.CharField(max_length = 32, help_text = _('primary fur color'),
                            choices = (('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('Cinnamon','Cinnamon'), (None, '')), blank = True)
    # highlight_fur_color = models.CharField(max_length = 32, help_text = _('highlight fur color'),
    #                         choices = (('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('Cinnamon','Cinnamon'), (None, '')), blank = True)
    location = models.CharField(max_length = 128, help_text = _('location'),
                            choices = (('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), (None, '')), blank = True)
    specific_location = models.CharField(max_length = 128, help_text = _('Additional notes to the location'), blank = True)
    running = models.NullBooleanField(help_text = _('Running'), blank=True,)
    chasing = models.NullBooleanField(help_text = _('Chasing'), blank=True,)
    climbing = models.NullBooleanField(help_text = _('Climbing'), blank=True,)
    eating = models.NullBooleanField(help_text = _('Eating'), blank=True,)
    foraging = models.NullBooleanField(help_text = _('Foraging'), blank=True,)
    other_activities = models.CharField(help_text = _('Other Activities'), max_length = 128, null = True, blank = True)
    kuks = models.NullBooleanField(help_text = _('Kuks'), blank=True,)
    quaas = models.NullBooleanField(help_text = _('Quaas'), blank=True,)
    moans = models.NullBooleanField(help_text = _('Moans'), blank=True,)
    tail_flags = models.NullBooleanField(help_text = _('Tail Flags'), blank=True,)
    tail_twitches = models.NullBooleanField(help_text = _('Tail Twitches'), blank=True,)
    approaches = models.NullBooleanField(help_text = _('Approaches'), blank=True,)
    indifferent = models.NullBooleanField(help_text = _('Indifferent'), blank=True,)
    runs_from = models.NullBooleanField(help_text = _('Runs from where?'), blank=True,)
    other_interactions = models.CharField(max_length = 32, null=True)

    def __str__(self):
        return self.unique_squirrel_id
