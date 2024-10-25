# Substitution Cipher

Substitution Ciphers are one of the most well-known encryption methods around. 

The concept is simple: Generate a Ciphertext Alphabet using a keyword by appending the keyword's letters at the front of the alphabet like so:

> e.g. Keyword is `ZEBRAS`
> 
> Normal Alphabet: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
> 
> Ciphertext Alphabet: `ZEBRASCDFGHIJKLMNOPQTUVWXY`

Then, generate the ciphertext by matching the letters of the normal alphabet to the letters in the Ciphertext Alphabet. 

> e.g. Using the above Ciphertext Alphabet
> 
> Plain text: `Is this the real life?`
> 
> Ciper text: `FP QDFP QDA OAZI IFSA?`

For more info, visit [Wikipedia](https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution).

## Developer's Reflections

The first cipher I tried to make was a Caesar Cipher, and back then I tried it using a wonky method which involved using ordinals.

But one day I suddenly realised I was making things far more complicated that it had to be, and that I could just use list position to encode and decode the text, and thus this script was born. 
