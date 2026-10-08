import os
import random
from django.conf import settings
from django.core.management.base import BaseCommand
from employees.models import Employee, Position, Department, Status


class Command(BaseCommand):
    help = "Seeds database with mock Positions, Departments, and 10 Employees matching actual models"

    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing existing data...")
        Employee.objects.all().delete()
        Department.objects.all().delete()
        Position.objects.all().delete()

        # 1. Ensure local image directory and dummy image files exist
        image_dir = os.path.join(settings.LOCAL_FILE_DIR, "images")
        os.makedirs(image_dir, exist_ok=True)

        sample_images = ["avatar1.jpg", "avatar2.jpg", "avatar3.jpg"]
        for img in sample_images:
            img_path = os.path.join(image_dir, img)
            if not os.path.exists(img_path):
                with open(img_path, "w") as f:
                    f.write("dummy image content")

        # 2. Seed Positions
        positions_data = [
            ("Frontend Developer", 85000.00),
            ("Backend Developer", 90000.00),
            ("DevOps Engineer", 95000.00),
            ("HR Specialist", 60000.00),
            ("Engineering Manager", 120000.00),
        ]
        positions = [
            Position.objects.create(name=name, salary=salary)
            for name, salary in positions_data
        ]

        # 3. Seed Managers (Employees who don't have a manager initially)
        manager1 = Employee.objects.create(
            name="Alex Rivera",
            address="101 Tech Way",
            image=os.path.join(image_dir, "avatar1.jpg"),
            status=Status.NORMAL,
        )
        manager2 = Employee.objects.create(
            name="Sarah Connor",
            address="202 Corporate Blvd",
            image=os.path.join(image_dir, "avatar2.jpg"),
            status=Status.NORMAL,
        )

        # 4. Seed Departments (OneToOneField with Manager)
        dept_eng = Department.objects.create(name="Engineering", manager=manager1)
        dept_hr = Department.objects.create(name="Human Resources", manager=manager2)
        Department.objects.create(name="Marketing", manager=None)

        # 5. Seed Remaining 8 Employees with assigned managers
        sample_names = [
            "John Doe", "Emma Watson", "Michael Brown", "Sophia Martinez",
            "David Wilson", "Olivia Taylor", "James Anderson", "Isabella Thomas"
        ]

        statuses = [
            Status.RECRUITMENT_PROCESS,
            Status.WAITING_ONBOARDING,
            Status.PROBATION,
            Status.NORMAL,
            Status.RESIGNED,
        ]

        for i, name in enumerate(sample_names):
            Employee.objects.create(
                name=name,
                address=f"{100 + i * 10} Main St, Suite {i + 1}",
                manager=random.choice([manager1, manager2]),
                image=os.path.join(image_dir, random.choice(sample_images)),
                status=random.choice(statuses),
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully seeded 10 employees, positions, and departments!")
        )