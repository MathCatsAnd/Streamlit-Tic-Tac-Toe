import streamlit as st
import plotly.graph_objects as go
import numpy as np
import asyncio

st.title('Tic Tac Toe')
def reset_game():
    del st.session_state.game
    del st.session_state.player
    del st.session_state.victory
st.button('reset game', on_click=reset_game)

def initialize():
    if 'color1' not in st.session_state:
        st.session_state.color1 = '#3A5683'

    if 'color2' not in st.session_state:
        st.session_state.color2 = '#73956F'

    if 'game' not in st.session_state:
        st.session_state.game = [[0 for row in range(3)] for col in range(3)]
        st.session_state.player = 1
        st.session_state.victory = 0
    return
initialize()

game = st.session_state.game
player = st.session_state.player
victory = st.session_state.victory
color1 = st.session_state.color1
color2 = st.session_state.color2

with st.sidebar:
    st.header("Settings Panel")

    def reset_colors():
        del st.session_state.color1
        del st.session_state.color2
    st.button('reset colors',on_click=reset_colors)

    color1 = st.color_picker('❄️ Player 1 Color', value = color1)
    color2 = st.color_picker('🎈 Player 2 Color', value = color2)
    st.session_state.color1 = color1
    st.session_state.color2 = color2

    color = {1:color1,-1:color2,0:'grey'}

if st.session_state.victory != 0:
    if st.session_state.victory > 1:
        st.success('It\'s a tie! Please click reset to play again.')
    else:
        st.success('Player '+ str(victory%3) + ' won! Please click reset to play again.')
        if st.session_state.victory == 1:
            st.snow()
        else: # victory == -1
            st.balloons()
else:
    st.info('It\'s player ' + str(player%3) + '\'s turn. Choose your move.')

def switch_player():
    st.session_state.player = player*-1

def play(i,j,player):
    if game[i][j] == 0:
        game[i][j] = player
        switch_player()
        st.session_state.game = game
        check_win(i,j,player)
    else:
        st.warning('That spot is already filled.')

def check_win(i,j,player):
    #Check victory by row
    if game[(i+1)%3][j] == player and game[(i+2)%3][j] == player:
        st.session_state.victory = player
        return
    #Check victory by column
    if game[i][(j+1)%3] == player and game[i][(j+2)%3] == player:
        st.session_state.victory = player
        return
    #Check victory by diagonal
    if (i+j)%2 == 0:
        #Check anti-diagonal
        if i != j or (i == 1 and j == 1):
            if game[(i+1)%3][(j-1)%3] == player and game[(i+2)%3][(j-2)%3] == player:
                st.session_state.victory = player
                return
        #Check (main) diagonal
        if i == j:
            if game[(i+1)%3][(j+1)%3] == player and game[(i+2)%3][(j+2)%3] == player:
                st.session_state.victory = player
                return
    if np.count_nonzero(np.array(game)) == 9:
        st.session_state.victory = 2
        return
    return

board = st.expander("Button Controls: Click to play",expanded=True)
with board:
    cols = st.columns(5)

    for i in range(3):
        with cols[i+1]:
            for j in range(2,-1,-1):
                st.button(f'({i},{j})',
                          disabled = bool(game[i][j]) or bool(victory), 
                          on_click = play, args=(i,j,player), key=str(i)+str(j))

x=[]
y=[]
z=[]
size=[]
for i in range(3):
    for j in range(3):
        if game[i][j] != 0:
            x.append(i)
            y.append(j)
            z.append(color[game[i][j]])
            size.append(75)
        else:
            x.append(i)
            y.append(j)
            z.append(0)
            size.append(10)


board_figure = go.Figure(data=[go.Scatter(
    x=x, y=y,
    mode='markers',
    marker=dict(
        color=z,
        opacity=.6,
        size=75,
    )
)])
board_figure.update_layout(height=500, width=500)
board_figure.update_xaxes(tickvals=[.5,1.5], range=[-.4,2.4], zeroline=False)
board_figure.update_yaxes(tickvals=[.5,1.5], range=[-.4,2.4], zeroline=False)

st.plotly_chart(board_figure)

    