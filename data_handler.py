import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_elements_csv():
    temp_lst = []
    with open(DATA_FILE_PATH) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dictionary = {key: value for key, value in zip(DATA_HEADER, row)}
            temp_lst.append(dictionary)
        return temp_lst


def add_element_csv(row):
    with open(DATA_FILE_PATH, 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(row)


def get_id():
    return len(get_elements_csv())
