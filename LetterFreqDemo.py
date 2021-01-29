validChars = "اإأبجدهوزحطيكلمنسعفصقرشتثخذضظغؤءئآة"
#using a valid characters varible to check what the file reads against it. And only use what is read if it is valid.
  
countOfLetters = 0
#using this varible to count all the characters/letters and get the relative frequency

frequencyDictionary = dict()
#intilizing a collection (in this case, dictionary) to hold the letters (keys) and their respective count (value).

with open(r"all_tech_files.txt", encoding="utf8") as file:
#requires absloute path of the .txt file

#opening the file (more on the content of the file in the report)
#python would only accpet the full file path. Encoding is utf8 to read arabic characters
    for line in file:
    #loop through the file, line by line.
        Words = line.split(" ")
        #defning Words by splitting them at the occurance of a space
        for word in Words: 
            #looping through the Words
            Chars = list(word) 
            #breaking down the Words into lists of charatcers
            for c in Chars: 
            #looping throguh the list of charaters
                if c not in validChars:
                #if a character is not valid: ignore it
                    continue
                else:
                    countOfLetters += 1
                    #if it is valid: count it (to be used for the relative frequncy as the denominator).
                    if c in frequencyDictionary:
                        frequencyDictionary[c] += 1
                        #if it is valid && already exists in the dictionary: add to its count.
                    else:
                        frequencyDictionary[c] = 1
                        #if it valid && is not in the dictrionary: add it as a new item.

print(countOfLetters) #4 561 998 letters, which is sufficent and why I did not use all the files in the dataset.
print(f'{":":<2} {"Letter":<2} {":":<2} {"Frequency":<5} {":":<2} {"Relative frequency in the dataset":<5} {":":<2}')   
for k,v in frequencyDictionary.items():
    print(f'{":":<2} {k:^6} {":":<4} {v:<6} {":":>6} {round(((v/countOfLetters)*100),1):<6} {":":>1}')
#print out the results in a table-like structure.

file.close()