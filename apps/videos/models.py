from django.db import models
from uuid import uuid4


class Video(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  url = models.URLField(null=False)
  downloaded_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{id}"
