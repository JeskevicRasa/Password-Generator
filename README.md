# Password-Generator

This Python script generates random passwords in two different ways.
In the first part, it defines a create_password function that generates a random password of length 5 by combining characters from the 'letters' string and random digits.

In the second part, it creates a list called 'listas' that includes integers from 0 to 9 and ASCII values for characters in the range from 'A' to 'z'.
It then generates a random password of length 20 by choosing random elements from 'listas' and adding them to the password. If the chosen element is a digit (0-9), it's added as is; otherwise, if it corresponds to an ASCII value, the corresponding character is added to the password.

Finally, it prints both generated passwords.