import csv
import numpy as np
with open('tweet.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            print(row[2])
        except:
            pass
