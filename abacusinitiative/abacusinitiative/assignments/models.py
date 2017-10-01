from django.db import models
from accounts.models import Student
from accounts.models import Instructor
# Create your models here.
class Question (models.Model):
    text = models.TextField()
    correct_ans_text = models.CharField(
        max_length = 255,
    )
    correct_ans_num = models.DecimalField()
    ans_text = models.CharField(
        max_length = 255,
    )
    ans_num = models.DecimalField()
    ans_type = models.CharField(
        max_length = 20,
    )

class Forum_Post(models.model):
    query = models.TextField()
    poster = models.ForeignKey(
        'Student',
        on_delete = models.CASCADE,
    )
    linked_q = models.ForeignKey(
        'Question',
        on_delete = models.CASCADE,
    )
    posts = models.Manager()

class Forum_Response(models.model):
    text = models.TextField();
    poster = models.ForeignKey(
        'Student',
        on_delete = models.CASCADE,
    )
    response_to = models.ForeignKey(
        'Forum_Post',
        on_delete = models.CASCADE,
    )

class Instructor_Response(models.model):
    text = models.TextField();
    poster = models.ForeignKey(
        'Instructor',
        on_delete = models.CASCADE,
    )
    response_to = models.ForeignKey(
        'Forum_Post',
        on_delete = models.CASCADE,
    )
