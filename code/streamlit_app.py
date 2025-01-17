{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c50f3e4e-a55d-49f5-9f85-086722df83e7",
   "metadata": {},
   "outputs": [],
   "source": [
    import streamlit as st
    import pickle
    
    st.title('Which author do you write like?')
    page = st.sidebar.selectbox
      'Select a page:'
        ('About', 'Make a prediction')
    
    if page == 'About':
        st.write('here is my model')
        st.write('get in touch with me at:')
    
    if page == 'Make a prediction':
        st.write('''Edgar Allen Poe and Jane Austen: both authors. Which one do YOU write like?''')
    
        with open('models/author_pipe.pkl', mode='rb') as pickle_in:\n
            pipe = pickle.load(pickle_in)\n
    
        user_text = st.text_input('Please input some text:',\n
            value='quoth the raven...nevermore')\n,
    
        predicted_author = pipe.predict([user_text])[0]\n,
    
        st.write(f'You write like: {predicted_author}')
   ]
  },
  {
   "cell_type": "code",
   "execution_count":1,
   "id": "9ce8be1e-88d6-47a6-b8f7-862877135bea",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
