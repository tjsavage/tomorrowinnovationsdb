from dashboard.models import Startup
from dashboard.models import Person
from dashboard.models import ReferenceSource
from dashboard.models import Review
from django.contrib import admin


    
admin.site.register(Startup)
admin.site.register(Person)
admin.site.register(ReferenceSource)
admin.site.register(Review)