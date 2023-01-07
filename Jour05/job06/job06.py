L = [23, 85, 43, 78, 72, 53, 81, 41, 33, 42, 54, 98]


def round_grades(l):
    round_grades = []
    for grade in L:
        if grade < 40:
            round_grades.append(grade)
        else:
            next_multiple = (grade // 5 + 1) * 5
            if next_multiple - grade < 3:
                round_grades.append(next_multiple)
            else:
                round_grades.append(grade)
    return round_grades


round_grades(L)

print(round_grades(L))
