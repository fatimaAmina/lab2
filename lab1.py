students = {"ali": 20,
            "ahmed":22,
            "sara":19,
            "noor":23,
            "omar":21}

print ("students data: ")
for name ,age in students.items():
    print(name,":", age)

avg = sum(students.values())/len(students)
print("\naverage age is: ", avg)

oldest = max(students, key=students.get)
youngest = min(students, key= students.get)

print("oldest students is: ", oldest, "-", students[oldest])

print("youngest students is: ", youngest, "-", students[youngest])

print("\nstudents older than average: ")
for name, age in students.items():
    if age>avg:
        print(name,age)

