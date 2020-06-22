import csv

data_all = open('output.csv', 'w', encoding='utf-8')
output = csv.writer(data_all)

emoji_list = []

with open('just.txt', 'r') as f:
    emoji_list = f.read().splitlines()
print(emoji_list)

for emoji in emoji_list:
    with open(emoji + '.csv', 'r', encoding="utf-8") as f:
        data = csv.reader(f)
        data.__next__()
        for tokens in data:
            tweet = tokens[2]
            label = emoji
            output.writerow([tweet,label])

data_all.close()

count = 0
with open('output.csv', 'r') as reader:
    for line in reader:
        count += 1
print(count)

