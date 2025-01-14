## Introduction
### Background
General finetuning efforts for Indian-Based Languages including Hindi are concentrated in producing task-specific LLMs, for example, QnA Agents that can help with assistive tasks in said language. Most of these models are trained with a focus on machine translation, and often generate qualitatively erroneous content because they lack an in-depth knowledge about the language.

Moreover, Grammar rules differ from language to language , same is the case for the Hindi language. To name a few differences :-
- Verb placement in English is usually before the noun, while in hindi its usually after the noun. Example:-

  `English - I like Mangoes.`

  `like` is the verb and `Mangoes` is the noun.

  `Hindi Translation - मुझे आम पसंद हैं।`

  `आम` is the noun i.e Mangoes arrives first followed by the verb `पसंद हैं` ie like
- In english the gender only affects the pronouns and nouns, while in hindi it affects the verb as well. Example:-

  `He drives a car` - `Male`
  
  `She drives a car` - `Female`

  In both these cases the verb `drive` remains the same while the pronouns change.

  `वह कार चलाता है।` - `Male`
  
  `वह कार चलाती है।` - `Female`

  In this case the verb is converted from `चलाता है।` in Male to `चलाती है।` in Females.

  and many more.
  
A lot of finetunining efforts fail to capture this essence of the Hindi language leading to illformed context and subpar translations. 

Various cultral nuances in the Hindi language like most of the languages of the Indian Subcontinent make it standout from its European counterparts. One such nuance is use of different pronouns depending upon the context such as age, position of a person being referred to etc. For exmaple:-

| English         | Hindi          | Context                       |
|-----------------|----------------|--------------------------------------------------|
|You should sleep.| तुम्हें सोना चाहिए। | For someone of the same age, younger, more casual |
|You should sleep.|आपको सोना चाहिए।| for someone older, more respecful                 |

and many more.

Now coming on to the bigger issue, most people who interact with LLMs using Hindi, are most probably using an  `ASCII KEYBOARD`, which provides only romanized english characters, apart from that various aspects of hindi language such as the use of `matras` make it harder to type. As a result a Hindi word 

say `भरोसा` which means trust will be written as `bharosa`

using the ASCII Keyboard, we have on our devices. We'll refer to this is as Transliterated Hindi, Phonetic Hindi or simply Hinglish. This is probably the most popular form of written hindi communication in the digital age. This needs to be considered while we are finetung our Language models on Hindi, as good percentage of user input in hindi will be of this form.

### Proposed Solution

With Viraam - Our finetunined Gemma2 Model, our goal is to develop an LLM for Hindi that tries to:
- Produces grammatically and culturally accurate textual media
- Suggests paraphrasing, and literary corrections for uploaded content
- Engages in fluent conversational dialogue with the user, including the understanding of transliterated and phonetic texts
- Performs mathematical, and scientific assistive tasks with ease in Hindi
- Recognizes cultural specific contexts and concepts definitive to Hindi, and its country of origin, India

## Dataset Curation
Data curation is one of the most if not the most important step in the finetunig process, slightly skewed datasets can lead to major overfitting or underfitting in the later stages, while uncleaned or irrelevant data can lead to halucination in output generation. Keeping these points in mind, our data processing has passed through various phases. These include:-
- ### Data Creation
  - Generating artificial or semi-artificial data, using ingenious or AI enabled tools.
- ### Data Collection
  - Data scraping.
    - Includes scraping data from various websites , open sourced github repositories, E-books (which allow such data collection for educational purposes)
  - Data extraction.
    - Data extracted using official tools from Wikipedia and Government Of India
- ### Data Preprocessing
  - Converting files to compatible file types.
    - converting from paraquet, tsv or text files to csv or json for ease of handling. 
  - Cleaning Data Using various techniques.
    - Uing various regex filters , as well as custom functions to remove special symbols, unrelated or illformed language data and other anomolies from the collected or created data.
  - Adding instructions into the dataset for instruction based finetunining.
    - Since we are finetuning an instructive model, various commands and prompts were added in order to get the best results in each data set.

