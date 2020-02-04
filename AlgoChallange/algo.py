string1 = 'aaabbcdd'
string2 = 'abdbacade'
duplicates = []
for each_letter_S1 in string1:
    if each_letter_S1 in duplicates:
        continue #skip letters we have already found that match between the two strings
    for each_letter_S2 in string2:
        if each_letter_S1 == each_letter_S2:
            duplicates.append(each_letter_S1)
            break
for each_letter_S2 in string2:
    if each_letter_S2 in duplicates:
        continue
    else:
        print(f'{each_letter_S2} is the unique letter in string 2: {string2}')
        break