marks= [78, 85, 90, 67, 85, 92, 78]
#avg
avg= sum(marks)/ len(marks)
#high
high= max(marks)
#low
low= min(marks)
#above avg
above_avg= sum(1 for m in marks if m > avg)
#grade
grades= {"A":0, "B":0, "C":0, "Fail":0}
for m in marks:
    if m>=90:
        grades["A"] += 1
    elif m>= 75:
         grades["B"] += 1
    elif m>= 50:
         grades["C"] += 1
    else:
         grades["Fail"] +=1
print("Average Marks:", avg)
print("Highest Marks:", high)
print("Lowest Marks:", low)
print("Students Above Average:", above_avg)
print("Grade Distribution:", grades)
