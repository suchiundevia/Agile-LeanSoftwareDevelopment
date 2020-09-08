from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Activity(models.Model):
    activity_title = models.CharField(max_length=150)
    activity_description = models.TextField()
    activity_material = models.CharField(max_length=250)
    activity_start_time = models.DateTimeField()
    activity_end_time = models.DateTimeField()
    activity_post_date = models.DateTimeField(default=timezone.now)
    activity_location = models.CharField(max_length=250)
    activity_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.activity_title)

    # Redirect page
    def get_absolute_url(self):
        # Reverse returns the full path as a string
        return reverse('activity-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Activity'
