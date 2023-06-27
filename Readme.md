# Table of Contents
[Overview](#overview)<br>
[List of Programs](#List)<br>
&nbsp;&nbsp;&nbsp;&nbsp;[Games](#List_Game)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GuessTheNumber](#List_Game_GuessTheNumber)<br>
&nbsp;&nbsp;&nbsp;&nbsp;[Utilities](#list_utilities)</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ANSIColors](#list_utl_ANSIColors)<br>
[Operational Mannual](#Mannual)<br>
&nbsp;&nbsp;&nbsp;&nbsp;[Games](#Mannual_Games)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GuessTheNumber](#Mannual_Games_GuessTheNumber)<br>
&nbsp;&nbsp;&nbsp;&nbsp;[Utilities](#Mannual_utilities)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ANSIColors](#Mannual_utils_ANSIColors)<br>

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
<a name="list_utilities"></a>
## Utilities
<a name="list_utl_ANSIColors"></a>
<b>ANSIColors.py</b> - All color codes to make terminal colorful.



<a name="Mannual"></a>
# Operational Mannual
<a name="Mannual_Games"></a>
## Games
<a name="Mannual_Games_GuessTheNumber"></a>
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

<a name="Mannual_utilities"></a>
## Utilities
<a name="Mannual_utils_ANSIColors"></a>
### ANSIColors
<code>python ./ANSIColors.py</code><br>
<code>python3 ./ANSIColors.py</code>
<br>
ANSI stands for American National Standards Institute. They have set up a standard for colorcodes in terminal screen like 46 is lime color and 126 is red color. Ofcourse no one can remember all those 256 colors. So, this simple script can print out color code in their respective color. The script also has the way it is implemented for python.
#### Requirement
- Python 3 or more
- ANSI Color supported Terminal. [Windows Terminal, Almost all GUI Terminal application in GNU/Linux]
