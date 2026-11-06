# student_name=(input('enter name :'))
# roll_number=int(input('enter rollnumber :'))
# subject=input('enter your subjects : ',).split()
# subtent_marks=0
# s=len(subject)*100
# d={}
# for i in subject:
#         d[i]=int(input(f'enter your {i} marks :' ,))
# # print(f'NAME : {student_name},ROLLNUMBER : {roll_number},',d)
# sum=d.values()
# subtent_mark=0
# for j in sum:
#         subtent_marks+=j
# print(f'NAME : {student_name},ROLLNUMBER : {roll_number},',d)
# print(f'student avarege marks ',(subtent_marks/s*100))
def student():
 student_name=(input('enter name :'))
 roll_number=int(input('enter rollnumber :'))
 subject=input('enter your subjects : ',).split()
 subtent_marks=0
 s=len(subject)*100
 d={}
 for i in subject:
        d[i]=int(input(f'enter your {i} marks :' ,))
# print(f'NAME : {student_name},ROLLNUMBER : {roll_number},',d)
 sum=d.values()
 subtent_mark=0
 for j in sum:
         subtent_marks+=j
         if subtent_marks >=(len(subject)*100/50) :
          print('hi')
 print(f'NAME : {student_name},ROLLNUMBER : {roll_number},',d)
 print(f'student avarege marks ',(subtent_marks/s*100))
 return subtent_marks
a=student()
print(a)
print(student())
