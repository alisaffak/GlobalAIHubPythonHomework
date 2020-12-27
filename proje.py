student_name = "Ali".upper()
student_surname = "Şaffak".upper()
all_courses = ["Calculus","Lineer Algebra","Computer Science","DSP","Embeded Systems"]
selected_courses = set()
student_grades = {}

def select_courses():
    j = 1
    for i in all_courses:
        print("{}-{}".format(j,i))
        j  +=1
    print("6-No course selection")
    print("Please select at least 3 courses. ")
    selected = input("Enter the course's number:")
    if selected == "1":
        selected_courses.add(all_courses[0])
    elif selected == "2":
        selected_courses.add(all_courses[1])
    elif selected == "3":
        selected_courses.add(all_courses[2])
    elif selected == "4":
        selected_courses.add(all_courses[3])
    elif selected == "5":
        selected_courses.add(all_courses[4])

    else:
        print("ınvalid input")

def exam():
    for i in selected_courses:
        print(i)

    select = input("choose the course you will take the exam: ")
    if select in selected_courses:
        midterm = input("Enter the midterm notes: ")
        final = input("Enter the final notes: ")
        project = input("Enter the project notes: ")
        student_grades["midterm"] = int(midterm)
        student_grades["final"] = int(final)
        student_grades["project"] = int(project)

    else:
        print("Invalid input")
        exam()

def calculate_notes():
    grade = student_grades["midterm"]*0.3 + student_grades["final"]*0.5 + student_grades["project"]*0.2

    if grade >= 90 :
        print("AA")
    elif 70 <= grade < 90 :
        print("BB")
    elif 50 <= grade < 70 :
        print("BB")
    elif 30 <= grade < 50 :
        print("BB")
    else:
        print("FF")
        print("You failed the lesson")

tries = 3
while (tries > 0):
    name = input("Please enter your name: ").upper()
    surname = input("Please enter your surname: ").upper()
    if name == student_name and surname == student_surname:
        print("WELCOME!")
        while len(selected_courses) < 3 :
            select_courses()
        exam()
        calculate_notes()


    elif name != student_name and surname == student_surname:
        tries -= 1
        print("Opps! You have last {} entries".format(tries))
    elif name == student_name and surname != student_surname:
        tries -= 1
        print("Opps! You have last {} entries".format(tries))
    elif name != student_name and surname != student_surname:
        tries -= 1
        print("Opps! You have last {} entries".format(tries))

    else:
        print("Please try again later!")
        break































