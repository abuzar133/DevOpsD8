import csv

#read csv file
#csv(comma seperated value) is simple file format used to store tabular dta such as spreadsheets
with open("example.csv",'r')as file:
    csv_reader = csv.reader(file) #generates areader object [iterator]
    header = next(csv_reader) # (retutns the next row of the resderd itersble object as a list# )
    for i in csv_reader: #iterating through the reader object for thr remaning rows
        print(i)


#write a csv file
data = [
    ['name','age','city'],
    ['jhondoe','46','chicago'],
    ['jane doe','46','newyork'],
    ['tom doe','47','los angeles']
]

with open("data.csv",'w')as file:
    csv_writer = csv.writer(file) #generates a writer object [iterator]
    for row in data: #iterating through data list
        csv_writer.writerow(row) #write each row to the csv file