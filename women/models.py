from django.db import models

<<<<<<< HEAD
=======

>>>>>>> fea1ddb08459080fe811979e2bf507e42621471a
class Women(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
    is_published = models.BooleanField(default=True)
=======
    is_published = models.BooleanField(default=True)
>>>>>>> fea1ddb08459080fe811979e2bf507e42621471a
