from django.db import models

# Create your models here.

class Fbpage(models.Model):

 facebook_page = models.CharField(verbose_name='Facebookページ名', max_length=20, null=True, blank=True)
 good_number = models.CharField(verbose_name='いいね数', null=True, blank=True, max_length=20)
 category_name = models.CharField(verbose_name='カテゴリ名', max_length=20, null=True, blank=True)
 created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
 id_number = models.CharField(verbose_name='id', max_length=20, null=True, blank=True)
 objects = models.Manager()

 class Meta:
  verbose_name_plural = 'Fbpage'


class Fbdate(models.Model):
 text = models.TextField(verbose_name='テキスト', blank=True, null=True)
 photo = models.TextField(verbose_name='画像', blank=True, null=True)
 id_number = models.TextField(verbose_name='id', null=True, blank=True)
 k_id = models.TextField(verbose_name='k_id', null=True, blank=True)
 day = models.TextField(verbose_name='day', null=True, blank=True)
 uploaded_at = models.DateTimeField(auto_now_add=True)
 objects = models.Manager()

 class Meta:
  verbose_name_plural = 'Fbdate'