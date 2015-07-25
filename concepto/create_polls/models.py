from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ethinicity = models.CharField(max_length=255)

    class Meta:
        app_label = 'create_polls'


class Polls(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField(blank=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(Users, null=True)
    stat = models.IntegerField(null=True)

    class Meta:
        app_label = 'create_polls'


class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    poll = models.ForeignKey(Polls)
    answer_text = models.TextField(blank=False)
    answer_img_url = models.CharField(max_length=255, null=True)
    answer_vid_url = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'create_polls'


class Votes(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.ForeignKey(Answers)
    user = models.ForeignKey(Users, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    loggedin = models.IntegerField()

    class Meta:
        app_label = 'create_polls'


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField()

    class Meta:
        app_label = 'create_polls'


class Category_Poll(models.Model):
    id = models.IntegerField(primary_key=True)
    poll = models.ForeignKey(Polls)
    category = models.ForeignKey(Categories)

    class Meta:
        app_label = 'create_polls'


class Mediums(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'create_polls'


class Shares(models.Model):
    id = models.IntegerField(primary_key=True)
    poll = models.ForeignKey(Polls)
    user = models.ForeignKey(Users)
    created_at = models.DateTimeField()
    medium = models.ForeignKey(Mediums)

    class Meta:
        app_label = 'create_polls'
