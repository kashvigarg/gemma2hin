# Tooling Description

### Translation
--- data/en-hi
- en-hi-train: ```extract_tsv.py``` underlines how the dataset has been converted from its parent TSV format to a usable uniform CSV structure
- en-hi-train2: ```extract_mixed_corp.py``` underlines how the dataset has been extracted from the mixed-language corpus
- en-hi-train3: ```extract_txt.py``` underlines how the dataset has been extracted to CSV from its original TXT format


### Transliteration
--- data/transliteration
```re_filter_data.py``` and
```translit_to_csv.py``` have been used to describe the creation of the transliterated datasets. The former removes a combination of literals from the datasets while ```translit_to_csv.py``` underlines the creation of the translit-aditi dataset.

### Grammar Correction
--- data/mono-hi
```build_vyakaran_datasets.py``` uses Vyakaran Rachna textbook to 


```insert_errors.py```
```pos_tagger.py```

### QnA 
--- data/QnA 
1. HindiQnA.Biology
2. HindiQnA.maths
```translator.py``` has been used to translate 15k data pairs from the MetaMathQA dataset, to Hindi, in order to adequately represent mathematical reasoning within the training dataset. 

3. HindiQnA.squad
4. HindiQnA.Chemistry


## Global Scripts
```add_instructions.py``` adds a combination of varied instructions to the target dataset for reducing instruction-based bias in model training

```filter_token_len.py``` has been used to filter datasets with accordance to token size limits; 512 and 1024.

