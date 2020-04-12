# Snatch Solver
This project initially started as a command line utility for my family and I
to check for solutions we missed after we finished a game of Snatch. Since
then, it has devloped into a small webapp to serve that same functionality,
but online.

Given a word , the service finds every word in the dictionary with a distinct
root and whose letters are a superset of that given word. For example,
submitting `test` would return `attest`, but **not** `tests`.
While the letters in `test` are a subset of those in `tests`, the two
words have the same root, i.e. `test`.

You can find the most recent deployment [here](snatch.nikoapps.com).

The dictionary currently being used was found
[here](https://drive.google.com/file/d/1oGDf1wjWp5RF_X9C7HoedhIWMh5uJs8s/view),
as recommended by
[this](https://boardgames.stackexchange.com/questions/38366/latest-collins-scrabble-words-list-in-text-file)
stack overflow post.


<br>

## Local Development
In order to run the webapp locally, run the following from the top level
directory:
<br>
``` docker-compose up```

This will build the local code and run it in a container at
```localhost:8000```. In addition, it will rebuild and update as you make
updates to the code, so you can see your changes live.

The app also has continuous deployment setup (TODO @John), so every time
changes are committed to master, the [deployed version](snatch.nikoapps.com)
should update.

<br>

## Snatch: the game that started all this
Snatch is a fun game that requires 2 or more players and set of letter tiles.
While we've found that scrabble tiles have a good distribution, we've also
had fun using bananagrams tiles.

#### Setup
- Begin by laying all letters flat in the middle of the table, facing down.

#### Gameplay
- All players are assigned a letter minimum. The default is 4, but you can
shift this to accomodate for players of different levels (a better player may
be given a minimum of 5, for example)
- Players can form words using letters that have been flipped over in the
middle, if the word they form is at least as long as their minimum.
- Players can also *steal* words from other players. In order to steal a
word, **at least** one letter must be added from the middle of the board. The
letters originally in the word being stolen must stay together in the new
word and must all be used, but may be rearranged. In addition, the new word
must have a different root meaning. Here is an example below.
  - Let's say Player one has the word `income`, and the letters in
  the middle are `b`, `s`, `h`, and `r`. Player 2 would like to steal income.
  - Player 2 is **not** allowed to turn `income` into `bins` and `chrome`.
  While this uses letters from the middle, adds letters, and makes words with
  new roots, you are not allowed to separate letters once they are in a word.
  - Player 2 is **not** allowed to turn `income` into `incomes`. Stolen words
  must change the *root meaning* of the word being stolen
  - Player 2 could, however, turn `income` into `combine` by adding the `b`
  from the middle and rearranging the letters.

#### Turns
- Snatch doesn't have turns like in other games.
- Anybody can call out a word when they see it. So if somebody wants to make
`cart` out of the middle, they say `cart` before somebody else uses the
letters. The same is true for stealing. To steal a word, you must say the
*new* word before anybody else. So to steal `income` by adding a `b`, you
would call out `combine`.
- If multiple players call out a word that uses the same letters from the
middle at the same time, they play rock paper scissors to decide who gets it.
- Flipping: players can turn letters over whenever they want, within reason.
We usually go with "flip letters over when most people feel like they need
more letters". If many people are obviously deep in thought, don't start
flipping letters, instead ask if they're ready.
- Disputes: if somebody tries to make a word that no one believes exists,
they must give a definition (can be a loose one) of what the word means. If
people still doubt it, you can look up the word online.

#### Scoring and winning
- The game is over when all letters have been used or all players agree to
end it, i.e. if nobody can steal any other words.
- Words are worth 1 point for the first "letter minimum" letters, and then 1
point for each additional lettter. For example, if a player with a 4 letter
minimum makes `combine`, they would get 1 point for the first 4 letters, and
then another 3 for the remaining letters, for a total of 4.
- The player with the most points wins!