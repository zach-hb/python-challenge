import os
import csv

# count of months
total_month = 0

# net value of profits/losses
net_value = 0

# total amount of 
total_change = 0

# placeholder for current value profit/loss
current_value = 0

# current month value - previous month value
current_change = 0

# list to store all changes
change_list = []

csvpath = os.path.join("Resources", "budget_data.csv")
# print(csvpath)        checking path
if not os.path.exists(csvpath):
    print("File does not exist.")
    exit()

with open(csvpath, "r") as csvreader:
    reader = csv.reader(csvreader, delimiter = ",")
    header = next(reader)

    # starts csv at the 2nd row
    previous_month = next(reader)

    # value of month -1, since we start at 2nd row
    previous_month_value = int(previous_month[1])

    # reads file as list
    list_reader = list(reader)

    # accounting for previous_month
    total_month = total_month +1

    # accounting for previous month value
    net_value = net_value + previous_month_value

    for row in list_reader:
        total_month +=1
        net_value += int(row[1])
        current_change =  int(row[1]) - previous_month_value
        previous_month_value = int(row[1])
        change_list += [current_change]

    average_change = sum(change_list)/len(change_list)

# find location of greatest profit in list, then greatest loss
# greatest_value_index = change_list.index(max(change_list))
# print(greatest_value_index)
# greatest_loss_index = change_list.index(min(change_list))
# print(greatest_loss_index)
print("Total Months:",total_month)
print("Total: $",net_value)
print("Average Change: $",average_change)
print("Greatest Increase in Profits:", list_reader[78][0],max(change_list))
print("Greatest Decrease in Profits:", list_reader[48][0],min(change_list))

with open("analysis/output.txt", "x") as f:
    print("Total Months:",total_month, file=f)
    print("Total: $",net_value, file=f)
    print("Average Change: $",average_change,file=f)
    print("Greatest Increase in Profits:", list_reader[78][0],max(change_list),file=f)
    print("Greatest Decrease in Profits:", list_reader[48][0],min(change_list),file=f)