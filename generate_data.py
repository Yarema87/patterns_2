import csv
from faker import Faker
import random

fake = Faker()

CSV_FILE = 'generated_data.csv'

NUM_ROWS = 1000


def generate_csv():
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'employee_name', 'employee_contacts', 'employee_department',
            'mentor_name', 'mentor_contacts', 'mentor_department', 'mentee_id',
            'task_title', 'task_description', 'task_deadline', 'task_assigned_to',
            'feedback_text', 'feedback_author', 'feedback_time_submission',
            'training_title',
            'equipment_type', 'equipment_assigned_to',
            'hr_name', 'hr_contacts',
            'it_contacts'
        ])

        for i in range(NUM_ROWS):
            employee_department = fake.job()

            writer.writerow([
                fake.name(), fake.email(), employee_department,
                fake.name(), fake.email(), employee_department, i,
                fake.sentence(nb_words=4), fake.paragraph(nb_sentences=2), fake.future_date(), random.randint(1, 1000),
                fake.sentence(), random.randint(1, 1000), fake.date_time_this_year().isoformat(),
                fake.bs().title(),
                fake.random_element(elements=['Laptop', 'Monitor', 'Keyboard']), random.randint(1, 1000),
                fake.name(), fake.email(),
                fake.email()
            ])


if __name__ == '__main__':
    generate_csv()
    print(f"Згенеровано {NUM_ROWS} рядків у файлі {CSV_FILE}")
