<h1>Caesar's cipher in Python</h1>


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Caesar_cipher_left_shift_of_3.svg/2560px-Caesar_cipher_left_shift_of_3.svg.png" width="500" class="center">

 <i>"In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or
 Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of 
 substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number 
 of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E 
 would become B, and so on. The method is named after Julius Caesar, who used it in his private
  correspondence."</i> - Wikipedia

  See more: https://en.wikipedia.org/wiki/Caesar_cipher

<h2>Files:</h2>

 ````main.py```` asks for user input (string to encrypt) and a shift key (number), then returns the encrypted message to the user.
 
 ````caesar_cipher.py```` is the encryption function.
 
 ````tests.py```` makes sure that the encryption function works properly.
 
 
<h2>The algorithm:</h2> 

Each character is translated to a number, a=0, b=1, c=2, d=3... z=25. The caesar cipher encryption function, e(x), x being the character we are trying to encrypt.

<img src="http://practicalcryptography.com/media/latex/bdd325f4306cf573601de60e4e175dfbe7acbb14-11pt.png" class="center">


This encryption program currently supports uppercase, lowercase, spaces and numbers.
