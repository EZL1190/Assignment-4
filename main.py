import sys
import tasks
import webget
import csv_data_conversion as cdc

if __name__ == '__main__':
    _, url = sys.argv

file_name = webget.download(url)
data = cdc.get_data_set(file_name)

#print(tasks.task1(data))
#print(tasks.task2(data))
#print(tasks.task3(data))
#print(tasks.task4(data))
#print(tasks.task5(data))
#tasks.plot1(data)
#tasks.plot2(data)
tasks.plot3(data)
