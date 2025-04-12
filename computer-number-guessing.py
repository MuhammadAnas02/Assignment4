import streamlit as st
import random

st.markdown("""
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
""", unsafe_allow_html=True)

st.title("🤖 Computer Guesses Your Number")
difficulty = st.radio("Select Difficulty:", ("Easy", "Medium", "Hard"), key="difficulty")
max_number = 10 if difficulty == "Easy" else 50 if difficulty == "Medium" else 100

st.session_state.setdefault("game_won", False)
st.session_state.setdefault("max_number", max_number)
st.session_state.setdefault("low", 1)
st.session_state.setdefault("high", max_number)
st.session_state.setdefault("guess", random.randint(1, max_number))
st.session_state.setdefault("diff", difficulty)

if st.session_state.diff != difficulty:
    st.session_state.diff = difficulty
    st.session_state.max_number = max_number
    st.session_state.low = 1
    st.session_state.high = max_number
    st.session_state.guess = random.randint(1, max_number)
    st.session_state.game_won = False

if not st.session_state.game_won:
    st.write(f"Think of a number between 1 and {st.session_state.max_number}, and I'll try to guess it.")
    st.write(f"Is your number **{st.session_state.guess}**?")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Too High", key="too_high"):
            st.session_state.high = st.session_state.guess - 1
            if st.session_state.low <= st.session_state.high:
                st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            else:
                st.error("🚨 Hmm, it seems there's no number left. Did you make a mistake?")
            st.rerun()

    with col2:
        if st.button("Too Low", key="too_low"):
            st.session_state.low = st.session_state.guess + 1
            if st.session_state.low <= st.session_state.high:
                st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            else:
                st.error("🚨 Hmm, it seems there's no number left. Did you make a mistake?")
            st.rerun()

    with col3:
        if st.button("Correct", key="correct"):
            st.session_state.game_won = True
            st.rerun()

else:
    st.success(f"🎉 Yay! I guessed your number {st.session_state.guess} correctly!")
    st.balloons()
    if st.button("Play Again", key="play_again"):
        st.session_state.low = 1
        st.session_state.high = st.session_state.max_number
        st.session_state.guess = random.randint(1, st.session_state.max_number)
        st.session_state.game_won = False
        st.rerun()


st.markdown("---")
st.markdown("*Made with ❤️ using Streamlit*")
