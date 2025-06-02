a = "hello"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for i in a:
    if i.isalpha():
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("vowels:", vowel_count, "consonants:", consonant_count)

