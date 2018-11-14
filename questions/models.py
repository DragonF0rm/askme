from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


def make_num_human_readable(num):
    if num % 1000000 != 0:
        return str(num % 1000000)+'m'
    if num % 1000 != 0:
        return str(num % 1000)+'k'
    return str(num)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    #TODO check and fix upload_to
    avatar = models.ImageField(default='default_user_avatar.png',
                               upload_to='user_avatars')


class Tag(models.Model):
    text = models.SlugField(unique=True)

    def get_tag(self):
        self.usage += 1
        self.save()
        return self.text

    #def get_


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='questions')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '[pk={}] {}'.format(self.pk, self.title)

    def get_text_preview(self):
        #TODO make better, maybe add <cut>i
        #Maybe truncate
        return self.text[:256]+'...'

    def get_creation_time(self):
        return self.created_at.strftime("%d %b %Y at %H:%M")

    def get_answers_count(self):
        return Answer.objects.all().filter(question__pk=self.pk).count()

    def get_answers(self):
        return Answer.objects.all().filter(question__pk=self.pk).count()

    def get_tags(self):
        return self.tags.all()

    def get_votes(self):
        result = 0
        for i in Vote.objects.filter(question=self):
            if i.vote:
                result += 1
            elif i is False:
                result -= 1
        return result

    #def get_absolute_url(self):
        #return reverse("question", kwargs={"pk": self.pk})


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_creation_time(self):
        return self.created_at.strftime("answered %d %b %Y at %H:%M")


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote = models.NullBooleanField()

    def make_vote(self, boolean):
        self.vote = boolean
        self.save()
