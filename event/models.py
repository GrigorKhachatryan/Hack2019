from django.db import models


class Artists(models.Model):
    name = models.CharField(max_length=50)
    log = models.CharField(max_length=50)
    pas = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Events(models.Model):
    artist_id = models.ForeignKey(Artists, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField()
    #likes = models.IntegerField()
    #dislikes = models.IntegerField()

    def __str__(self):
        return self.title

class Fans(models.Model):
    ticket = models.CharField(max_length=50)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.ticket

class Polls(models.Model):
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Questions(models.Model):
    poll_id = models.ForeignKey(Polls, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return self.name


