from django.db import models
from user.models import Myuser
# Create your models here.
class Meeting (models.Model):
    title=models.CharField(max_length=50)
    reason=models.CharField(max_length=250)
    creator_id = models.ForeignKey('user.Myuser', on_delete=models.CASCADE)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    meeting_link=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class MeetingMember(models.Model):
    meeting= models.ForeignKey('Meeting', on_delete=models.CASCADE)
    user_id = models.ForeignKey('user.Myuser', on_delete=models.CASCADE)