# Table of Contents
[Overview](#overview)<br>
[List of Programs](#List)<br>
&nbsp;&nbsp;&nbsp;&nbsp;[Games](#List_Game)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GuessTheNumber.py](#List_Game_GuessTheNumber)

<a name="overview"></a>
# Overview
Here, I try to create simple python program, but overcomlicate things. <br> The general rule is: <br>
- Some elements of output in terminal should be colorful.
- There should be heavy implementation of fail-safe practice, like error handeling.
- <code> Ctrl + C </code> should never crash the program. Termination must be done safely.
- One program should be done and dusted in one file only

<a name="List"></a>
# List of Programs
<a name="List_Game"></a>
## Game
<a name="List_Game_GuessTheNumber"></a>
<b>GuessTheNumber.py</b> - Computer thinks of the number, you have to guess it.

<a name="Mannual"></a>
# Operational Mannual
<a name="Mannual_GuessTheNumber"></a>
### GuessTheNumber.
<code>python ./GuessTheNumber.py</code><br>
<code>python3 ./GuessTheNumber.py</code>
<br>

You are offered to enter lower limit and upper limit. Lower limit is minimum value computer can think of, and Higher limit is the maximim value computer can think of. Upper limit cannot be less than or equal to lower limit. Then you have to enter your guessed number. Your guess cannot be less than Lower limit and it cannot be more than Upper limit. Next, you will enter the number of guesses. Any value less than or equal to 0 will be considered as infinite guess.<br>
If your guess is less than computer's number, computer will say "More than that". If your guess is more than computer's number, computer will say more than that. otherwise, whatever exception the universe may bring (like if your guess exatly matches the computer's number), you will get Bingo! with number of trials you took to get here.<br>
Then, new game will restart. The game will run for infinitely long time. Just press <code> Ctrl + C </code> while cursor focus on terminal screen to quite out of game. If you want to play the game again with different Lower limit, Upper limit, or number of guess allowed, you need to quite the game by pressing <code> Ctrl + C </code> in your keyboard and re-run the program again.<br>
#### Requirement
- Python 3 or more
- ANSI Color supported Terminal. [Windows Terminal, Almost all GUI Terminal application in GNU/Linux]