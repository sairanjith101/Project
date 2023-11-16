import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student.settings')

import django
django.setup()

from studentApp.models import *
from faker import Faker
from random import *
faker = Faker()

def generate(n):
    for i in range(n):
        fSno = randint(1113,1200)
        fSname = faker.name()
        fSclass = randint(1,12)
        fSaddress = faker.city()
        record = Student.objects.get_or_create(Sno = fSno, Sname = fSname, Sclass = fSclass,
        Saddress = fSaddress)

generate(48)