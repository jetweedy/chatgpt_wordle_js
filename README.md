# Teaching ChatGPT to write Wordle in JavaScript

Because I had run into some problems getting ChatGPT to help me guess possible remaining words when playing Wordle once, I decided to try to play a game of it to see if it understood the rules. It seemed to, but then failed miserably at actually obeying them to make guesses (see the earliest parts of the transcript provided in this collection as index.html).

Anyway, so after a few exchanges, I just asked it if it could program a Wordle. It made a reasonable attempt to, but...
* The code had several errors that prevented it from running... mainly missing declarations and conflicting IDs in the HTML that caused confusion with potential variable names in the JavaScript (which it often excluded, maybe because the HTML element with that ID existed already).
* It didn't really play the way I expected the Wordle to play. It lacked an adequate UI, and results were being logged to the console, something most users wouldn't know to open up.

Be interacting with it with pretty human speech, just addressing concerns with the code in a way that I might with a student in a JavaScript course, I was able to eventually coax a surprisingly well-functioning version of a Wordle game out of it. 

This was interesting on several levels:
* It was impressive to see just how much ChatGPT understood and retained in context as the conversation progressed.
* It was a fun exercise in describing an application at a human language level well enough that an AI could write what I wanted.
* It was an interesting challenge to format the raw copy-pasted text programmatically with some Python (included)
