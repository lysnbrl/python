first_name = "Jade"
middle_name = "Navarro"

full_name1 = first_name + " " + middle_name + " " +  "Pérez" + "."
print(full_name1)

full_name2 = "Mx. %s %s %s." %(first_name, middle_name, "Pérez")
print(full_name2)

full_name3 = "Mx. {} {} {}.".format(first_name, middle_name, "Pérez")
print(full_name3)

full_name4 = "Mx. {first} {middle} {last}.".format(
    first = first_name, 
    middle = middle_name, 
    last = "Pérez"
)
print(full_name4)

full_name5 = f"Mx. {first_name} {middle_name} {'Pérez'}, {23}, {10 * 10}."
print(full_name5)