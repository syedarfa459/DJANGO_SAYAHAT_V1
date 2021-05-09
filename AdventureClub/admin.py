from django.contrib import admin
from AdventureClub import models

admin.site.register(models.AdventureClub)
admin.site.register(models.AdventureEvent)
admin.site.register(models.EventBooking)
admin.site.register(models.TouristReview)