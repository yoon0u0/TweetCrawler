import csv, re

data_all = open('output_len80_total1000.csv', 'w', encoding='utf-8')
emoji_count = open('emojicount_len80_total1000.csv', 'w', encoding='utf-8')

output = csv.writer(data_all)
emoji_count_f = csv.writer(emoji_count)

emoji_list = []
min_length = 80

with open('emoji.txt', 'r') as f:
    emoji_list = f.read().splitlines()
print(emoji_list)

for emoji in emoji_list:
    count = 0

    ## emoji.csv
    with open(emoji + '.csv', 'r', encoding="utf-8") as f:
        data = csv.reader(f)
        data.__next__()
        for tokens in data:
            tweet = tokens[2]
            label = emoji

            ## regexp
            regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            url = re.findall(regex, tweet)
            url_list = [x[0] for x in url] 

            if len(url_list) == 0 and len(tweet) >= min_length:
                output.writerow([tweet, len(tweet), label])
                count += 1
        # emoji_count_f.writerow([emoji, count])


    ## emoji2.csv
    with open(emoji + '2.csv', 'r', encoding="utf-8") as f:
        data = csv.reader(f)
        data.__next__()
        for tokens in data:
            tweet = tokens[2]
            label = emoji

            ## regexp
            regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            url = re.findall(regex, tweet)
            url_list = [x[0] for x in url] 

            if len(url_list) == 0 and len(tweet) >= min_length:
                output.writerow([tweet, len(tweet), label])
                count += 1
            
            if count < 1000:
                continue
            else:
                break
        # emoji_count_f.writerow([emoji, count])

    if count < 1000: 
        with open(emoji + '3.csv', 'r', encoding="utf-8") as f:
            data = csv.reader(f)
            data.__next__()
            for tokens in data:
                tweet = tokens[2]
                label = emoji

                ## regexp
                regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
                url = re.findall(regex, tweet)
                url_list = [x[0] for x in url] 

                if len(url_list) == 0 and len(tweet) >= min_length:
                    output.writerow([tweet, len(tweet), label])
                    count += 1
                
                if count < 1000:
                    continue
                else:
                    break
            # emoji_count_f.writerow([emoji, count])

    emoji_count_f.writerow([emoji, count])
        
data_all.close()
emoji_count.close()


