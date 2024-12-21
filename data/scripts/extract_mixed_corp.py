import csv

def is_hindi(character):
    maxchar = max(character)
    if u'\u0900' <= maxchar <= u'\u097f':
        return True
    else:
      return False
    
with open("eng-hin-train.csv", "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        with open("sentencepairs_csv.csv", "r", encoding='utf-8') as f:
            csvFile = csv.reader(f)
            for lines in csvFile:
                lines.pop(0)
                lines.pop(1)
                writer.writerow(lines)

with open("eng-hin-train2.csv", "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        
        with open("hindencorp05.plaintext", "r", encoding='utf-8') as fw:
            data = fw.read()
            data = data.split('\n')
            data = data[:20000]
            for lines in data:
                lines = lines.split('\t')
                lines.pop(0)
                lines.pop(0)
                lines.pop(0)
                hin = lines[1]
                if not (is_hindi(hin)):
                     continue
                else:
                      writer.writerow(lines)

    