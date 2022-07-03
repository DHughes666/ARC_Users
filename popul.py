import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Albion.settings') 

import django
django.setup()

from faker import Faker
from AP.models import User

fakegen = Faker()

def createUsers(N=5):
    for entry in range(N):
        fakeName = fakegen.name().split() 
        first_Name = fakeName[0]  
        last_Name = fakeName[1]
        email = fakegen.email()
        usee = User.objects.get_or_create(first_Name=first_Name, last_Name=last_Name, email=email)[0]
if __name__ == '__main__':
    print('Populating fields')
    createUsers(20)
    print('Done!')