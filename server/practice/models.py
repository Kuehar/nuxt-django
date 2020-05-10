from django.db import models

# Create your models here.


CATEGORY = (
    (1, '飲料'),
    (2, '生花'),
)

class Item(models.Model):
    name = models.CharField(verbose_name='商品名',max_length=255,null=False)
    category = models.IntegerField(verbose_name='カテゴリ',choices=CATEGORY)
    image = models.FileField(verbose_name='画像')
    price = models.PositiveIntegerField(verbose_name='値段',null=False)
    description = models.TextField(verbose_name='詳細',blank=True,null=True)

    def __str__(self):
        return self.name