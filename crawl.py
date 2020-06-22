from glob import glob

with open("emoji.txt", "r") as f:
    lines = f.read().splitlines()
    for l in lines:
        with open("run_crawl.sh", "a") as fw:
            fw.write('python GetOldTweets3.py --querysearch "'+l+'" --lang en --maxtweets 2000 --output '+l+'.csv\n')