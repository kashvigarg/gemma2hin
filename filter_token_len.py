from transformers import AutoTokenizer
import os
import pandas as pd

# translit
# qna_maths
# qna_bio
# qna_chem

CWD = os.getcwd()

paths = [
    "./data/transliteration/hinglish.hindi.csv",
    "./data/transliteration/translit-aditi.csv",
    "./data/QnA/HindiQnA.maths.csv",
    "./data/QnA/HindiQnA.Biology.csv",
    "./data/QnA/HindiQnA.Chemistry.csv"
]

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b-it", add_eos_token=True, use_fast=True, token="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")
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

def filter_token_len(filepath, newpath):
    df = pd.read_csv(filepath)
    print("Old size:", len(df))
    
    def tokenize_row(row):
        data = f"### instruction: {row['instruction']} ### input: {row['input']} ### output: {row['output']}" + tokenizer.eos_token
        return len(tokenizer(data, truncation=False)["input_ids"])
    
    df["tokenized_length"] = df.apply(tokenize_row, axis=1)
    filtered_df = df[df["tokenized_length"] <= 512].drop(columns=["tokenized_length"])
    filtered_df.to_csv(newpath, index=False)
    print("New size:", len(filtered_df))

for path in paths:
    new_path = path.replace(".csv", ".filtered.csv")

    filter_token_len(filepath=path, newpath=new_path)