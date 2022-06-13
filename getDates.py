import pandas as pd
from pprint import pprint
from sys import platform
import datetime
import csv
import sys

class Course:
    def __init__(self, name, section, instructor, start_date, end_date, start_time, end_time, location, meeting_patterns,days):
        self.name = name
        self.section = section
        self.instructor = instructor
        self.start_date = start_date.strip()
        self.end_date = end_date.strip()
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.meeting_patterns = meeting_patterns
        
        self.days = days

    def __repr__(self) -> str:
        return self.name
    
    def detailed(self):
        return self.__dict__

def getDayName(day):
    dayMap = {"M":"Monday","T":"Tuesday","W":"Wednesday","R":"Thursday","F":"Friday","S":"Saturday","U":"Sunday"}
    return dayMap.get(day.rstrip())

#gets the day of the week from a date
def getDayFromDate(date):
    return pd.Timestamp(date).day_name()



def main():
    csv_titles = ["Subject","Description","Start Time","End Time","Location","Start Date","End Date"] #csv headers
    if platform == "win32":
        filename = 'uploads\View_My_Courses.xlsx'
    else:
        filename = 'uploads/View_My_Courses.xlsx'
    excel = pd.read_excel(filename)
    if platform == "win32":
        excel.to_csv("downloads\classes.csv", index=None, header=True)
        df = pd.DataFrame(pd.read_csv("downloads\classes.csv"))
    else:
        excel.to_csv("downloads/classes.csv", index=None, header=True)
        df = pd.DataFrame(pd.read_csv("downloads/classes.csv"))
    titles = list(df.iloc[1])[1:]
    class_row = []
    for index, row in df.iterrows():
        if index < 2:
            continue
        if row[2]:
            class_row.append(list(row[1:]))
    classes = []

    for row in class_row:
        for i in range(len(row)):
            print(f"row[{i}]: {row[i]}")
        name = row[0]
        section = row[3]
        try:
            meeting_patterns = row[6]
            location = row[6].split("|")[2]
            start_time = row[6].split("|")[1].split("-")[0]
            end_time = row[6].split("|")[1].split("-")[1]
            days = [getDayName(x) for x in " ".join(row[6].split("|")[0]).strip().split(" - ")]
        except:
            meeting_patterns = "TBD"
            location = "TBD"
            start_time = "TBD"
            end_time = "TBD"
            days = []
        instructor = row[8]
        start_date = row[9].strip().split(" ")[0]
        end_date = row[10].strip().split(" ")[0]
        classes.append(Course(name, section, instructor, start_date, end_date, start_time, end_time, location, meeting_patterns, days)) #create a class object with the attributes read from the workday file

    rows_to_write = []
    for c in classes:
        start_date = datetime.date(int(c.start_date.split("-")[0]),int(c.start_date.split("-")[1]),int(c.start_date.split("-")[2]))#gets the start day of each course
        date_iter = start_date #creates a variable to iterate through dates
        end_date = datetime.date(int(c.end_date.split("-")[0]),int(c.end_date.split("-")[1]),int(c.end_date.split("-")[2]))#gets the end day of each course
        delta = datetime.timedelta(days=1)#increments the date by one day
        while date_iter <= end_date:
            if(getDayFromDate(date_iter) in c.days):#if the day of the week is in the days of the course ex. M,T,W,R,F
                row = f'{c},{c.section},{c.start_time},{c.end_time},{c.location}' #get the row to write to the csv
                print(row)
                rows_to_write.append([c.name,c.section,c.start_time,c.end_time,c.location,date_iter,date_iter])#add the row to the list of rows to write
            date_iter += delta


    #write the rows to the csv
    if platform == "win32":
        with open('downloads\classes.csv', 'w+') as csvfile:
            writer = csv.writer(csvfile,delimiter=',')
            writer.writerows([csv_titles]+ rows_to_write)
    else:
        with open('downloads/classes.csv', 'w+') as csvfile:
            writer = csv.writer(csvfile,delimiter=',')
            writer.writerows([csv_titles]+ rows_to_write)

if __name__ == "__main__":
    main()