import streamlit as st
import random

st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        color: #ff6347;
        font-size: 2.5em;
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stNumberInput input {
        border: 2px solid #ccc;
        border-radius: 5px;
        padding: 5px;
    }
    .stRadio>div {
        display: flex;
        justify-content: center;
    }
    .stAlert {
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("🎉 Number Guessing Game")

difficulty = st.radio("Select Difficulty:", ("Easy", "Medium", "Hard"), key="difficulty_radio")
max_number = 10 if difficulty == "Easy" else 50 if difficulty == "Medium" else 100

# Initialize session state keys if they don't exist.
if "difficulty" not in st.session_state:
    st.session_state.difficulty = difficulty
    st.session_state.max_number = max_number
    st.session_state.random_number = random.randint(1, max_number)
    st.session_state.game_won = False
elif st.session_state.difficulty != difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.max_number = max_number
    st.session_state.random_number = random.randint(1, max_number)
    st.session_state.game_won = False

if "game_won" not in st.session_state:
    st.session_state.game_won = False

if not st.session_state.game_won:
    st.write(f"I'm thinking of a number between 1 and {st.session_state.max_number}. Can you guess it?")
    guess = st.number_input(
        "Enter your guess:",
        min_value=1,
        max_value=st.session_state.max_number,
        step=1,
        key="guess_input"
    )
    if st.button("Submit Guess", key="submit"):
        if guess < st.session_state.random_number:
            st.warning("📉 Too low! Try again.")
        elif guess > st.session_state.random_number:
            st.warning("📈 Too high! Try again.")
        else:
            st.session_state.game_won = True
            st.experimental_rerun()
else:
    st.success(f"🎊 Congratulations! You guessed the number {st.session_state.random_number} correctly!")
    st.balloons()
    if st.button("Play Again", key="play_again"):
        st.session_state.random_number = random.randint(1, st.session_state.max_number)
        st.session_state.game_won = False
        st.experimental_rerun()

st.markdown("---")
st.markdown("*Made with ❤️ using Streamlit*")
