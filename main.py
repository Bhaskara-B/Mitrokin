import pandas as pd

data = pd.read_csv('acronyms.csv', encoding='ISO-8859-1')


read = input("Enter the Correct Acronym: ")
found = False

for i in range(len(data)):
	if read == data.acronym[i]:
		print("The Definition is:", data.defination[i])
		found = True
		

if not found:
	print("Acronym not found in the dataset.")
