from faker import Faker
from django.core.management.base import BaseCommand
from ...models import Student, Exams
import random

fake = Faker()


class Command(BaseCommand):
    help = "Seed Database"

    def handle(self, *args, **options):
        students = Student.objects.all()[:10]

        subjects = ["English", "Mathematics", "World History"]
        years = [2020, 2021, 2022, 2023, 2024, 2025]
        exam_types = ['WAEC', 'NECO']

        created_count = 0

        for student in students:

            # ✅ pick ONE year per student
            year = random.choice(years)
            exam_type = random.choice(exam_types)

            for subject in subjects:

                # ✅ prevent duplicates
                if Exams.objects.filter(
                    student=student,
                    subject=subject,
                    year=year,
                    exam_type=exam_type

                ).exists():
                    continue

                score = random.choice([
                    round(random.uniform(40, 100), 2),
                    None
                ])

                Exams.objects.create(
                    student=student,
                    subject=subject,
                    score=score,
                    year=year,
                    exam_type=exam_type
                )

                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"✅ Seeded {created_count} records")
        )