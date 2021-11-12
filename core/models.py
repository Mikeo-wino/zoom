from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

MEMBERSHIP_TYPE_CHOICES = [
    ('CC', 'Content creater'),
    ('Y', 'Youtuber'),

]
CONTENT_TYPE = [
    ('MATH', 'MATHEMATICS'),
    ('CS', 'COMPUTER_SCIENCE'),
    ('ENG', 'ENGINEERING'),
    ('ECON', 'ECONOMICS'),
    ('MED', 'MEDICINE'),
    ('MR', 'REVIEWING MOVIES'),
]
class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    What_are_you= models.CharField(choices=MEMBERSHIP_TYPE_CHOICES, max_length=200, default='CC')
    Which_educational_or_tutorial_content_can_you_create_or_looking_for=models.CharField(
        choices=CONTENT_TYPE, max_length=200, default='MR')
    terms= models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

class ContentRequestModel(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    type_here_the_type_of_content_you_want = models.TextField()

    def __str__(self):
        return self.full_name