As part of the finetuning process, we train the Gemma2 2b parameter instructive model on a few sets of mixed data with the following compositional characteristics:

### Types of Datasets
#### 1) English to Hindi Translation
In complex adaptive languages like Hindi, there are multiple ways to express the same idea, for example, the word "Jump" can be translated as उछलो or कूदो, among others.

This variation becomes even more pronounced when considering factors like gender, levels of formality and expressions of respect. In order to build high-quality datasets for our eng-hindi translation task, we chose sources that maintain this variation.

1. Contains 2869 English phrases along with their Hindi translations [^1].

2. contains 13182 human-annotated translation pairs of english to hindi translations [^2]

3. contains about 50k translated pairs, mainly comprising of transcribed spoken data in Hindi, TED talks with Hindi transcripts, and Wikipedia articles [^3]

#### 2) Hindi to Hindi Grammar Correction & Paraphrasing 
The creation and writing of Hindi content often encounters challenges such as errors in orthography, syntax, or overall fluency. Despite these prevalent issues, the vast diversity of errors in Hindi, coupled with the limited availability of digitized content, has left this area largely unexplored.

As the part of the Viraam project, we have developed a comprehensive corpus of <incorrect Hindi, corrected Hindi> pairs using a blend of automated and manual techniques, with a special focus on grammatical errors in the language. This includes:
- Generating inflectional errors from scraped Wikipedia content using POS taggers.
- Manually extracting errors from traditional Hindi grammar books and preprocesing them to suit our requiremnents [^4].

The following flowchart represents errors we have chosen for representation within our dataset.

[closable columns]
flowchart

#### 3) Transliteration
The model is finetuned using 2 sets of transliteration datasets; 
- It features 30k transliterated word, and sentence pairs [^5]. The advantage it offers is that it provides multiple transliterated hindi words for single hindi word that different people might use. Such as the word `पिघले` can be written as `pighle` or `pighale`.
- It includes 55.5k sentence pairs that are uniquely presented in a QnA fashion, with data formats handling instruct-follow, user-assistant roleplay, code-writing and general Q/A on Indian Context [^6].

#### 4) Question/Answer or Conversational Content
We also aim to enhance the model's capabilities for extractive question answering and assistive tasks. This includes enabling the model to identify and extract precise answers from Hindi texts based on user queries, or provided context as well as understand user commands appropriately.

For this purpose various Hindi QnA based datasets with variety of questions from subjects like chemistry, biology, physics, indian history were selected and were sprinkled throughout the data. Apart from providing the necessary Indian context and Hindi terminologies this also makes sure that the model doesnt overfit while performing monotonous tasks like translation and transliteration.

#### Scientific & Mathematical Reasoning
To facilitate quantitive reasoning abilities within the finetuned model, we include Hindi datasets with scientific context, in the form of; [^7] that contains about 40k Hindi translated problem-solution pairs spanning across 25 Biology topics, and [^8], constituting similar context for Chemistry. 

