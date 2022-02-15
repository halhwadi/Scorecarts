from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class TicketModel(models.Model):
    priority_list = [("1", "high"), ("2", "moderate"), ("3", "Low")]
    status_list = [("1", "on_progress"), ("2", "closed")]

    createdby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket')
    Title = models.CharField(max_length=100, blank=False,null=False)
    Description = models.TextField(max_length=1000, blank=False, null=False)
    priority = models.CharField(max_length=2, choices=priority_list, default=None, blank=False, null=False)
    status = models.CharField(max_length=2, choices=status_list, default=None, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    uu_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    slug = models.SlugField(null=False, unique=True, editable=False)



    def __str__(self):
        return f'{self.createdby.username}-{str(self.id)}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uu_id)
        return super().save(*args, **kwargs)

