from django.db import models
from django.contrib.auth.models import User

class Startup(models.Model):
    STAGE_CHOICES = (
        ('S', 'Seed/Angel'),
        ('A', 'Round A'),
        ('B', 'Round B'),
        ('L', 'Late Stage'),
    )
    
    PRIORITY_CHOICES = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )
    
    NEXT_STEP_CHOICES = (
        ('H', 'Hold'),
        ('P', 'Pass'),
        ('D', 'Do Diligence'),
        ('G', 'Green Light'),
        ('I', 'Invested')
    )
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    idea = models.TextField(blank=True)
    problem = models.TextField(blank=True)
    users = models.TextField(blank=True)
    competitors = models.TextField(blank=True)
    money = models.TextField(blank=True)
    milestones = models.TextField(blank=True)
    url = models.URLField(blank=True)
    note = models.TextField(blank=True)
    reference_source = models.ManyToManyField('ReferenceSource', null=True, blank=True)
    stage = models.CharField(max_length=1, choices=STAGE_CHOICES, default='S')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='L')
    next_step = models.CharField(max_length=1, choices=NEXT_STEP_CHOICES, default='H')
    people = models.ManyToManyField('Person', null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, null=True)
    date_updated = models.DateField(auto_now=True, null=True)
    first_contact_date = models.DateField(null=True)
    first_pitch_date = models.DateField(null=True, blank=True)
    slide_deck = models.FileField(upload_to="slide_decks/", null=True, blank=True)
    term_sheet = models.FileField(upload_to="term_sheets/", null=True, blank=True)
    one_pager = models.FileField(upload_to="one_pagers/", null=True, blank=True)
    
    
    def __unicode__(self):
        return self.name

    def get_application_dict(self):
	dict = {}
	dict['Idea'] = self.idea
	dict['Problem'] = self.problem
	dict['Users'] = self.users
	dict['Competitors'] = self.competitors
	dict['Money'] = self.money
	dict['Milestones'] = self.milestones
	return dict
    
    def get_verbose_field(self, field):
	return self._meta.get_field_by_name(field)[0].verbose_name
    
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, null=True)
    date_updated = models.DateField(auto_now=True, null=True)
    background = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)
    note = models.TextField(blank=True)
    reference_source = models.ManyToManyField('ReferenceSource', null=True, blank=True)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.full_name()

class Review(models.Model):
    NEXT_STEP_CHOICES = (
        ('H', 'Hold'),
        ('P', 'Pass'),
        ('D', 'Do Diligence'),
        ('G', 'Green Light'),
        ('I', 'Invested')
    )
    
    date = models.DateField(auto_now=True, null=True)
    reviewer = models.ForeignKey(User)
    startup = models.ForeignKey('Startup', null=True)
    next_step = models.CharField(max_length=1, choices=NEXT_STEP_CHOICES, default='P')
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return self.reviewer.username + " reviews " + self.startup.name + ", says " + self.get_next_step_display()

class Update(models.Model):
    date = models.DateField(auto_now=True, null=True)
    added_by = models.ForeignKey(User)
    startup = models.ForeignKey('Startup')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
class ReferenceSource(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
    