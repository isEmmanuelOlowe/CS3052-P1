import sys
import math
from modules.quickSelect import QuickSelect
from modules.cp3 import ClosestPoints


'''
The main method of the program
'''


def Main():
    #processes the data
    data = processData()
    #checks if the data has been correctly formatted
    if data == []:
        print("Incorrectly formatted input")
    else:
        data.sort()
        #Generates the closests points
        distance = ClosestPoints(data)[0][0]
        if distance == 0:
            print("0")
        else:
            #Formatting the distance into the correct format
            significant_digits = 9
            ##Presenting the number to 9 SF
            rounded_distnace = round(
                distance, significant_digits - int(math.floor(math.log10(abs(distance)))) - 1)
            if rounded_distnace > 99999999:
                rounded_distnace = int(rounded_distnace)
            print(rounded_distnace)


'''
This method process the incoming data converts it to a 2D array

@return 2D array of given data or [] if error
'''


def processData():
    #Checks if we are the top of the file
    head = True
    #the length of the file
    length = 0
    #stores the data
    data = []
    try:
        #loops over everline of the file.
        for line in sys.stdin:
            #checks if we are at the top of the file
            if head == True:
                length = int(line)
                #checks the length of the file is valid
                if length < 2:
                    raise Exception
                head = False
            else:
                #splits new line and formats the numbers
                newLine = line.strip("\n")
                items = newLine.split()
                if len(items) != 2:
                    raise Exception
                else:
                    data.append([float(items[0]), float(items[1])])
        #in the event the file is empty
        if length == 0:
            raise Exception
        #in event error in the length and size of the data
        if length != len(data):
            raise Exception
        #returns formatted data
        return data
    except:
        #returns [] if an exception has been generated.
        return []


if __name__ == "__main__":
    Main()
