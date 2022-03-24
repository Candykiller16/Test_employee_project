import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_employee_project.settings')
django.setup()

from django_seed import Seed
from employee.models import EmployeeMPTT, User

number_of_employee = int(input('Number of employees to add: '))

seeder = Seed.seeder()
seeder.add_entity(User, number_of_employee)
seeder.add_entity(EmployeeMPTT, number_of_employee,
                  {
                      'first_last_patro_name': lambda x: seeder.faker.name(),
                      'level': lambda x: random.randint(0, 4)
                  })

seeder.execute()
