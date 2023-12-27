import pandas as pd
import os

num_rows = 125
data = pd.read_csv('acronyms.csv', encoding='ISO-8859-1', nrows= num_rows)

read = input("Enter the Correct Acronym: ")
i = 0
run = True

while i < data.shape[0]:
    if read == data.acronym[i]:
        print("The Definition is:", data.defination[i])
        run = False  # Break out of the loop once the acronym is found
        break
    i += 1

if run:
    print("Acronym not found in the dataset.")