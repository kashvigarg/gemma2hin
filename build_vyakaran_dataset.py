import os
import csv
from more_itertools import batched

ROOT_DIR = os.getcwd()
os.chdir("../mono-hi")
PATH_DIR = os.getcwd()
FILENAME = ""

# manually edit fields
data = """"""
error = ""
list1 = []
list2 = []

# for paragraphs of single word errors
with open(os.path.join(PATH_DIR, FILENAME), "a", encoding="utf-8", newline='') as f:
    lines = data.split("\n")
    words = []
    writer = csv.writer(f)
    for line in lines:
        sub_words = line.split(" ")
        for w in sub_words:
            if (w!=''):
                words.append(w)
    
    for batch in batched(words, n=2):
        (hi_err, hi_corr) = batch
        writer.writerow([hi_err, hi_corr, error])

# for lists of single word errors
with open(os.path.join(PATH_DIR, FILENAME), "a", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    i = 0
    words = []

    if (len(list1)!=len(list2)):
        print("Lists not Equal")

    for w in list1:
        if (w!=''):
            words.append(list1[i])
            words.append(list2[i])
        i=i+1

    for batch in batched(words, n=2):
        (hi_err, hi_corr) = batch
        writer.writerow([hi_err, hi_corr, error])

# for paragraphs of sentence-length errors
with open(os.path.join(PATH_DIR, FILENAME), "a", encoding="utf-8", newline='') as f:
    lines = data.split("\n")
    sentences = []
    writer = csv.writer(f)
    for line in lines:
        ul = line.split("।")
        l = []
        for u in ul:
            if (u!=''):
                # handle questions
                if not (u.endswith('?')):
                    u += "।"
                u.strip()
                l.append(u)
        if (len(l)<2):
            continue
        hi_err, hi_corr = l[0], l[1]
        writer.writerow([hi_err, hi_corr, error])