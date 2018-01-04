from csv import reader
import matplotlib.pyplot as plt

#Function to import csv file and make put the data into dataset list
def read_file(filename):
    dataset = list()
    with open(filename,'r') as file:
        csv_reader = reader(file)
        
        for row in csv_reader:
            dataset.append(row)

    return dataset

# Converting string into float cause we cannot do arithmetic operations on string
def str_to_float(dataset):
    for row in dataset:
        for i in range(len(row)):
            row[i] = float(row[i])

# Finding out maximum and minimum from dataset for the normalizatoin
def minmax(dataset):
    minmax = list()
    _min = min(dataset[0])
    _max = max(dataset[0])
    minmax.append([_min,_max])
    return minmax

# Normalizing the data to build a better model
def normalize(dataset,minmax):
    
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[0]) / (minmax[1] - minmax[0])

# Prediction Function
def predict(x,coef):
    y = coef[0] + coef[1] * x
    return y

# Optmization Function to find the best coeffiecient
def find_coef(dataset,l_rate,epoch):
    coef = [0.0 for i in range(len(dataset[0]))]
    for i in range(epoch):
        for row in dataset:
            y = predict(row[0],coef)
            error = y - row[1]
            coef[0] = coef[0] - error * l_rate
            for i in range(len(row) - 1):
                coef[i+1] = coef[i+1] - error * l_rate  * row[i]

    return coef

# Plotting  on graph to visualize everything
def plot_on_graph(dataset,predicted):
    #Plotting on the graph
    fig, ax = plt.subplots()
    
    for row in dataset:
        ax.plot(row[0],row[1],marker='o', markersize=3, color="red")

    for row in predicted:
        ax.plot(row[0],row[1],marker='o',color="black")
    ax.grid(True, which='both')
    ax.set_aspect('equal')
    ax.set_xlabel("Prices per SQ/Ft")
    ax.set_ylabel("Size of the house")
    plt.show()

# Learning Rate
l_rate =0.01
# Number of Iteration
epoch = 50
# Temporary Dataset cause we just need two colums from this dataset
tmp_dataset = read_file('RealEstate.csv')
dataset = list() #Dataset as list
for row in tmp_dataset: 
    dataset.append([row[5], row[6]]) #Taking row 5 and 6 into the database

dataset.pop(0) # Popping out the first row cause it's justlabel

str_to_float(dataset) 
minmax = minmax(dataset)
normalize(dataset,minmax[0])
coef = find_coef(dataset,l_rate,epoch)
predicted = list() # Declaring predicted as a list
for row in dataset:
    predicted.append([row[0],predict(row[0],coef)]) #Predicting the values
plot_on_graph(dataset,predicted) # Plotting graphs to visualize




