import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user story', 'acceptance criteria', 'business value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    return []


def get_elements_csv(file_csv):
    temp_lst = []
    with open(file_csv) as file:
        for line in file:
            temp_lst.append(line.split(";"))
        return temp_lst


def add_element_csv(file, element):
    temp = get_elements_csv(file)
    temp.append(';'.join(element))
    with open(file, "w")as file:
        for row in temp:
            file.write(row)
