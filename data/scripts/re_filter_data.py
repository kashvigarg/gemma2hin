import re
import os

ROOT_DIR = os.getcwd()
os.chdir("../spare")
PATH_DIR = os.getcwd()
 
pattern = r'<[^>]*>|<\/[^>]*>|%(?!{)[^ ]*'

def clean_text(filename):
    data = None
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()

    with open(filename, "w", encoding="utf-8") as fw:
        for line in data:
            clean_line = re.sub(pattern, '', line)
            fw.write(clean_line)

for filename in os.listdir(PATH_DIR):
    clean_text(os.path.join(PATH_DIR, filename)) 

