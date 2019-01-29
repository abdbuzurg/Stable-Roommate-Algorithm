from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from . data import COUNTRIES, YEAR, SIZE, CAMPUSES


class Survey(models.Model):
    full_name = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date_published', auto_now_add = True)
    email = models.EmailField(max_length=254)
    country = models.PositiveSmallIntegerField(choices=COUNTRIES) # 0->KG, 1->TJ, 2->KZ
    campus = models.PositiveSmallIntegerField(choices=CAMPUSES) # 0 -> Naryn, 1-> Khorog, 2->Tekeli
    gender = models.PositiveSmallIntegerField(choices=((0,'Male'),(1,'Female')))
    year = models.PositiveSmallIntegerField(choices=YEAR) # (0 -> prep ... 4-> senior)
    scale1 = models.IntegerField()
    scale2 = models.IntegerField()
    scale3 = models.IntegerField()
    scale4 = models.IntegerField()
    scale5 = models.IntegerField()
    scale6 = models.IntegerField()
    scale7 = models.IntegerField()
    scale8 = models.IntegerField()
    extra1 = models.TextField(max_length=500, blank=True)
    extra2 = models.TextField(max_length=100)
    extra3 = models.CharField(max_length=50, blank=True)
    extra4 = models.PositiveSmallIntegerField(choices=SIZE)
    extra5 = models.PositiveSmallIntegerField(choices=SIZE)
    extra6 = models.TextField(max_length=500, blank=True)


    def __str__(self):
        # return '%s %s' % (self.surname, self.first_name)
        return '%s' % (self.full_name)
