import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def read_elements_csv():
    temp_lst = []
    with open(DATA_FILE_PATH) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dictionary = {key: value for key, value in zip(DATA_HEADER, row)}
            temp_lst.append(dictionary)
        return temp_lst


def add_element_csv(row, index=len(read_elements_csv())):
    temp_lst = insert_element_csv(row, index)

    with open(DATA_FILE_PATH, 'w') as file:
        csv_writer = csv.writer(file)
        for line in temp_lst:
            csv_writer.writerow(line.values())


def insert_element_csv(row, index):
    temp_lst = read_elements_csv()
    zip_row = zip(temp_lst[0].keys(), row)
    dict_row = dict((key, value) for key, value in zip_row)
    temp_lst[index] = dict_row
    return temp_lst


def get_id():
    return len(read_elements_csv())


def get_element_by_id(user_id):
    for elt in read_elements_csv():
        if elt['id'] == str(user_id):
            # print(elt)
            return elt
