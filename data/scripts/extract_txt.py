''' ------ Data Source ------

[https://github.com/suvaansh/Machine-Translation-English-to-Hindi-/blob/master/hin.txt]
'''


import csv

def is_hindi(character):
    maxchar = max(character)
    if u'\u0900' <= maxchar <= u'\u097f':
        return True
    else:
      return False

with open("en-hi-train3.csv", "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        with open("en-hi-train3.txt", "r", encoding='utf-8') as fw:
            data = fw.read()
            data = data.split('\n')
            for line in data:
                i = 0
                for ch in line:
                    if (is_hindi(ch)):
                        break
                    else :
                        i+=1
                eng_sen = line[:i]
                hindi_sen = line[i:]
                eng_sen = eng_sen.strip()
                hindi_sen = hindi_sen.strip()
                writer.writerow([eng_sen, hindi_sen])

    
