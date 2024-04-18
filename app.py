import streamlit as st
from RPS_game import check_outcome
from RPSbot import RPSbot_chat
import pandas as pd

#print(emoji.emojize(":raised_fist:"))
#print(emoji.emojize(":victory_hand:"))
#print(emoji.emojize(":raised_hand:"))

st.markdown("# Rock Paper Sciscors bot 🤖")

if "game_history" not in st.session_state:
    st.session_state.game_history = {"You": 0, "RPSbot": 0, "Tie": 0}

if "messages" not in st.session_state:
    st.session_state.messages = []

col_1, col_2 = st.columns(2)

container = col_1.container(border=True, height=350)
container_2 = col_1.container(border=False, height=100)
container_3 = col_2.container(border=True, height=400)

for message in st.session_state.messages:
    with container.chat_message(message["role"]):
        container.markdown(message["content"])

if prompt := container_2.chat_input():
    # Display user message in chat message container
    with container.chat_message("user"):
        container.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

play = str(prompt).upper()
if play in ['R', 'P', 'S']:
    bot_play = RPSbot_chat(play)
    resp = f"{bot_play}, {check_outcome(play, bot_play, st.session_state.game_history)}"
elif play == 'STATS':
    hist = st.session_state.game_history
    games_played = hist["You"] + hist["RPSbot"] + hist["Tie"]
    if games_played == 0:
        resp = "You haven't played any games yet. [R]ock, [P]aper :raised_hand:, [S]cissors?"
    else:
        resp = f"Your win rate is {round(100* st.session_state.game_history["You"] / games_played,1)}%"
else:
    resp = "[R]ock✊, [P]aper✋, [S]cissors✌?"

print(st.session_state.game_history)

response = resp
# Display assistant response in chat message container
with container.chat_message("assistant"):
    container.markdown(response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})


chart_data = pd.DataFrame.from_dict(st.session_state.game_history, orient='index')
container_3.bar_chart(chart_data, use_container_width=True, color=['#3399ff'])

st.text("Type 'stats' to calculate you win rate.")