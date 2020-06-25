count = 0
with open('output_len80_total1000.csv', 'r') as reader:
    for line in reader:
        count += 1

print("total:", count)
