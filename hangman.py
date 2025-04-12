# import random
# import string
# from words import handyman_words


# def get_valid_word(handyman_words):
#     word = random.choice(handyman_words)
#     while "-" in word or " "in word:
#         word = random.choice(handyman_words)
#     return word.upper()

# def hangman():
#     word = get_valid_word(handyman_words)
#     word_letters = set(word) # letters in the word
#     alphabet = set(string.ascii_uppercase)
#     used_letters = set()


#     lives = 4


#     while len(word_letters)> 0 and lives > 0:
            
            
#             print(f"You have {lives} left and you have used these letters:",' '.join(used_letters))

#             word_list = [letter if letter in used_letters else '-' for letter in word]
#             print('current word:',' '.join(word_list))
#             user_letters = input("Enter your letter").upper()
#             if user_letters in alphabet - used_letters:
#                 used_letters.add(user_letters)
#                 if user_letters in word_letters:
#                     word_letters.remove(user_letters)
#                 else:
#                      lives -=1
#                      print("letter is not in the word")

#             elif user_letters in used_letters:
#                 print("you have already used this letter please try again")
    
#             else:
#                  print("Invalid character please try again")


#     if lives == 0:
#          print("you died")
#     else:
#          print("you guessed the word",word,"!!")


import streamlit as st
import random
import string
from words import handyman_words

if "initialized" not in st.session_state:
    st.session_state.word = random.choice(handyman_words)
    while "-" in st.session_state.word or " " in st.session_state.word:
        st.session_state.word = random.choice(handyman_words)
    st.session_state.word = st.session_state.word.upper()
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.used_letters = set()
    st.session_state.lives = 4
    st.session_state.initialized = True

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Hangman Game</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Guess the handyman word!</h3>", unsafe_allow_html=True)

while st.session_state.lives > 0 and len(st.session_state.word_letters) > 0:
    st.markdown(f"<p style='text-align: center; font-size: 20px;'>Lives Remaining: <strong>{st.session_state.lives}</strong></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 20px;'>Used Letters: {' '.join(sorted(st.session_state.used_letters))}</p>", unsafe_allow_html=True)
    current_word = " ".join([letter if letter in st.session_state.used_letters else "_" for letter in st.session_state.word])
    st.markdown(f"<p style='text-align: center; font-size: 24px;'>{current_word}</p>", unsafe_allow_html=True)
    
    guess = st.text_input("Enter a letter", key="guess_input")
    if st.button("Submit Guess"):
        guess = guess.upper()
        if guess and guess in string.ascii_uppercase:
            if guess not in st.session_state.used_letters:
                st.session_state.used_letters.add(guess)
                if guess in st.session_state.word_letters:
                    st.session_state.word_letters.remove(guess)
                    st.success("Good guess!")
                else:
                    st.session_state.lives -= 1
                    st.error("Incorrect guess!")
            else:
                st.warning("Letter already used.")
        else:
            st.error("Invalid input. Enter a single alphabet letter.")
        st.experimental_rerun()
    break

if st.session_state.lives == 0:
    st.error(f"You lost! The word was {st.session_state.word}.")
elif len(st.session_state.word_letters) == 0:
    st.success(f"You won! The word was {st.session_state.word}.")

if st.button("Play Again"):
    st.session_state.clear()
    st.experimental_rerun()
