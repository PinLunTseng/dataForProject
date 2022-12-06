from django.contrib.auth.models import User
from django.db import models


class Assets(models.Model):
    name = models.TextField(max_length=200)


class Period(models.Model):
    date = models.DateTimeField()


class Index(models.Model):
    index = models.IntegerField()
    period = models.ForeignKey(Period, on_delete=models.CASCADE)


class Price(models.Model):
    assets = models.ForeignKey(Assets, on_delete=models.CASCADE)
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    price = models.FloatField()


class WeightMV(models.Model):
    assets = models.ForeignKey(Assets, on_delete=models.CASCADE)
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    weight = models.FloatField()


class WeightCVaR(models.Model):
    assets = models.ForeignKey(Assets, on_delete=models.CASCADE)
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    weight = models.FloatField()


class WeightWOmega(models.Model):
    assets = models.ForeignKey(Assets, on_delete=models.CASCADE)
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    weight = models.FloatField()


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    risk_preference = models.FloatField(default=0)
    amount = models.FloatField(default=0)


class AssetsDetail(models.Model):
    name = models.TextField()
    full_name = models.TextField()
    industry_code = models.IntegerField()
    recommend_score = models.FloatField()
    introduction = models.TextField()
    link_yahoo_finance = models.TextField()
    link_official_website = models.TextField()


class Industry(models.Model):
    name = models.TextField()

