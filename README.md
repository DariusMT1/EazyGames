# EazyGames
# README

## Overview
This repository contains three classic games implemented in Python: Tic-Tac-Toe, Blackjack, and Snake. Each game is designed to be run from the command line and provides a simple, interactive experience.

## Table of Contents
Tic-Tac-Toe
Blackjack
Snake
Requirements
How to Run

&nbsp;
# Tic-Tac-Toe

## Description 
Tic-Tac-Toe is a two-player game where players take turns marking a space in a 3x3 grid with either an "X" or an "O". The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game. If all nine squares are filled and no player has three in a row, the game is a draw.

## Features
Two-player game
Simple text-based interface
Randomly removes three moves if the game is a draw

## How to Play
Run the script.
Players take turns entering a position (1-9) to place their mark.
The game will announce the winner or if the game is a draw.

## Code
The code for Tic-Tac-Toe is located in the tictactoe.py file.

&nbsp;
# Blackjack

## Description
Blackjack is a popular card game where the goal is to have a hand value as close to 21 as possible without going over. Players compete against the dealer.

## Features
Single-player game against the dealer
Simple text-based interface
Basic rules of Blackjack

## How to Play
Run the script.
Follow the prompts to hit or stand.
The game will announce the winner based on the hand values.

## Code
The code for Blackjack is located in the blackjack.py file.

&nbsp;
# Snake

## Description
Snake is a classic arcade game where the player controls a snake that grows in length as it eats food. The game ends if the snake runs into the screen border or itself.

## Features
Single-player game
Simple text-based interface using the curses library
Randomly placed food

## How to Play
Run the script.
Use the arrow keys to control the snake.
The game ends if the snake runs into the border or itself.

## Code
The code for Snake is located in the snake.py file.

&nbsp;
# Requirements
Python 3.x
curses library (for Snake game) <br />
How to Run <br />
Clone the repository: <br />

Sh <br />
Apply code <br />
Insert in terminal <br />

git clone https://github.com/DariusMT!/EazyGames.git <br />
cd EazyGames <br />
Run the desired game: <br />

Tic-Tac-Toe:

Sh <br />
Apply code <br />
Insert in terminal <br />

python tictactoe.py <br />

Blackjack: 

Sh <br />
Apply code <br />
Insert in terminal <br />

python blackjack.py <br />

Snake:

Sh <br />
Apply code <br />
Insert in terminal <br />

python snake.py <br />

&nbsp;
# Notes
Ensure you have the curses library installed for the Snake game. This library is typically included with Python on Unix-based systems. For Windows, you may need to install a compatible version.
The games are designed to be run from the command line.
Enjoy playing these classic games! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
