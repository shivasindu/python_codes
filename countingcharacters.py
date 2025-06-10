ex = 'pahalgam'
result = {}
# Simple way without using collections
for ch in ex:
    if ch in result:
        result[ch] += 1
    else:
        result[ch] = 1
# Printing characters with more than one repetition
for ch in result:
    if result[ch] > 1:
        print(ch, '=', result[ch])
