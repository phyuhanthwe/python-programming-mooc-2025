# Write your solution here
def add_student(students, name):
    if name not in students:
        students[name] = []
    return students

def add_course(students, name, course:tuple):
    course_name_to_add = course[0]
    course_point_to_add = course[1]
    course_exists = False

    for existing_course_name, existing_point  in students[name]:
        if existing_course_name == course_name_to_add:
            if course_point_to_add > existing_point:
                students[name] = [course]
                course_exists = True
                break
            else: 
                course_exists = True
                break
    if not course_exists and course_point_to_add > 0:
        students[name].append(course)
    return students

def print_student(students, name):
    if name not in list(students.keys()):
        print(f"{name}: no such person in the database")
    else:
        courses = students[name]
        if not courses:
            print(f"{name}: \n no completed courses")
            return

        print(f"{name}:")
        print(f" {len(courses)} completed courses:")
        total_grade_points = 0
        for course_name, point in courses:
            print(f"  {course_name} {point}")  
            total_grade_points += point 

        if total_grade_points > 0: 
            average_grade = total_grade_points / len(courses)
            print(f" average grade {round(average_grade, 2)}")

def summary(students):
    best_point = {'point': 0, 'name': None}
    num_students = len(students)
    print(f"students {num_students}")

    most_completed = 0
    most_completed_name = None
    for name, course in students.items():
        num_course = len([c for c in course if c[1] > 0])
        if num_course > most_completed:
            most_completed = num_course
            most_completed_name = name
        
        total_grade_points = 0
        for course_name, point in course:
            # print(f"  {course_name} {point}")  
            total_grade_points += point 

        if total_grade_points > 0: 
            average_grade = total_grade_points / len(course)
            if average_grade > best_point['point']:
                best_point['point'] = average_grade
                best_point['name'] = name

    print(f"most courses completed {most_completed} {most_completed_name}")
    print(f"best average grade {round(best_point['point'],2)} {best_point['name']}")

if __name__=="__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
    summary(students)
