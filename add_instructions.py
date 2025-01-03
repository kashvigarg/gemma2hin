import pandas as pd
import os

ROOT_DIR = os.getcwd()
os.chdir("../mono-hi")
PATH_DIR = os.getcwd()
 
 #edit commit
instructions = [
    "Identify and correct the mistake in the provided Hindi sentence:",
    "Fix the grammar error in the given Hindi sentence:",
    "Make corrections to the grammar of the following Hindi sentence:",
    "Correct the given sentence:",
    "Identify any grammatical issues in the sentence and fix them:",

    "दिए गए वाक्य में व्याकरण संबंधी त्रुटि को सुधारें।",
    "हिंदी वाक्य में मौजूद गलती को ठीक करें।",
    "निम्नलिखित वाक्य में व्याकरण की त्रुटि पहचानकर सुधारें।",
    "दिए गए वाक्य को व्याकरण की दृष्टि से सही करें।",
    "हिंदी वाक्य में गलती खोजें और उसे ठीक करें।",

    "Diye gaye sentence mein grammar ki galti ko theek karo:",
    "Hindi sentence ke errors ko identify karke correct karo:",
    "Grammar mistake ko correct karo jo sentence mein hai:",
    "Hindi sentence ka grammar sahi karo:",
    "Jo bhi error hai Hindi sentence mein, usse fix karo:"
]

def add_instructions(filename):
    df = pd.read_csv(filename)
    df['instruction'] = [instructions[i % len(instructions)] for i in range(len(df))]
    df_reorder = df[['instruction', 'hi_err', 'hi_corr']]
    df_reorder.to_csv(filename, index=False)
    print(f"Instructions added and saved to {filename}.")

for filename in os.listdir(PATH_DIR):
    add_instructions(os.path.join(PATH_DIR, filename)) 

