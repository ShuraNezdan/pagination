import csv
from pprint import pprint



statin: list = []


with open('data-398-2018-08-30.csv', newline='',  encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    
    
    statin.append([i for i in reader])
    # for i in reader:
        
    #     statin.append(i)
        


pprint(statin)