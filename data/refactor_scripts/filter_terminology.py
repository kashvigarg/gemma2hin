import os
import csv
import pandas as pd
import random

# Directory setup
ROOT_DIR = os.getcwd()
os.chdir("../en-hi-terminology")  # Adjust this based on your actual directory structure
PATH_DIR = os.getcwd()

# File paths
PHY_PATH = "physics.txt"
CHEM_PATH = "chemistry.txt"
BIO_PATH = "biology.txt"

# Output CSV paths
PHY_CSV = "physics.csv"
CHEM_CSV = "chemistry.csv"
BIO_CSV = "biology.csv"
FINAL_CSV = "final_data.csv"

def is_hindi(character):
    maxchar = max(character)
    if u'\u0900' <= maxchar <= u'\u097f':
        return True
    else:
      return False

def process_physics():
    """Processes the physics.txt file."""
    with open(os.path.join(PATH_DIR, PHY_PATH), encoding="utf-8") as f:
        with open(PHY_CSV, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            phy_data = f.readlines()
            data = []
            for line in phy_data:
                words = line.split("(")
                if (len(words)>2):
                    continue
                hin = words[0].strip()
                eng = words[1].strip()
                eng = eng[:len(eng)-1]
                writer.writerow([eng,hin])


def process_chemistry():
    """Processes the chemistry.txt file."""
    with open(os.path.join(PATH_DIR, CHEM_PATH), encoding="utf-8") as f:
        chem_data = f.readlines()
        with open(CHEM_CSV, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for line in chem_data:
                i = 0
                for ch in line:
                    if not (is_hindi(ch)) and ch!=" " and ch!="," and ch!="(" and ch!=")" and ch!="-":
                        break
                    else :
                        i+=1
                hindi_sen = line[:i]
                eng_sen = line[i:]
                eng_sen = eng_sen.strip()
                hindi_sen = hindi_sen.strip()
                writer.writerow([eng_sen,hindi_sen])

def process_biology():
    """Processes the biology.txt file."""
    with open(os.path.join(PATH_DIR, BIO_PATH), encoding="utf-8") as f:
        bio_data = f.readlines()
        with open(BIO_CSV, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for line in bio_data:
                i = 0
                for ch in line:
                    if not (is_hindi(ch)) and ch!=" " and ch!="," and ch!="-":
                        break
                    else :
                        i+=1
                hindi_sen = line[:i]
                eng_sen = line[i:]
                eng_sen = eng_sen.strip()
                hindi_sen = hindi_sen.strip()
                writer.writerow([eng_sen,hindi_sen])

def select_and_shuffle_data():
    """Selects and shuffles data from individual CSV files and writes to a final CSV."""
    # Read data from CSVs
    phy_df = pd.read_csv(PHY_CSV, encoding="utf-8", header=None)
    chem_df = pd.read_csv(CHEM_CSV, encoding="utf-8", header=None)
    bio_df = pd.read_csv(BIO_CSV, encoding="utf-8", header=None)

    # Select subsets
    selected_phy = phy_df[:300]
    selected_chem = chem_df[:300]
    selected_bio = bio_df[:200]

    # Combine and shuffle
    combined_df = pd.concat([selected_phy, selected_chem, selected_bio])

    # Write to final CSV
    combined_df.to_csv(FINAL_CSV, index=False, encoding="utf-8")
    print(f"Final shuffled dataset written to {FINAL_CSV}")

# Process files
process_physics()
process_chemistry()
process_biology()

# Select and shuffle data
select_and_shuffle_data()
