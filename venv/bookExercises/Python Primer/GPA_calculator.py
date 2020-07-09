
print ("Welcome to the GPA Calculator")
print("Please Enter all your letter Grades. One per Line")
print("Enter a blank line to signify the end")


points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+':3.33, 'B':3.0, 'B-':2.67, 'C+':2.33, 'C':2.0 , 'C-':1.67, 'D+':1.33 , 'D':1.0 ,'F':0.0}

num_courses = 0
total_points = 0
done = False

while not done:
    grade = input()    # Ask for User Input
    if grade == '':
        done = True   # if blank line detected
    elif grade not in points:
        print (f"Unknown grade {grade} being ignored")  # if grade is not in point's keys
    else:
        num_courses += 1
        total_points += points[grade]  # fetch GPA value belonging to grade key entered

if num_courses > 0:
    print("Your GPA is {0:.3}".format(total_points/num_courses))  # finally calculate the GPA

    