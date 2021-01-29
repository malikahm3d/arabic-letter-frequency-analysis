# arabic-letter-frequency-analysis
Arabic letter frequency analysis of more than 4.5 million letters.

This project is part of the cryptography course.

It is a python program to take a txt file and read it, first by line, then by word, then by character. If a character is valid, it is then added to a dictionary,
where the key is the letter, and the value is the times it is repeated. Finally, the results are printed out.
The data set I used is a large collection of Arabic articles from three major news publications, separated into seven categories.
I used the files in the tech category and ran a command prompt code to copy all the files into one that the python program reads.
cmd code, inside the tech folder: cp *.txt all_tech_files.txt
Dataset source: https://data.mendeley.com/datasets/57zpx667y9/2
