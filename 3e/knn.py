#-------------------------------------------------------------------------
# AUTHOR: Cameron Ross
# FILENAME: knn.py
# SPECIFICATION: Answer to question 3e on Assignment 2
# FOR: CS 4210- Assignment #2
# TIME SPENT: 25 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays
#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        #skipping the header
        if i > 0: db.append (row)

# Perform the prediction on each point
predictions = 0
wrong = 0 
for i in range(len(db)):

    # For each row in db...
        # Map attrributes to numeric values and store in x 
        # Map classes to numeric values and store in y
        # Ignore recrd[i], and put it in testSample
    testSample = []
    testSampleClass = -1
    X = []
    Y = []
    for j in range(len(db)):
        record = db[j]
        if j == i: 
            testSample = [float(record[0]), float(record[1])]
            testSampleClass = record[2]
        else:
            X.append([ float(record[0]), float(record[1]) ])
            Y.append(record[2])
   
    # Fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=3, p=2)
    clf = clf.fit(X, Y)
    # Make the prediction
    predicted_class = clf.predict([testSample])[0]
    predictions = predictions + 1
    # See if we are correct
    wrong = wrong + (1 if testSampleClass != predicted_class else 0)

# Error = (# Wrong) / (# Predictions)
error = wrong / predictions
print(f'Error rate: {error}')






