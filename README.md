
/// This project is a personal project completed by Qian Song, the two commiters are the same person with two accounts.

#Copyright (c) 2016 Qian Song

#License

This program is available under MIT licence, please see COPYING.
 
Qian_OSSProject_2016
#Mancala Game

#Game introduction:

Mancala is a two-player game in which players moves stones around a board, trying to capture as many as possible.
On a player's turn, he or she chooses one of the pits on his or her side of the board(not the mancala) and removes all of the stones from that pit. The player then places one stone in each pit, moving counterclockwise around the board, starting with the pit immediately next to the chosen pit, including his or her Mancala but not the opponent's mancala. If the player's last stone ends in an empty pit on his or her own side, the player captures all of the stones in the pit directly across the board from where the last stone was placed (the opponents stones are removed from the pit and placed in the player's Mancala) as well as the last stone placed(the one placed in the empty pit). The game ends when one player cannot move on his or her turn, at which time the other player captures all of the stones remaining on his or her side of the board.

#Languages

Python

html

javascript


#Major Task:
In this project, the major task is to write a program to determine the next move by implementing one or two appropriate algorithms. 

#Build and run instruction:

1  Python code:
Python 2.7 interpreter is needed to run the code. Create a folder and put the source code(mancala.py) in it. Start, go into the working directory, run the code by typing python mancala.py. 

$ python mancala.py

Then you will see the guide menu to choose a mode to play or to quit. 

Welcome to mancala!
Please choose:

1. Play with Player.

2. Play with Computer

3. Quit Game!


Choose  1 to play with another player, 2 to play with computer, 3 quit game. The plate (two arrays) will show in current state. Type the number of pit which you choose to move the stones(number of stones are shown by array elements) and the updated plate state will show on terminal, and the program will also prompt whose turn it is. 


2  Javascript and html code build and run instruction:

In order to run these, a browser is needed (chrome is recommended). Put source code (mancala.html and mancalaPVP.js) in a folder and open html file by the browser. The game webpage will show up, there will be a link of instructions on how to play the game and prompt button to start game.


