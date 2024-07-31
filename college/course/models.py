from django.db import models


class Course(models.Model):
    course_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    email = models.EmailField(max_length=200)
    
    def __str__(self):
        # return self.title
        return str(self.course_id)