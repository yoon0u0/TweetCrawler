emoji_list = []

with open('emoji.txt', 'r') as f:
    emoji_list = f.read().splitlines()
print(emoji_list)

for emoji in emoji_list:
    count = 0
    count2 = 0
    count3 = 0

    with open(emoji+'.csv', 'r') as reader:
        for line in reader:
            count += 1
    print(emoji, count)

    with open(emoji+'2.csv', 'r') as reader:
        for line in reader:
            count2 += 1
    print(emoji+'2', count2)

    # with open(emoji+'3.csv', 'r') as reader:
    #     for line in reader:
    #         count3 += 1
    # print(emoji+'3', count3)
