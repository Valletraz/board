from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

TANKS = 'TK'
HILI = 'HL'
DD = 'DD'
TRADERS = 'TR'
GILDMASTERS = 'GM'
QUESTGIVERS = 'QG'
BLACKSMITHS = 'BS'
TANNERS = 'TN'
POTIONBREWERS = 'PB'
SPELLMASTERS = 'SM'

CAT_CHOICE = (
    (TANKS, 'Танки'),
    (HILI, 'Хилы'),
    (DD, 'ДД'),
    (TRADERS, 'Торговцы'),
    (GILDMASTERS, 'Гилдмастеры'),
    (QUESTGIVERS, 'Квестгиверы'),
    (BLACKSMITHS, 'Кузнецы'),
    (TANNERS, 'Кожевники'),
    (POTIONBREWERS, 'Зельевары'),
    (SPELLMASTERS, 'Мастера Заклинаний'),
)


class Post(models.Model):
    add_time = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    message = models.TextField()
    category = models.CharField(max_length=2, choices=CAT_CHOICE)
    # upload = models.FileField(upload_to='uploads/')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def length(self):
        return self.pk.count()


class Response(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    isAccepted = models.BooleanField(default=False)

    def accept_response(self):
        self.isAccepted = True
        self.save()

    def delete_response(self):
        self.isAccepted = False
        self.save()
