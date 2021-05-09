from django.db import models
from django.contrib.auth.models import User


class AdventureClub(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default="",editable=False)
    club_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=11, default='')
    email = models.EmailField(null=True)
    club_address = models.CharField(max_length=150)
    city=models.CharField(null=False,blank=False,default="",max_length=256)

    def __str__(self):
        return self.club_name


class AdventureEvent(models.Model):
    # event_by = models.ForeignKey(AdventureClub, on_delete=models.CASCADE)
    event_by = models.CharField(max_length=100)
    title = models.CharField(max_length=256)
    overview = models.CharField(max_length=256, default='')
    image = models.ImageField(null=True, upload_to='AdventureClub/AdventureEventPics')
    event_start_date = models.DateField()
    event_end_date = models.DateField()

    def __str__(self):
        return "Club- " + self.event_by.club_name + '-' + self.title


class EventBooking(models.Model):
    booked_event = models.ForeignKey(AdventureEvent, on_delete=models.CASCADE)
    start_point = models.CharField(max_length=150, null=True)
    destination = models.CharField(max_length=150, null=True)

    def __str__(self):
        return "BookedEventFrom- " + str(self.booked_event)


class TouristReview(models.Model):
    tourist_id = models.ForeignKey(User, on_delete=models.CASCADE, )
    adventureevent = models.ForeignKey(AdventureEvent, on_delete=models.CASCADE)
    tourist_review = models.CharField(max_length=256)

    def __str__(self):
        return str(self.tourist_id)
