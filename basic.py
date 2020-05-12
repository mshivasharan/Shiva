import time
import os
import pandas

while True:
    if os.path.exists("tempts_today.csv"):
        data = pandas.read_csv("tempts_today.csv") 
        print(data.mean()["st1"])
    else:
        print("file does not exist")
    time.sleep(10)