# Auto-Correct

## Overview 
AutoCorrect system based upon seq2seq model that is used to correct spelling of wrong words
### About Seq2Seq Model
Sequential2Sequential or seq2seq is machine learning model takes sequential input and gives sequential output 
It is based upon Encoder-Decoder Architecture 
It is used for phrase-based statistical machine translation (SMT)

### Why it is used:
Autocorrection is also need sequence of charaters and need to generate sequence of characters as output which is similar to Machine translation at character level

## Key Features 
* **1** **Deep Learning** Model is based upon seq2seq model which is used since autocorrection is comparable to concept of machine translation that is used to convert of language to other
* **2** **Natural Language Translation** NLP is used in it.

## Dependencies:
* Numpy
* Glob
* Tensorflow
* Streamlit

## Organisation of files
 ```
/project-root
||-- dataset
||-- AutoCorrect.ipynb
||-- Front_end.py
||--Encoder.h5
||-- Decoder.hs
||--README.md
```
- **Dataset** : Folder that has dataset of files used to create it
- **AutoCorrect.ipynb** : Notebook thata consist how the model has been created
- **Encoder.h5** and **Decoder.h5** : Encoder and Decoder models
