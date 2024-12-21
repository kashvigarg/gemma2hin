'''POS Tagger for hindi.input.txt as extracted using wikiextract/
'''

import stanza
import csv

def initialize_stanza():
    stanza.download("hi") 
    return stanza.Pipeline(lang="hi", processors="tokenize,pos")

def tag_pos(sentence, nlp):
    """
    Tags parts of speech for a given Hindi sentence using Stanza.

    :param sentence: A string containing the Hindi sentence.
    :param nlp: The initialized Stanza NLP pipeline.
    :return: List of tuples (word, POS tag).
    """
    doc = nlp(sentence)
    tagged_words = []
    for sentence in doc.sentences:
        for word in sentence.words:
            tagged_words.append((word.text, word.upos))  # Text and Universal POS tags
    return tagged_words

def process_and_save_with_pos(input_file, output_file, nlp):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = infile.read()

    sentences = data.split('.')  # Split sentences by '.'
    output_rows = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        tagged_words = tag_pos(sentence, nlp)
        output_rows.append(str(tagged_words))

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvfile.write("\n".join(output_rows))

    print(f"Processed {len(sentences)} sentences. Results saved to {output_file}.")

if __name__ == "__main__":
    input_file = "hindi.input.txt"  
    output_file = "hindi_pos_tags.txt"  

    # Initialize Stanza NLP
    nlp_pipeline = initialize_stanza()

    # Process sentences and save with POS tags
    process_and_save_with_pos(input_file, output_file, nlp_pipeline)
