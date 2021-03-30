

name = "abhishek"

sub1 =  90
sub2 =  80
sub3 =  90
sub4 =  75
sub5 =  83


stu_total = 0

stu_total = sub1 + sub2 + sub3 + sub4 + sub5 

student_precent = float(stu_total*100)/500

print ('student Name  :', name)
print('student Total  :', stu_total)
print ('student precent :', student_precent, '%' )

if (student_precent>=60 ):
    print("student divition is 1st")

if (student_precent<60 and student_precent >=50 ):
    print("student divition is 2nd")
    
if (student_precent<50 and student_precent >=40 ):
    print("student divition is 3rd")

if (student_precent<39):
    print("student divition is Fail")
    

