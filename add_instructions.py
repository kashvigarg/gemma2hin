import pandas as pd
import os

ROOT_DIR = os.getcwd()
os.chdir("./mono-hi")
PATH_DIR = os.getcwd()


instructions=[
    "Write the Hindi script preserving the pronunciation",
    "Given the Hinglish word, provide its Hindi equivalent",
    "This is a transliteration task. Convert Hinglish to Hindi script",
    "Convert the following text into Hindi script:",
    "Convert this sentence from Hinglish phonetic text to Hindi:",
    "उच्चारण को बनाए रखते हुए हिंदी लिपि लिखें:",
    "दिए गए हिंग्लिश शब्द का हिंदी समानार्थक प्रदान करें:",
    "यह एक लिप्यंतरण कार्य है। हिंग्लिश को हिंदी लिपि में बदलें:",
    "निम्नलिखित शब्द को हिंदी लिपि में बदलें:",
    "Uccharan ko banaye rakhte hue Hindi lipi likhein:",
    "Diye gaye Hinglish shabd ka Hindi samanarthak pradan karein:",
    "Nimnlikhit paath ko Hindi lipi mein badlein:",
    "Yeh ek lipyantaran kaarya hai."
]


# instructions = [
#     "Identify and correct the mistake in the provided Hindi sentence:",
#     "Fix the grammar error in the given Hindi sentence:",
#     "Make corrections to the grammar of the following Hindi sentence:",
#     "Correct the given sentence:",
#     "Identify any grammatical issues in the sentence and fix them:",

#     "दिए गए वाक्य में व्याकरण संबंधी त्रुटि को सुधारें।",
#     "हिंदी वाक्य में मौजूद गलती को ठीक करें।",
#     "निम्नलिखित वाक्य में व्याकरण की त्रुटि पहचानकर सुधारें।",
#     "दिए गए वाक्य को व्याकरण की दृष्टि से सही करें।",
#     "हिंदी वाक्य में गलती खोजें और उसे ठीक करें।",

#     "Diye gaye sentence mein grammar ki galti ko theek karo:",
#     "Hindi sentence ke errors ko identify karke correct karo:",
#     "Grammar mistake ko correct karo jo sentence mein hai:",
#     "Hindi sentence ka grammar sahi karo:",
#     "Jo bhi error hai Hindi sentence mein, usse fix karo:"
# ]

def add_instructions(filename):
    df = pd.read_csv(filename)
    df['instruction'] = [instructions[i % len(instructions)] for i in range(len(df))]
    df_reorder = df[['instruction', 'english', 'transliterated_hindi']]
    df_reorder.to_csv(filename, index=False)
    print(f"Instructions added and saved to {filename}.")

for filename in os.listdir(PATH_DIR):
    add_instructions(os.path.join(PATH_DIR, filename)) 

