#-------------------------------------------------------------------------
# AUTHOR: Cameron Ross
# FILENAME: decision_tree_2.py
# SPECIFICATION: Answer to question 2 on Assignment 2
# FOR: CS 4210- Assignment #2
# TIME SPENT: 30 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
for ds in dataSets:
    dbTraining = []
    X = []
    Y = []
    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            # Skip header
            if i > 0: dbTraining.append(row)

    # For each row in db_training...
        # Map attrributes to numeric values and store in x 
        # Map classes to numeric values and store in y
    for record in dbTraining:
        list = []
        # Age  
        if record[0] == 'Young': list.append(1)
        elif record[0] == 'Presbyopic': list.append(2)
        else: list.append(3)
        # Prescription  
        list.append(1 if record[1] == 'Hypermetrope' else 2)
        # Astigmatism  
        list.append(1 if record[2] == 'No' else 2)
        # Tears  
        list.append(1 if record[3] == 'Normal' else 2)
        # Append
        X.append(list)
        Y.append(1 if record[4] == 'No' else 2)

    predictions = 0
    correct = 0 
    # Loop your training and test tasks 10 times here
    for i in range (10):
        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                # Skip header
                if i > 0: dbTest.append(row)

        # Map the test data to numbers and get the prediction
        for record in dbTest:
            list = []
            # Age  
            if record[0] == 'Young': list.append(1)
            elif record[0] == 'Presbyopic': list.append(2)
            else: list.append(3)
            # Prescription  
            list.append(1 if record[1] == 'Hypermetrope' else 2)
            # Astigmatism  
            list.append(1 if record[2] == 'No' else 2)
            # Tears  
            list.append(1 if record[3] == 'Normal' else 2)
            # Actual value
            actual_class = 1 if record[4] == 'No' else 2
            # Make the prediction with the tree
            predicted_class = clf.predict([list])[0]
            # Add to accuracy prediction
            predictions = predictions + 1
            correct = correct + (1 if actual_class == predicted_class else 0)

    # Find the average accuracy of this model during the 10 runs (training and test set)
    # Accuracy = (# Correct) / (# Predictions)
    accuracy = correct / predictions
    print(f"final accuracy when training on {ds}: {accuracy}")
