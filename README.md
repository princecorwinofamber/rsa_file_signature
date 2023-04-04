### Homework 1 by Andrey Kovalevskiy


How to run: ensure that you have python of version 3.6 or later installed.

To generate a new RSA key pair, use the command
```bash
python3 generate_key_pair.py
```

To sign a file, use the command
```bash
python3 sign.py
```
Enter the name of the file you want to sign and the private key that you have generated earlier when prompted to do so.  
The signature would be written into a separate file that has the name of the file being signed plus ".signature" suffix.


To verify the publisher of a file, use the command
```bash
python3 verify.py
```
Enter the name of the file, which signature you want to verify and the private key that you have generated earlier when prompted to do so.
Remember to keep the signature file in the working directory.


For the homework, file "helloworld.pdf" was signed with public key   665314570652039178871243337174761845499898889734205829691405516645816218347103674150103451169759193448620631243305065819385569105262915748792894176313003, 8560223826249753024122944739661332459710535133522597771486713891988753638060213655092336969324811377555196200914465949749822546062929610192966237071047103   and private key   1796373886576545096406393444283582679299164979424234592881226539687271799550011148438113460838260042405248995130486003618863774528736038371741110433444515, 8560223826249753024122944739661332459710535133522597771486713891988753638060213655092336969324811377555196200914465949749822546062929610192966237071047103  

Its signature is in the file "helloworld.pdf.signature".
