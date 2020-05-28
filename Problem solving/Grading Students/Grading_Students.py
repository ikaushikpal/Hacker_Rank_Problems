
grade = [73,67,38,33]

def gradingStudents(grades):
    marks = []
    for val in grades :
        if val>=38:
            rem = val % 5
            mark = val
            if rem!=0:
                mark = ((val//5)+1)*5
            if mark-val<3:
                marks.append(mark)
            elif mark-val==3:
                marks.append(val)
        else:
            marks.append(val)
    return marks


print(gradingStudents(grade))

this is totally wrong
