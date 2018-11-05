from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


def make_num_human_readable(num):
    if num % 1000000 != 0:
        return str(num % 1000000)+'m'
    if num % 1000 != 0:
        return str(num % 1000)+'k'
    return str(num)


def make_month_human_readable(month):
    return {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }.get(month)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    #TODO check and fix upload_to
    avatar = models.ImageField(default='media/default_user_avatar.png',
                               upload_to='media/user_avatars')


#class TagManager(models.Manager):
    #def get_tags(self, _question):


class Tag(models.Model):
    text = models.SlugField(unique=True)
    usage = models.PositiveIntegerField(default=0)

    #TODO move to TagManager
    def get_tag(self):
        self.usage += 1
        self.save()
        return self.text

    #TODO move to TagManager
    def get_usage(self):
        return self.usage


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
        #TODO make better, maybe add <cut>
        return self.text[:64]+'...'

    def get_answers_count(self):
        manager = AnswerManager()
        return manager.get_answers_count(self)

    def get_answers(self):
        manager = AnswerManager()
        return manager.get_answers(self)

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


class AnswerQuerySet(models.QuerySet):
    def get_answers_count(self, _question):
        return self.filter(question=_question).count()

    def get_answers(self, _question):
        return self.filter(question=_question)


class AnswerManager(models.Manager):
    def get_queryset(self):
        return AnswerQuerySet(self.model, using=self._db)

    def get_answers_count(self, _question):
        return self.get_queryset().get_answers_count(_question)

    def get_answers(self, _question):
        return self.get_queryset().get_answers(_question)


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    #def get_creation_time(self):
        #return self.created_at.strftime("answered %d %b %Y at %H:%M")


#class VoteManager(models.Manager):
    #def get_votes(self, _question):
        #for i in super().get_queryset().filter(question )


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote = models.NullBooleanField()

    def make_vote(self, boolean):
        self.vote = boolean
        self.save()

    ##def has_vote(self,  question):


