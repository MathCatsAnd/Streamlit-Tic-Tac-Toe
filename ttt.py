'A game of tic-tac-toe'

import streamlit as st
import numpy as np
import gameboard as sg

st.title('Tic Tac Toe')

def reset_game():
    st.session_state.victory = 0
    st.session_state.game = sg.DEFAULT(3,3)
st.button('Reset game', on_click=reset_game)

def check_win(board):
    # Check rows
    for i in range(3):
        if all(board[i][j]['player'] == 1 for j in range(3)):
            return 1
        if all(board[i][j]['player'] == 2 for j in range(3)):
            return 2
    # Check columns
    for j in range(3):
        if all(board[i][j]['player'] == 1 for i in range(3)):
            return 1
        if all(board[i][j]['player'] == 2 for i in range(3)):
            return 2
    # Check diagonals
    if all(board[i][i]['player'] == 1 for i in range(3)):
        return 1
    if all(board[i][i]['player'] == 2 for i in range(3)):
        return 2
    if all(board[i][2-i]['player'] == 1 for i in range(3)):
        return 1
    if all(board[i][2-i]['player'] == 2 for i in range(3)):
        return 2
    if all(board[i][j]['player'] != 0 for i in range(3) for j in range(3)):
        return -1
    return 0

def initialize():
    if 'color1' not in st.session_state:
        st.session_state.color1 = '#3A5683'
        st.session_state.alpha1 = 255
    if 'color2' not in st.session_state:
        st.session_state.color2 = '#73956F'
        st.session_state.alpha2 = 255
    if 'game' not in st.session_state:
        st.session_state.player1 = 'Player 1'
        st.session_state.player2 = 'Player 2'
        st.session_state.game = sg.DEFAULT(3,3)
        st.session_state.victory = 0

initialize()

if st.session_state.player1 == '':
    st.session_state.player1 = 'Player 1'
if st.session_state.player2 == '':
    st.session_state.player2 = 'Player 2'

color1 = st.session_state.color1
color2 = st.session_state.color2

with st.sidebar:
    st.header("Player Settings")

    def reset_colors():
        del st.session_state.color1
        del st.session_state.color2
        del st.session_state.alpha1
        del st.session_state.alpha2
    st.button('reset colors',on_click = reset_colors)

    # Set player info

    player1 = st.text_input('Player 1', key='player1')
    color1 = st.color_picker('❄️ Player 1 Color', key='color1')
    alpha1 = st.slider("Player 1 Alpha", 30, 255, key='alpha1')
    st.write('---')
    player2 = st.text_input('Player 2', key='player2')
    color2 = st.color_picker('🎈 Player 2 Color', key='color2')
    alpha2 = st.slider("Player 2 Alpha", 30, 255, key='alpha2')

    color1 = color1+f'{alpha1:02x}'
    color1 = color1.upper()

    color2 = color2+f'{alpha2:02x}'
    color2 = color2.upper()

    players = {player1:color1,player2:color2}

st.session_state.victory = check_win(st.session_state.game)

if st.session_state.victory != 0:
    for i in range(3):
        for j in range(3):
            st.session_state.game[i][j]['enabled'] = False

if st.session_state.victory == 1:
    st.snow()
if st.session_state.victory == 2:
    st.balloons()
if st.session_state.victory == -1:
    st.success('It\'s a tie! Please click reset to play again.')

sg.gameboard(3,3, players, board_state = st.session_state.game,  key='game')
