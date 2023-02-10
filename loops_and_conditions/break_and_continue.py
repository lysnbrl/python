course_title = "Curso Profesional de Python"

for char in course_title:
    if char == " ":
        break
    
    print(char)

for char in course_title:
    if char == " ":
        continue

    print(char)