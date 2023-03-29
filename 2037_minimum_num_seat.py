def minimum_seat(seats,students):
    seats.sort();students.sort();s=0
    # print(seats)
    # print(students)
    for i in range(len(seats)):
        s+=abs(seats[i]-students[i])
    return s
s=[12,14,19,19,12]
stu=[19,2,17,20,7]
print(minimum_seat(s,stu))
