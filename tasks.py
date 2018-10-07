import matplotlib.pyplot as plt
import collections as col
import operator
from mpl_toolkits.mplot3d import Axes3D
import random

def task1(data):
    counter = 0;
    for row in data:
        if row['adult'] == 'True':
            counter += 1
    return counter

def task2(data):
    counter = 0
    for row in data:
        for row2 in row['genres']:
            if row2['name'] == 'Animation':
                counter += 1
    return counter

def task3(data):
    movie = {'budget' : 0, 'title': ''}
    for row in data:
        if row['budget'] > movie['budget']:
            movie['budget'] = row['budget']
            movie['title'] = row['original_title']
    return movie

def task4(data):
    movie = {'popularity' : 0, 'title': ''}
    for row in data:
        if len(row['production_countries']) > 0:
            for row2 in row['production_countries']:
                if row2['name'] == 'Denmark' and row['popularity'] > 0:
                    movie['title'] = row['original_title']
                    movie['popularity'] = row['popularity']

    return movie

def task5(data):
    movie = {'revenue': 0, 'title': ''}
    for row in data:
        for row2 in row['genres']:
            if len(row2) > 0:
                if row2['name'] == 'Action' and row['original_language'] == 'en' and row['revenue'] > movie['revenue']:
                    movie['revenue'] = row['revenue']
                    movie['title'] = row['original_title']
    return movie

def plot1(data):
#    idk = {}
#    for row in data:
#        date = row['release_date']
#        idk.setdefault(date[5:], 0)
#        idk[date[5:]] += 1

    date_array = []
    for row in data[:50]: #Vi bruger 50 i stedet for alle, for at gøre det læsligt
        date = row['release_date']
        if date != '': 
            date_array.append(date[5:])

    c = col.Counter()
    release_date_array = c.update(date_array)
    
    counterlist =  []
    for key in sorted(c.items()):
        counterlist.append([key])

    final_data = {}
    for row in counterlist:
        for row2 in row:
            final_data.setdefault(row2[0], row2[1])

    

    plt.cla()
    plt.bar(final_data.keys(), final_data.values(), width=0.5, linewidth=0, align='center')
    #plt.ticklabel_format(useOffset=False)
    plt.axis([0, len(final_data), 0, max(final_data.values())])
    plt.title('Number of movies according to release day', fontsize=12)
    plt.xlabel("MM/DD", fontsize=10)
    plt.ylabel("Number of movies", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    print(final_data)
    plt.show()

def plot2(data):
    final_date = {}
    for row in data[:50]:
        final_date.setdefault(row['runtime'], 0)
        final_date[row['runtime']] += 1
    


    x_values = final_date.keys()
    y_values = final_date.values()
    plt.title('Scatter-Plot with runtime', fontsize=12)
    plt.xlabel("Runtime", fontsize=10)
    plt.ylabel("MM/DD", fontsize=10)
    plt.scatter(x_values, y_values, s=100)
    plt.show()

def plot3(data):
    buzzword = {}
    for row in data:
        words_list = row['overview'].split(" ")
        for word in words_list:
            buzzword.setdefault(word, 0)
            buzzword[word] += 1
    buzzword_sorted = list(sorted(buzzword.values()))[-100:]
    #sorted_d[-100:] last 100

    revenue = []
    for row in data:
        rev = row['revenue']
        if rev != '' and rev != 0: 
            revenue.append(rev)

    budget = []
    for row in data:
        bud = row['budget']
        if bud != '' and bud != 0: 
            budget.append(bud)


    fig = plt.figure()
    ax = Axes3D(fig)

    plt.title('3D Scatter-Plot', fontsize=12)
    ax.set_xlabel('Revenue')
    ax.set_ylabel('Budget')
    ax.set_zlabel('Buzzword')
    ax.set_xlim3d(0, max(revenue[:100]))
    ax.set_ylim3d(0, max(budget[:100]))
    ax.set_zlim3d(0, max(buzzword_sorted))
    ax.scatter(revenue[:100], budget[:100], buzzword_sorted)
    plt.show()

    