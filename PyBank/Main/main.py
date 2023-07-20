import os
import csv


csvpath = os.path.join("python-challenge","PyBank","Resources","budget_data.csv")

with open(csvpath,encoding='UTF-8') as csv_file: # why is it encoding? vs just , 'r'
    csv_reader = csv.reader(csv_file,delimiter=',')
    csv_header = next(csv_file) # this line of code should skip the header of any excel sheet/csv file and focus on the data not headers ( Since headers are often the first row)
    
       
    months = []
    money = [] 
    for column in csv_reader:
        months.append(column[0])
        money.append(int(column[1])) # wait can we format this?
        


  
    total_months = len(months)
    profit = sum(money)
    average =  profit / total_months
    increase = max(int(profit))
    decrease = min(int(profit))



print(f"Total Months: {total_months}")
print(f"Loss/Profit is: {profit}")
print(f"average is: {average}")
print(f"The greatest increase was:{increase}" )
print(f"The greatest decrease was: {decrease}" )
