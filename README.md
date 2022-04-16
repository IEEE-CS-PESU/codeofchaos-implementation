# Writeup & resources to implement the Code of Chaos event for AT '22
## It's recommended that this repo be made public after the event to let the losing teams know where they went wrong

Sub-games :
- Introduction to Bhai-Lang (unassigned) [PENDING]
- Clash of Code (assigned to Srividya Prasad) [DONE]
- Memory tokens (assigned to Kohav Dey) [PENDING]
- Bug relay (assigned to Sriram Radhakrishna) [PENDING]

Supporting resources :
- Power cards (assigned to Manisha Reddy) [PENDING]
- Codinero integration into the game (unassigned) [PENDING]

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
General notes :

Introduction to Bhai-Lang  (and maybe BrainF*ck)
Provide conditional and loop exercises to be executed in bhai lang
These programs must have subtle cases where competitors will be likely to make silly mistakes. E.g. simulate a complex finitevstate machine 
https://github.com/DulLabs/bhai-lang

----------------------------------------------------------------------------------------------------------------------------------------------------------
a series of games based on code 

https://www.codingame.com/multiplayer/clashofcode

Clash of Code is a 5 min coding game with a global leaderboard. Club can create its own private clash for the teams.

Level 1 - Write the code and solve the puzzle in the least amount of time.
Level 2 - Solve the puzzle with the shortest code as fast as possible.
Level 3 - Reverse coding(only output given) + shortest code + fastest
Essentially a coding tournament. 2-3 games in each level.

When they open any game they'll get a random puzzle that we have no control over. So, we could alternatively use a platform like Kahoot to replicate the concept but with our own puzzles.

Make announcements for top teams and distribute goodies after every game.
----------------------------------------------------------------------------------------------------------------------------------------------------------

Memory Tokens (changes needed)

- The classic 5x5 tile game with 12 pairs of images +1. If u match a pair of images, u get the image as an NFT which u can save in your wallet.
- They will have roughly 30 seconds to solve this game. Now by example, if they get 3 pairs of images, they have to decensor the rest 9 images. So more tiles a team gets in those 30 seconds, the fewer images they have to decensor in the second part of this level. Moreover, each image will carry a token value of let’s say 2 IEEE CS tokens. Then the number of images they get in the tile game will be added to the wallet.
    -    Coming to the second part, all the images will be modified a lot via image processing which they have to reverse and get the original image. This all will be done in a stipulated time. The tokens would be awarded on the extent of which the reversed image looks similar to the original.

----------------------------------------------------------------------------------------------------------------------------------------------------------

Bug Relay
 
This event will be the final stage of the event where all teams have to complete the previous three games to participate.

Programs will be provided to each team where one member will have to debug the code at a time in relay format till all bugs are resolved. All provided programs will have the same number of bugs of moderate resolution difficulty.

The first team to get the program running gets a point. First to three points wins.

In case three pointers turn out to be an unlikely scenario, the most points wins.

In case all the teams get totally stuck like they did in certain stages of init(), points will be awarded at the end of a timer based on how many bugs they correctly identified.

If none of the above scenarios occurred, god help us all.

----------------------------------------------------------------------------------------------------------------------------------------------------------

Notes on supporting resources :

Coins are awarded for each level/sub-level which can be redeemed in ethereum at the end of the event as the cash prize or be used to buy cards that have effects on other teams.

Cards :

A wheel must be spun to decide which card the buyer gets

The wheel is spun by any team that completes a sub-game before the allocated time.

They can be used to ...

stop a specific team from working for N minutes

Socrates’ Stars - wheel spinner chooses a team to be made a pauper where the defendant & accuser make their cases with minute long speeches followed by a vote from all the other teams to determine the verdict (if the defendant wins, the accuser suffers the same verdict)

stop a random team from working for N minutes

confine a team to a slow & buggy computer with a broken keyboard for N minutes

Diogenes’ Dilemma I/II - loot a specific/random team of N% of their coins (another wheel can be spun to decide N)

get any specific team out of a confinement (can be used by a team currently in confinement)

Russian Revolution - redistribute all teams’ wealth equally among all the teams (very small probability on the wheel, can’t be used in the last game)

The American Dream - counter card for the previous card which should be spun for within 5 minutes of a Russian Revolution (teams can pool in coins for this)

a clue coupon that can be used at any point for more than necessary help from the mentors

problem giveaway card

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////







