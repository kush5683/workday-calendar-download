import pandas as pd
from rich import print



def clean(filepath):
    excel = pd.read_excel(filepath)
    c = excel.to_csv(index=None, header=True)
    headers = ['Info', 'Course Listing', 'Credits', 'Grading Basis', 'Section', 'Instructional Format', 'Delivery Mode',
               'Meeting Patterns', 'Registration Status', 'Instructor', 'Start Date', 'End Date']
    rows_to_write = []
    for row in c.split('\n'):
        cols = row.split(',')
        try:
            if cols[8] == "Registered" and cols[3] == "Graded":
                rows_to_write.append(row)
        except IndexError as Ignore:
            pass
    for row in rows_to_write:
        print(row)
        print("\n")
    with open('temp.csv', 'w+') as f:
        f.write(','.join(headers))
        f.write('\n')
        for row in rows_to_write:
            f.write(row)
            # f.write('\n')
    csv_to_excel = pd.read_csv('temp.csv')
    csv_to_excel.to_excel('temp.xlsx', index=None, header=True)


if __name__ == '__main__':
    clean('View_My_Courses.xlsx')
