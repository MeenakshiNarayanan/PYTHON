arr = [11,22,33,11,44,55]
finalarr = [ ]
for i in arr:
    if i not in finalarr:
        finalarr.append(i)
print(finalarr)
