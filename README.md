# Teaching ChatGPT to write Wordle in JavaScript

## Why I did it:

Because I had run into some problems getting ChatGPT to help me guess possible remaining words when playing Wordle once, I decided to try to play a game of it to see if it understood the rules. It seemed to, but then failed miserably at actually obeying them to make guesses (see the earliest parts of the transcript provided in this collection as index.html).

Anyway, so after a few exchanges, I just asked it if it could program a Wordle. It made a reasonable attempt to, but...
a. The code had several errors that prevented it from running... mainly missing declarations and conflicting IDs in the HTML that caused confusion with potential variable names in the JavaScript (which it often excluded, maybe because the HTML element with that ID existed already).
b. It didn't really play the way I expected the Wordle to play. It lacked an adequate UI, and results were being logged to the console, something most users wouldn't know to open up.

## What it showcases: