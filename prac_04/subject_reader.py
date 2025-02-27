"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


# def main():
#     data = load_data()
#     print(data)
#
#
# def load_data():
#     """Read data from file formatted like: subject,lecturer,number of students."""
#     input_file = open(FILENAME)
#     for line in input_file:
#         print(line)  # See what a line looks like
#         print(repr(line))  # See what a line really looks like
#         line = line.strip()  # Remove the \n
#         parts = line.split(',')  # Separate the data into its parts
#         print(parts)  # See what the parts look like (notice the integer is a string)
#         parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
#         print(parts)  # See if that worked
#         print("----------")
#     input_file.close()
#
#
# main()

def main():
    """Load subject data and display details."""
    subjects = load_data()
    display_subject_details(subjects)


def load_data():
    """Read data from file and return lists"""
    subjects = []
    with open(FILENAME, "r") as input_file:
        for line in input_file:
            line = line.strip()  # remove newline
            parts = line.split(",")  # split by comma
            parts[2] = int(parts[2])  # convert student number to an integer
            subjects.append(parts)  # store as a nested list
    return subjects


def display_subject_details(subjects):
    """display subject details"""
    for subject in subjects:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students")


main()
