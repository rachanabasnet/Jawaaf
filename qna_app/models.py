from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    c_title = models.CharField(max_length=255)
    c_desc = models.TextField(max_length=1200)

    def __str__(self):
        return (self.c_title)


class QuestionModel(models.Model):
    title = models.CharField(max_length= 255)
    posted_by = models.CharField(max_length=120)
    q_desc = models.TextField(max_length= 1500)
    timestamp = models.DateTimeField(auto_now_add=True)
    q_votes = models.IntegerField(default=0)
    q_img = models.ImageField(upload_to='QuestionImg', blank=True, null=True)
    category = models.ForeignKey(CategoryModel, on_delete= models.CASCADE)

    def __str__(self):
        return (self.title[:50] + '...')
        return (self.q_desc[:50] + '...')


class AnswerModel(models.Model):
    a_desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ans_by = models.CharField(max_length=120)
    a_votes = models.IntegerField(default=0)
    is_accepted = models.BooleanField(default=0)
    a_img = models.ImageField(upload_to='AnswerImg', blank=True, null= True)
    questions = models.ForeignKey(QuestionModel,on_delete= models.CASCADE)

    def __str__(self):
        return (self.a_desc[:50] + '...')