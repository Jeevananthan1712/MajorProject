# import csv
# #
# import matplotlib.pyplot as plt
# # %matplotlib inline
# import numpy as pd
# labels='1','2','3'
# sizes=[]
# sizep=[]
# sizer=[]
#
# explode=(0.1,0.1,0.1)
# with open('MoneyData.csv', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#
#     for row in plots:
#         sizes.append(row[0])
#         sizep.append(row[2])
#         sizer.append(row[3])
# plt.pie(sizes,explode=explode,labels=labels,
#        autopct='%0.1f%%',shadow=True)
# plt.show()
#








# import csv
#
# import matplotlib.pyplot as plt
# # %matplotlib inline
# import numpy as pd
# x=[]
# y=[]
# z=[]
#
# with open('Data.csv', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#
#     for row in plots:
#         x.append(row[1])
#         y.append(row[0])
# plt.bar(x,y)
# # plt.show()
#
#
#
#
#
#

# df=sbn.load_dataset("Data")
# pairplot with the hue = gender parameter
# sbn.pairplot( data, hue='category')
# sbn.boxplot(x='category', y='amount', data=dataset)
# displaying the plot

# #

import matplotlib.pyplot as plt
import csv
import pandas as pd

x = []
y = []
dataset = pd.read_csv('Data.csv')
data = dataset.copy()
d = data.head(25)

with open('Data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    print(csvfile)
    for row in plots:
        print(row[1])
        x.append(row[1])
        y.append(row[0])
# print(x)
# plt.plot(x, y, color='g', label="Category Wise Data")
plt.scatter(x, y, color = 'g',s = 100)
plt.xticks(rotation = 0)
plt.xlabel('Category')
plt.ylabel('Money')
# plt.title('Ages of different persons')
plt.legend()
plt.show()
# # #
# # # # # import matplotlib.pyplot as plt
# # # # # import csv
# # # # #
# # # # # Subjects = []
# # # # # Scores = []
# # # # #
# # # # # with open('SubjectMarks.csv', 'r') as csvfile:
# # # # #     lines = csv.reader(csvfile, delimiter=',')
# # # # #     for row in lines:
# # # # #         Subjects.append(row[0])
# # # # #         Scores.append(int(row[1]))
# # # # #
# # # # # plt.pie(Scores, labels=Subjects, autopct='%.2f%%')
# # # # # plt.title('Marks of a Student', fontsize=20)
# # # # # plt.show()