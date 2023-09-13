from tkinter import *
import sqlite3
import random


def getAnimal(query):
    # connect to DB
    conn = sqlite3.connect('model/AnimalList.db')

    # create cursor for intacting with DB
    cursor = conn.cursor()

    # get random record and retrieve animal name from said record
    animalRecord = cursor.execute(query)
    animal = animalRecord.fetchone()[0]
    print(animal)

    # commit the transaction
    conn.commit()

    # close the cursor
    conn.close()

    return animal
# END getAnimal function

"""
1) checks to see if animal is already in list, if so, it
    empties 'animal' variable then returns control back to 
    buildAnimalList() function for further querying
2) LCV is updated along depending on whether a duplicate exists
"""
def animalDuplicateCheck(lcv, animal, list):
    # for-loop for running through list for duplicates
    for duplicate in list:
        # if duplicate, empty variable: 'animal' & redo iteration by decrementing LCV
        if animal == duplicate:
            animal = ''
            lcv -= 1
        # else, print news to console
        else:
            print("NO duplicate to " + animal)

    # if variable 'animal' is not empty after checking for duplicates, append it to the list
    if animal != '':    
        list.append(animal)
        print(animal + " added to list at iteration: " + str(lcv))
        lcv += 1

    # Return LCV for while loop in buildAnimalList() function 
    return lcv
# END animalDuplicateCheck function

# builds the animal list for thew GUI app
def buildAnimalList(param):
    
    # variables for creating animal list for GUI app
    animalList = []
    queriedAnimal = ''

    # a loop that uses queries to pick random animals from the DB to build the animal list
    i=1
    while i <= param:
        
        # gets a random number for the choosing of an animal
        intCls = random.randint(1,5)

        #match/case for choosing an animal table
        match intCls:            
            
            case 1:
                query = "SELECT * FROM Amphibian ORDER BY RANDOM() LIMIT 1;"
                queriedAnimal = getAnimal(query)
                i = animalDuplicateCheck(i, queriedAnimal, animalList) # loop control variable
                        
            case 2:
                query = "SELECT * FROM Bird ORDER BY RANDOM() LIMIT 1;"
                queriedAnimal = getAnimal(query)
                i = animalDuplicateCheck(i, queriedAnimal, animalList) # loop control variable
                    
            case 3: 
                query = "SELECT * FROM Fish ORDER BY RANDOM() LIMIT 1;"
                queriedAnimal = getAnimal(query)
                i = animalDuplicateCheck(i, queriedAnimal, animalList) # loop control variable
                
            case 4:
                query = "SELECT * FROM Mammal ORDER BY RANDOM() LIMIT 1;"
                queriedAnimal = getAnimal(query)
                i = animalDuplicateCheck(i, queriedAnimal, animalList) # loop control variable
                        
            case 5:
                query = "SELECT * FROM Reptile ORDER BY RANDOM() LIMIT 1;"
                queriedAnimal = getAnimal(query)
                i = animalDuplicateCheck(i, queriedAnimal, animalList) # loop control variable

    # prints to console the end of the iteration
    print("---------------- End of Iterations ----------------")

    # END while-loop

    # combines animal list into one long string of animals
    animalStr = '/'.join(animalList)
    return animalStr
# END buildAnimalList function
