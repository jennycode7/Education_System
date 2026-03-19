from django.core.management.base import BaseCommand
from faker import Faker
from ...models import LGA, School, Student
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed database"

    def handle(self, *args, **kwargs):

        lgas = []
        schools = []

        # Create LGAs
        for _ in range(10):
            lga = LGA.objects.create(
                name=fake.city(),
                state=fake.state()

            )
            lgas.append(lga)

        # Create Schools linked to LGAs
        for _ in range(30):
            school = School.objects.create(
                name=fake.company() + " Secondary School",
                lga=random.choice(lgas)
            )
            schools.append(school)

        # Create Students linked to Schools
        for _ in range(1000):
            Student.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                other_names=fake.first_name(),
                school=random.choice(schools),
                year = random.randint(2005, 2025),
                current_class=random.choice(["Class 5", "Class 4", "Class 3"])
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))