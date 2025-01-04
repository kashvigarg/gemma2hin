import pandas as pd
import os
import datasets
import csv
from datasets import load_dataset

ROOT_DIR = os.getcwd()
os.chdir("../translit")
PATH_DIR = os.getcwd()
FILENAME = "translit1.csv"

CSV_PATH = os.path.join(PATH_DIR, FILENAME)

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
        
        writer.writerow(data_list)

