#Task 1 -> Merge three input csv files and produce a sorted (by stock (A-Z)) to new file: merged.csv
#Task 2 -> Merge three input csv files and identify 15 companies with highest "MarketCap" sorted (largest to smallest) to new file: marketcap.csv 
#Task 3 -> Provide stock symbol functionality. User should be able to search for stock by symbol and if it exists, display values, otherwise display "Not found"
####### -> This needs to be run from command line


#Thoughts -> Data Structure: dictionary (key-> value), binary tree
######### -> Dictionary: O(1) searching, O(1) inserting, O(n) merging dictionaries together 

###NEED TO DO: Sort merged files, identify highest 15 "Marketcap" and create new csv files for each 

import csv #used for writing a new csv file
import sys as s #used to read user input from command line 


#Main data structures & variables
stock_dict = {}

print("Arguments: ", len(s.argv))
print("Argument List: ", str(s.argv))


def readCSV(filename):

    file = open(filename)
    csv_reader = csv.reader(file)
    #header = next(csv_reader)
    
    for row in csv_reader:
        symbol = row[0] #key value for stocks for constant lookup 

        if symbol not in stock_dict:
            stock_dict[symbol] = row #Split remainder of row since index 0 is symbol and that is now key 

    file.close()

def findStock():

    errormessage = "Not found."

    if len(s.argv):
        userinput = str(s.argv[1])

        if userinput in stock_dict:
            print(stock_dict[userinput])
        else:
            print(errormessage)


if __name__ == "__main__":

    for i in range(1, 4):
        filename = 'companylist-' + str(i) + '.csv'
        readCSV(filename)

    findStock()