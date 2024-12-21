import stanza
import csv

# Initialize Stanza for Hindi
def initialize_stanza():
    stanza.download("hi")  # Download Hindi language model
    return stanza.Pipeline(lang="hi", processors="tokenize,pos")

# POS Tagging function
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

# Process sentences and save to CSV
def process_and_save_with_pos(input_file, output_file, nlp):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = infile.read()

    sentences = data.split('.')  # Split sentences by '.'
    output_rows = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        # POS Tagging
        tagged_words = tag_pos(sentence, nlp)
        output_rows.append(str(tagged_words))

    # Save results to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        # writer = csv.writer(csvfile)
        # writer.writerow(["POS Tags"])  # Header
        # writer.writerows(output_rows)
        csvfile.write("\n".join(output_rows))

    print(f"Processed {len(sentences)} sentences. Results saved to {output_file}.")

# Main execution
if __name__ == "__main__":
    input_file = "hindi.input.txt"  # Input file with Hindi sentences
    output_file = "hindi_pos_tags.txt"  # Output file for POS-tagged sentences

    # Initialize Stanza NLP
    nlp_pipeline = initialize_stanza()

    # Process sentences and save with POS tags
    process_and_save_with_pos(input_file, output_file, nlp_pipeline)
