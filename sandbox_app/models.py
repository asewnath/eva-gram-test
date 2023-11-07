from django.db import models


class Plot(models.Model):
  title  = models.CharField(max_length=200)
  div    = models.TextField()
  script = models.TextField()

  def __unicode__(self):
    return self.title