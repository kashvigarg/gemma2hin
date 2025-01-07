import pandas as pd
import os
import datasets
import csv
from datasets import load_dataset

ROOT_DIR = os.getcwd()
os.chdir("../transliteration")
PATH_DIR = os.getcwd()
FILENAME = "translit1.csv"
DSNAME = "hinglish.aditi/hinglish.aditi.csv"

CSV_PATH = os.path.join(PATH_DIR, FILENAME)
DS_PATH = os.path.join(PATH_DIR, DSNAME)
# df1 = pd.read_csv(CSV_PATH)
# df2 = pd.read_csv(DS_PATH)

# print(len(df1))
ds = load_dataset("manishiitg/aditi-syn-v2")

with open (CSV_PATH, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["instruction", "input", "output"])
    for message in ds["train"]["messages"]:
        # instr,input,output
        data_list = []
        for content in message:
            if (content['content']=="system") | (content['content']==""):
                data_list.append("You are an AI Assistant.")
            else :
                data_list.append(content['content'])
        if len(data_list)==3:
            writer.writerow(data_list)

