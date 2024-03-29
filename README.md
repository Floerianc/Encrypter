# How to use this **shit**
## 1. Encryption.exe
This file creates another .txt file which stores the codes, that are **FUNDAMENTAL** for the decryption, don't delete this, do not edit anything and don't **PLEASE** don't move it out of the folder. Be aware that the Encryption.exe, the .txt and the Decryption.exe **HAVE** to be in the **EXACT SAME FOLDER** or else it will break my shit.

### Soooo... how does *this* encryption stuff work?

1. You enter a sentence, word or anything really, except numbers and special characters, this only works for normal characters thanks
2. It gives each unique character a unique ID, encrypts it by multiplying the ID by 16384 because I felt like it and then it encrypts it into Base64
3. It quickly decrypts the sentence, so you can actually see the encrypted and decrypted input at the end. Pretty simple
4. It creates a .txt file, which contains the unique ID of every single character in the message

## 2. Decryption.exe
This uses the .txt file to decrypt everything from the .txt file, thats why you shouldn't delete or edit it to decrypt it.

1. It loads each line from the .txt file
2. Decrypts the Codes from the .txt file into ascii and then divides the number by 16384
3. Converts the number into an Ascii-Character
4. Shows the Decrypted Text at the end.
