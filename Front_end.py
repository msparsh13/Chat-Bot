import streamlit as st
from keras.models import load_model
import numpy as np

characters = list("abcdefghijklmnopqrstuvwxyz0123456789")
char2idx = { characters[x]:x+1 for x in range(0 , len(characters)) }
idx2char = { char2idx[x]:x for x in characters }

encoder_model = load_model(r"C:\Users\Sparsh Mahajan\OneDrive\Documents\c progams\.vscode\.vscode\backend\AutoCorrect\encoder (3).h5")
decoder_model = load_model(r"C:\Users\Sparsh Mahajan\OneDrive\Documents\c progams\.vscode\.vscode\backend\AutoCorrect\decoder (3).h5")

num_dec_tokens = 39 

max_dec_len = max([len(x) for x in df[1]])

count = len(characters)+1
symbols = [" " , "\n"]
for s in symbols:
    char2idx[s]=count
    idx2char[count]=s
    count+=1

def convt_word(word):
    l = [char2idx[w] for w in word ]
    return l

def word_correct(input_seq):
    states_value = encoder_model.predict(input_seq)
    target_word = np.zeros((1, 1, num_dec_tokens))
    target_word[0, 0, char2idx[' ']] = 1.
    stop_condition = False
    decoded_word = ''
    while not stop_condition:
        output_tokens, h = decoder_model.predict(
            [target_word] +[ states_value])
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = idx2char[sampled_token_index]
        decoded_sentence += sampled_char
        if (sampled_char == '/n' or len(decoded_word) > max_dec_len):
            stop_condition = True
        target_word = np.zeros((1, 1, num_dec_tokens))
        target_word[0, 0, sampled_token_index] = 1.
        states_value = [h]
    return decoded_word





def correct(word):
    x= convt_word(word)
    a=np.zeros([19, 38])
    for i , t in enumerate(x):
        a[i , t]=1
    return word_correct(a.reshape(1 , 19 , 38))


st.header("AutoCorrect")
word = st.text_area()
st.write(correct(word))