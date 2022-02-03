# S algoritms

import csv

# # Read file:
# load te csv file and assign each row to a data frame
# also print the row to see the dataset (optional)


a = []
with open("finds.csv", "r") as csfile:
    reader = csv.reader(csfile)
    for row in reader:
        a.append(row)
        print(row)
num_attrubute = len(a[0]) - 1
#
#
# # 1. The most general hypothesis is represented by:
# #        '''['?', '?', '?', '?', '?', '?']'''
# # 2.  The most specific hypothesis is represented by:
# #          '''['0', '0', '0', '0', '0', '0']'''

hypothesis = a[0][:-1]
print(hypothesis)
print("a length", len(a))
print(num_attrubute)
print(a[0][num_attrubute])
print("\n Find S: Finding a maximally specific hypothesis")
for i in range(len(a)):
    if a[i][num_attrubute] == "yes":
        for j in range(num_attrubute):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
    print("The taining example no:", i + 1, " the hypothesis is:", hypothesis)
print("\n The maximally specific hypothesis for training set is")
print(hypothesis)