As part of the required mathematical content, we translated 15k pairs from [^9] using the (deep_translator)[https://pypi.org/project/deep-translator/] pipeline for Google Translate, featuring a wide variety of question-answer pairs spread across various important mathematical concepts like arithmetic calculations, and word problems, providing necessary hindi terminologies for mathematical problems.

#### Contextual Awareness QnA
In complex languages like Hindi, many intra-language nuances stem from cultural and historical events or stories. Therefore, incorporating cultural literacy into our dataset is crucial. [^10] and [^11] helps us adequately represent this within our model.


### Adding Instructions to our Datasets
As mentioned above ,to minimize instruction-specific bias in model responses and to make the model more averse with varied inputs , we incorporate diverse instruction prompts. These prompts are a combination human and machine generated data. Each dataset within the combined collection includes 12- 15 variations of instructions. These instructions are written in English, Hindi and Transliterated Hindi. One exmaple of instructions for grammar correction datasets is given below.
```
instructions_grammar = [
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
```
The rest can be viewed in [instructions_config](https://github.com/jaydee029/gemma2hin/blob/main/instruction_config.py) file.

### Various Tools Used
For Grammar
- Error Injection Tool
  - We used a custom error injection tool for inserting grammatical error of various types into the hindi sentences fetched from wikipedia dumps. This tool was created by forking the wikiextracter tool [^12], we added a custom POS tagger into the tool [here](https://github.com/kashvigarg/gemma2hin/blob/main/pos_tagger.py) and made necessary changes in the legacy codebase to make it work upto our expectations.
  - We added grammatical errors associated with hindi adjectives , pronouns and auxilliary verbs, The POS Tagger would break the sentences in to small tokens and assign each token a POS Tag, these lists would then pass through our [insert_error](https://github.com/kashvigarg/gemma2hin/blob/main/insert_errors.py) script, which would juggle various parts of speech such as `matras` to include a small error of a certain type in each sentence.
- [build_vyakaran_datasets.py](https://github.com/kashvigarg/gemma2hin/blob/main/build_vyakaran_dataset.py) uses Vyakaran Rachna textbook to build and clean grammar datasets
 
scripts used for data in english to hindi translation
- [extract_tsv.py](https://github.com/kashvigarg/gemma2hin/blob/main/data/refactor_scripts/extract_tsv.py) underlines how the dataset has been converted from its parent TSV format to a usable uniform CSV structure.
- [extract_mixed_corp.py](https://github.com/kashvigarg/gemma2hin/blob/main/data/refactor_scripts/extract_mixed_corp.py) underlines how the dataset has been extracted from the mixed-language corpus.
- [extract_txt.py](https://github.com/kashvigarg/gemma2hin/blob/main/data/refactor_scripts/extract_txt.py) underlines how the dataset has been extracted to CSV from its original TXT format.

scripts used for transliterated data collection and processing
- [re_filter_data.py](https://github.com/kashvigarg/gemma2hin/blob/main/data/refactor_scripts/re_filter_data.py) and [translit_to_csv.py](https://github.com/kashvigarg/gemma2hin/blob/main/data/refactor_scripts/translit_to_csv.py) have been used to describe the creation of the transliterated datasets. The former removes a combination of literals from the datasets while translit_to_csv.py underlines the creation of the translit-aditi dataset.

Other scripts
[translator.py](https://github.com/kashvigarg/gemma2hin/blob/main/translator.py) has been used to translate 15k data pairs from the MetaMathQA dataset, to Hindi, in order to adequately represent mathematical reasoning within the training dataset.

[add_instructions.py](https://github.com/kashvigarg/gemma2hin/blob/main/add_instructions.py) adds a combination of varied instructions to the target dataset for reducing instruction-based bias in model training

[filter_token_len.py](https://github.com/kashvigarg/gemma2hin/blob/main/filter_token_len.py) has been used to filter datasets with accordance to token size limits; 512 and 1024.

### References 

[^1]: https://github.com/suvaansh/Machine-Translation-English-to-Hindi-/tree/master 

[^2]: https://tatoeba.org/en/downloads

[^3]: https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0023-625F-0#

[^4]: हिन्दी व्याकरण एवं रचना प्रबोध, 9-12, Board of Secondary Education Rajasthan, Ajmer

[^5]: https://raw.githubusercontent.com/bsantraigi/tensorflow-seq2seq-hindi/master/data/Hindi%20-%20Word%20Transliteration%20Pairs%201.txt  

[^6]: https://huggingface.co/datasets/manishiitg/aditi-syn-v2

[^7]: https://huggingface.co/datasets/manishiitg/camel-ai-biology

[^8]: https://huggingface.co/datasets/manishiitg/camel-ai-chemistry

[^9]: https://huggingface.co/datasets/meta-math/MetaMathQA/tree/main

[^10]: https://huggingface.co/datasets/aneesh-b/SQuAD_Hindi

[^11]: https://huggingface.co/datasets/kaifahmad/indian-history-hindi-QA-3.4k

[^12]: https://github.com/s-ankur/wikiextract/tree/0d854e6e91db3e5e99d1e9a58781e08513fbbfb4




