# makemigrations and migrate: locally worked. User & Profile
# are in pgadmin4 > geodjango server > postgres database
# should they be in gis?
# lab 5 step 1


from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    mpoly = models.MultiPolygonField(srid=4326)


def __str__(self):
    return self.name


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=15)

    def __str__(self):
        return str(self.username)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    lon = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return str(self.lon), str(self.lat)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

