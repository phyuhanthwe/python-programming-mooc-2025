# Write your solution here
from functools import reduce

def grade_dis(total_point, exam_point):
    grade = 0
    if exam_point < 10:  
        grade = 0
    elif 0 <= total_point <= 14:
        grade = 0
    elif 15 <= total_point <= 17:
        grade = 1
    elif 18 <= total_point <= 20:
        grade = 2
    elif 21 <= total_point <= 23:
        grade = 3
    elif 24 <= total_point <= 27:
        grade = 4
    else:
        grade = 5
    return grade

def pass_percent(grade_lst):
    passing = sum(1 for grade in grade_lst if grade > 0)
    pass_percentage = (passing / len(grade_lst)) * 100
    return pass_percentage

def grade_print(grade_lst):
    grade_counts = [grade_lst.count(i) for i in range(6)]
    output = "Grade distribution:\n"
    for i in range(5, -1, -1):
        star = "*" * grade_counts[i]
        output += f"{i}: {star}\n"
    return output

def main():
    exam = []
    exercise = []
    total_points_list = []
    grade_list = []
    while True:
        info = input("Exam points and exercises completed: ")
        if info == "":
            break
        info_split = info.split(" ")

        if int(info_split[0]) >= 0 and int(info_split[0]) <= 20: 
            exam_point = int(info_split[0]) 
            exam.append(exam_point)
        if int(info_split[0]) >= 0 and int(info_split[0]) <= 100:
            ex_point = (int(info_split[1]) // 10) 
            exercise.append(ex_point)
        total_points_list.append(exam_point + ex_point)
        total_point = int(info_split[0]) + (int(info_split[1]) // 10)
        grade = grade_dis(total_point, int(info_split[0]))
        grade_list.append(grade)

    total_points = reduce(lambda x, y: x+y, total_points_list)
    points_avg = total_points / len(total_points_list)
    pass_percentage = pass_percent(grade_list)
    print(f"Statistics: ")
    print(f"Points average: {points_avg:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print(grade_print(grade_list))
    # ans1 = f"Statistics: \n"
    # ans2 = f"Points average: {points_avg} \n"
    # ans3 = f"Pass Percentage: {pass_percentage} \n"
    # ans4 = grade_print(grade_list)
    # return ans1 + ans2 + ans3 + ans4

main()