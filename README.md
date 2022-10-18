# Streamlit-Tic-Tac-Toe
Tic-Tac-Toe implemented in Streamlit

I built this to explore Streamlit's session state functionality. I plan to improve it further and possibly make it into a tutorial.

Known Issues:
1. If color is reset immediately after selecting a new color, then that new color will not reset. If any other button is clicked, or if the color picker is selected again without changing the color, then the color reset button will function correctly.
2. If color is changed while the game is in a winning state, the celebratory animation will repeat with each color seleciton.

Planned Improvements:
1. Make the game board interactive instead of relying on external buttons.
2. Shut down zoom control on the game board so accidental click and drag doesn't misalign the board.
3. Add a computer opponent.
4. Make current player more obvious.
