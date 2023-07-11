# ●	The maximum size of a class is 30
# ●	There needs to be a minimum of 2 classes
# ●	The distribution of each class should be as even as possible. 
# ●	We want to hire as little people as possible - so where possible focus on bigger classes, and less of them!

import math

def class_allocation(number_of_students):
    classes_dictionary = {}

    if number_of_students <= 30:
        no_of_classes = 1
        more_than_one = "" # This ensures the grammar is correct if it is one class (i.e. 1 class not 1 classes)
        classes_dictionary["Class 1"] = number_of_students
    else:
        no_of_classes = math.ceil(number_of_students/30)
        more_than_one = "es" # This ensures the grammar is correct if it is more than one class (i.e. 2 classes not 2 class)
        class_numbers = [number_of_students // no_of_classes + (1 if x < number_of_students % no_of_classes else 0) for x in range (no_of_classes)]

        i = 1
        while i < len(class_numbers):
            classes_dictionary[f"Class {i}"] = class_numbers[i-1]
            i +=1

    print(f"Proposed Allocation: {no_of_classes} class{more_than_one}")
    print(classes_dictionary)

    return classes_dictionary

given_number=int(input("How many students are there?"))
class_allocation(given_number)