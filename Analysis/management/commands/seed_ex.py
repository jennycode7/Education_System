from faker import Faker
from django.core.management.base import BaseCommand
from ...models import Student, Exams
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed DataBase"

    def handle(self, *args, **options):
        students = Student.objects.all()

        common_subjects = ['English', 'Mathematics', 'World History']
        years = [2020, 2021, 2022, 2023, 2024, 2025]



        for student in students:

            for year in years:
                for subject in common_subjects:

                    score = random.choice([
                        round(random.uniform(40, 100), 2), 
                        None
                    ])

                    Exams.objects.create(
                        student=student,
                        subject=subject,
                        score=score,
                        year=year
                    ) 
        



        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))