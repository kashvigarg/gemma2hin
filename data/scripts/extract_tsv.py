import csv
import pandas as pd

tsv_file = 'sentence_pairs.tsv'
csv_form = pd.read_table(tsv_file, sep='\t')
csv_form.to_csv('sentence_pairs_csv.csv', index=False)

with open("sentence_pairs_csv.csv", "r", encoding='utf-8') as source: 
    reader = csv.reader(source) 
      
    with open("output.csv", "w", encoding='utf-8', newline='') as result: 
        writer = csv.writer(result) 
        for r in reader: 
            writer.writerow((r[1], r[3]))
