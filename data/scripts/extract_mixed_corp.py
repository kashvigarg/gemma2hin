''' ------ Data Source ------
HindEnCorp 0.5, Charles University

[https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0023-625F-0]
'''


import csv

def is_hindi(character):
    maxchar = max(character)
    if u'\u0900' <= maxchar <= u'\u097f':
        return True
    else:
      return False

with open("en-hi-train2.csv", "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        with open("hindencorp05.plaintext", "r", encoding='utf-8') as fw:
            data = fw.read()
            data = data.split('\n')

            # First 20k lines
            data = data[:20000]
            for lines in data:
                lines = lines.split('\t')

                # Remove metadata columns
                lines.pop(0)
                lines.pop(0)
                lines.pop(0)

                # Filter for non-hindi chars
                hin = lines[1]
                if not (is_hindi(hin)):
                     continue
                else:
                      writer.writerow(lines)

    