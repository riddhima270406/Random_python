student_list = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6", "Student 7", "Student 8", "Student 9", "Student 10"]
  
print(student_list[0])
print(student_list[1])
print(student_list[2])
print(student_list[3])
print(student_list[4])
print(student_list[5])
print(student_list[6])
print(student_list[7])
print(student_list[8])
print(student_list[9])


s1_marks = int(input("Enter Student 1 marks: "))
# s2_marks = int(input("Enter Student 2 marks: "))
# s3_marks = int(input("Enter Student 3 marks: "))
# s4_marks = int(input("Enter Student 4 marks: "))
# s5_marks = int(input("Enter Student 5 marks: "))
# s6_marks = int(input("Enter Student 6 marks: "))
# s7_marks = int(input("Enter Student 7 marks: "))
# s8_marks = int(input("Enter Student 8 marks: "))
# s9_marks = int(input("Enter Student 9 marks: "))
# s10_marks = int(input("Enter Student 10 marks: "))


student = int(input("Press '1' if you wanna add more students otherwise press '0': "))
 
if student == 1:
    no_of_student = int(input("How many Students do you want to add: "))
    add_student = int(input("Enter Student marks:\n"*no_of_student))
    print

elif student != 1:
    print("bye")


