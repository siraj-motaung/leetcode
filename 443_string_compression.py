
counter = 1
results = []
chars = ["a", "a","a","a","a","a","a","a","a","a","a","a","a", "a", "b","b","a","a","a","a","a","a","a","a","a","a","a","a"]

lp = 0

for i in range(1, len(chars)):
    if chars[lp] == chars[i]:
        counter+=1
    else:
        results.append(chars[lp])
        if counter > 1:
            for n in str(counter):
                results.append(n)
        lp = i
        counter = 1

results.append(chars[lp])
if counter > 1:
    for n in str(counter):
        results.append(n)

print(results)
