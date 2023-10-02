#-------------------------------------------------------------------------
# AUTHOR: Cameron Ross
# FILENAME: naive_bayes.py
# SPECIFICATION: Answer to question 5b on Assignment 2
# FOR: CS 4210- Assignment #2
# TIME SPENT: 30 min
#-----------------------------------------------------------*/

# These two functions are used to make a nice looking output
def pad_word(word, length):
    word = str(word)
    if len(word) < length:
        padded_word = word + ' ' * (length - len(word))
        return padded_word
    else:
        return word
    
def print_row(c1,c2,c3,c4,c5,c6,c7):
    print(f'{pad_word(c1, 3)}   {pad_word(c2, 8)}   {pad_word(c3, 11)}   {pad_word(c4, 8)}   {pad_word(c5, 6)}   {pad_word(c6, 10)}   {pad_word(c7, 10)}')
   

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard dictionaries, lists, and arrays
#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

db = []
X = []
Y = []
# reading the data in the training csv file
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: db.append(row)
            
# For each row in db...
    # Map attrributes to numeric values and store in x 
    # Map classes to numeric values and store in y
for record in db:
    list = []
    # Outlook  
    if record[1] == 'Sunny': list.append(1)
    elif record[1] == 'Overcast': list.append(2)
    else: list.append(3)
    # Temp  
    if record[2] == 'Cool': list.append(1)
    elif record[2] == 'Hot': list.append(2)
    else: list.append(3)
    # Humidity  
    list.append(1 if record[3] == 'High' else 2)
    # Wind  
    list.append(1 if record[4] == 'Weak' else 2)
    # Append
    X.append(list)
    Y.append(1 if record[5] == 'No' else 2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the data in the test csv file
db_test = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: db_test.append(row)

# printing the header
print_row("Day", "Outlook", "Temperature", "Humidity", "Wind", "PlayTennis", "Confidence")
print("--------------------------------------------------------------------------")

# For each row in db_test...
    # Map attrributes to numeric values and make a prediction
for record in db_test:
    list = []
    # Outlook  
    if record[1] == 'Sunny': list.append(1)
    elif record[1] == 'Overcast': list.append(2)
    else: list.append(3)
    # Temp  
    if record[2] == 'Cool': list.append(1)
    elif record[2] == 'Hot': list.append(2)
    else: list.append(3)
    # Humidity  
    list.append(1 if record[3] == 'High' else 2)
    # Wind  
    list.append(1 if record[4] == 'Weak' else 2)
    # Make the prediction
    confidence = clf.predict_proba([list])[0]
    prediction = 'No' if confidence[0] > confidence[1] else 'Yes'
    prob = confidence[0] if confidence[0] > confidence[1] else confidence[1]
    prob = round(prob, 2)
    # Print result
    print_row(record[0], record[1], record[2], record[3], record[4], prediction, prob)
