from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    singer = models.ForeignKey(Singer, on_delete=models.PROTECT)
    lyrics = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('title', 'singer')

    def __str__(self):
        return self.title
