import pandas as pd
import os

data = pd.read_csv('acronyms.csv')

read = input("Enter the Correct Acronym: ") 
i = 0
run = True
while run:
    if i <= 50:
        if read == data.acronym[i]:
            print("The Defination is: ",data.defination[i])
        i += 1
    else:
        run = False