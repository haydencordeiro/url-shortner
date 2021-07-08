cpgi=[6,10,5,10]
percent=0
pointer=0
for i in cpgi:
    if i>7:
        percent+=((i*7.4)+12)
    else:
        percent+=((i*7.1)+12)
    pointer+=i
    
print(percent/len(cpgi),"%")
print()
print(pointer/len(cpgi))