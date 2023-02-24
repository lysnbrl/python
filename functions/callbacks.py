average = lambda *args : sum(args) / len(args)

approved = lambda grade : grade >= 7  

def display_message(average_function, approved_function, *args):
    average = average_function(*args)

    if approved_function(average):
        print(f"Congratulations, you passed the subject with {average}.")
    else:
        print("You failed the subject.")

display_message(average, approved, 8, 8, 9, 9, 10)