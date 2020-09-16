from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator


class Profile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(10)])
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="single", choices=(("single", "single"), (
        "married", "married")))
    gender = models.CharField(max_length=20, default="male", choices=(
        ("male", "male"), ("female", "female")))
    phone_no = models.CharField(validators=[RegexValidator(
        "[0]{1}[3]{1}[0-9]{2}[-]{1}[0-9]{7}")], max_length=15, null=True, blank=True, default='0300-0000000')
    description = models.TextField(null=True, blank=True)
    pic = models.ImageField(upload_to="gym/images/", null=True, blank=True)
    time = models.IntegerField(default=1, null=True, blank='True')

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    phone_no = models.CharField(validators=[RegexValidator(
        "[0]{1}[3]{1}[0-9]{2}[-]{1}[0-9]{7}$")], max_length=15, null=True, blank=True)
    subject = models.CharField(max_length=30)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Exercise(models.Model):
    name = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=20, default="male", choices=(
        ("male", "male"), ("female", "female")))
    chest = models.CharField(max_length=100, null=True, blank=True)
    back = models.CharField(max_length=100, null=True, blank=True)
    shoulder = models.CharField(max_length=100, null=True, blank=True)
    bitri = models.CharField(max_length=100, null=True, blank=True)
    leg = models.CharField(max_length=100, null=True, blank=True)
    six_pack = models.CharField(max_length=100, null=True, blank=True)
    cardio = models.CharField(max_length=100, null=True, blank=True)
    weight_lose = models.CharField(max_length=100, null=True, blank=True)
    balley_lose = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)
