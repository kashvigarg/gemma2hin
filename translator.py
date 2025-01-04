from deep_translator import GoogleTranslator
import pandas as pd
import time

SOURCE_FILE = './maths.csv'
TARGET_FILE = './data/QnA/HindiQnA.maths.csv'

BATCH_SIZE = 100
RETRY_DELAY = 5 

# Fetch 15k units of MathsQnA
df = pd.read_json("hf://datasets/meta-math/MetaMathQA/MetaMathQA-395K.json")
df = df[:15000]
df.drop(columns=["type","original_question"], inplace=True)
df.rename(columns={"response":"output", "query":"input"}, inplace=True)
df.to_csv(SOURCE_FILE, index=False)

df = pd.read_csv(SOURCE_FILE)
df_inp = df["input"].to_list()
df_out = df["output"].to_list()

total_records = len(df_inp)
print(f"Total records to translate: {total_records}")

def translate_batch(batch_input, batch_output):
    try:
        translated_input = GoogleTranslator('en', 'hi').translate_batch(batch_input)
        translated_output = GoogleTranslator('en', 'hi').translate_batch(batch_output)
        return translated_input, translated_output
    except Exception as e:
        print(f"Error during translation: {e}")
        return None, None

for start in range(0, total_records, BATCH_SIZE):
    end = start + BATCH_SIZE
    batch_inp = df_inp[start:end]
    batch_out = df_out[start:end]

    print(f"Translating batch {start // BATCH_SIZE + 1} ({start} to {end})...")

    translated_inp, translated_out = None, None
    for attempt in range(3):  
        translated_inp, translated_out = translate_batch(batch_inp, batch_out)
        if translated_inp and translated_out:
            break  
        print(f"Retrying batch {start // BATCH_SIZE + 1} (Attempt {attempt + 1})...")
        time.sleep(RETRY_DELAY)

    if not translated_inp or not translated_out:
        print(f"Failed to translate batch {start // BATCH_SIZE + 1}. Skipping...")
        continue  

    batch_df = pd.DataFrame({
        "input": translated_inp,
        "output": translated_out
    })
    with open(TARGET_FILE, "a", encoding="utf-8", newline="") as f:
        batch_df.to_csv(f, index=False, header=f.tell() == 0)  

    time.sleep(1)

print("Translation completed!")
