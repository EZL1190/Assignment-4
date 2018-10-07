import sys
import tasks
import webget
import csv_data_conversion as cdc

# url = 'https://raw.githubusercontent.com/MikkelHansen95/dataset/master/movies_metadata.csv'
if __name__ == '__main__':
    _, url = sys.argv

file_name = webget.download(url)
data = cdc.get_data_set(file_name)

print('\nMovies rated adult: ' + str(tasks.task1(data)))
print('\nMovies listed as "Animation": ' + str(tasks.task2(data)))
task3 = tasks.task3(data)
print('\n"' + task3['title'] + '" has the highest budget: ' + str(task3['budget']))
task4 = tasks.task4(data)
print('\n"' + task4['title'] + '" is the most popular danish movie with a popularity of: ' + str(task4['popularity']))
task5 = tasks.task5(data)
print('\n"' + task5['title'] + '" is the english movie with the biggest revenue: ' + str(task5['revenue']))
tasks.plot1(data)
tasks.plot2(data)
tasks.plot3(data)
