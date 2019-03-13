from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """the topics user learned"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.deletion.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """learned specific knowledge about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."