## Introduction

General finetuning efforts for Indian-Based Languages including Hindi are concentrated in producing task-specific LLMs, for example, QnA Agents that can help with assistive tasks in said language. Most of these models are trained with a focus on machine translation, and often generate qualitatively erroneous content because they lack an in-depth knowledge about the language.

With Viraam, our goal is to develop an LLM for Hindi that:
- Produces grammatically and culturally accurate textual media
- Suggests paraphrasing, and literary corrections for uploaded content
- Engages in fluent conversational dialogue with the user, including the understanding of transliterated and phonetic texts
- Performs mathematical, and scientific assistive tasks with ease in Hindi
- Recognizes cultural specific contexts and concepts definitive to Hindi, and its country of origin, India

## Dataset Curation
As part of the finetuning process, we train the base instruct Gemma2 on 2 sets of mixed data with the following compositional characteristics:

#### 1) English to Hindi Translation
In complex adaptive languages like Hindi, there are multiple ways to express the same idea, for example, the word "Jump" can be translated as उछलो or कूदो, among others.

This variation becomes even more pronounced when considering factors like gender, levels of formality and expressions of respect. In order to build high-quality datasets for our eng-hindi translation task, we chose sources that maintain this variation.

[1] contains 2869 English phrases along with their Hindi translations.

[2] contains 13182 human-annotated translation pairs 

[3] contains about 50k translated pairs, mainly comprising of transcribed spoken data in Hindi, TED talks with Hindi transcripts, and Wikipedia articles 

#### 2) Hindi to Hindi Grammar Correction & Paraphrasing 
The creation and writing of Hindi content often encounters challenges such as errors in orthography, syntax, or overall fluency. Despite these prevalent issues, the vast diversity of errors in Hindi, coupled with the limited availability of digitized content, has left this area largely unexplored.

As part of the Viraam project, we have developed a comprehensive corpus of <incorrect Hindi, corrected Hindi> pairs using a blend of automated and manual techniques, with a special focus on grammatical errors in the language. This includes:

Generating inflectional errors from scraped Wikipedia content using POS taggers.
Manually extracting errors from traditional Hindi grammar books.

The following flowchart represents errors we have chosen for representation within our dataset.

[closable columns]
flowchart

#### 3) Question/Answer or Conversational Content
We also aim to enhance the model's capabilities for extractive question answering and assistive tasks. This includes enabling the model to identify and extract precise answers from Hindi texts based on user queries, or provided context as well as understand user commands appropriately.

#### 4) Transliteration
The model is finetuned using 2 sets of transliteration datasets; [12] features 30k transliterated word, and sentence pairs. [11] includes 55.5k sentence pairs that are uniquely presented in a QnA fashion, with data formats handling instruct-follow, roleplay (Indian Famous Characters), code-writing and general Q/A on Indian Context.

#### 5) Scientific & Mathematical Reasoning
To facilitate quantitive reasoning abilities within the finetuned model, we include Hindi datasets with scientific context, in the form of; [8] that contains about 40k Hindi translated problem-solution pairs spanning across 25 Biology topics, and [9], constituting similar context for Chemistry. 

As part of the required mathematical content, we translated 15k pairs from [10] using the (deep_translator)[https://pypi.org/project/deep-translator/] pipeline for Google Translate, featuring a wide variety of question-answer pairs spread across various important mathematical concepts like arithmetic calculations, and word problems.

#### 6) Contextual Awareness
In complex languages like Hindi, many intra-language nuances stem from cultural and historical events or stories. Therefore, incorporating cultural literacy into our dataset is crucial. [7] helps us adequately represent this within our model.


### Instruction Tuning
To minimize instruction-specific bias in model responses, we incorporate diverse instruction prompts. These prompts are partially generated using GPT-4 and Gemini 1.5. Each dataset within the combined collection includes at least 15 variations of instructions.


### References 

[1] https://github.com/suvaansh/Machine-Translation-English-to-Hindi-/tree/master 

[2] https://tatoeba.org/en/downloads

[3] https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0023-625F-0#

[4] https://github.com/s-ankur/wikiextract/tree/0d854e6e91db3e5e99d1e9a58781e08513fbbfb4

[5] हिन्दी व्याकरण एवं रचना प्रबोध, 9-12, Board of Secondary Education Rajasthan, Ajmer

[6] https://huggingface.co/datasets/aneesh-b/SQuAD_Hindi

[7] https://huggingface.co/datasets/kaifahmad/indian-history-hindi-QA-3.4k

[8] https://huggingface.co/datasets/manishiitg/camel-ai-biology

[9] https://huggingface.co/datasets/manishiitg/camel-ai-chemistry

[10] https://huggingface.co/datasets/meta-math/MetaMathQA/tree/main

[11] https://huggingface.co/datasets/manishiitg/aditi-syn-v2

[12] https://raw.githubusercontent.com/bsantraigi/tensorflow-seq2seq-hindi/master/data/Hindi%20-%20Word%20Transliteration%20Pairs%201.txt  
