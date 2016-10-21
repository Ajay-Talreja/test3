def markshet(marks):
    count=0
    mrksum=sum(marks)
    percent=round((mrksum/7),2)
    for i in marks:
        if i<40:
            count+=1
    else:
        if (count>0 and count==3):
                x="You are Failed.!"
        elif count>3:
                x="You are Droped" 
        elif i>=40:
            print("Congratulation..")
            if percent<40:
                x=percent,"% and got 'E' grade"
            elif percent>=40 and percent<50:
                x=percent,"% and got 'D' grade"
                
            elif percent>=50 and percent<70:
                x=percent,"% and got 'C' grade"
            elif percent>=70 and percent<80:
                x=percent,"% and got 'B' grade"
            elif percent>=88 and percent<90:
                x=percent,"% and got 'A' grade"
            else:
                x=percent,"% and got 'O' grade" 
    return x       
marks=[]
for i in range(1,8):
    mk=int(input("Enter your marks: "))
    marks.append(mk)
print(markshet(marks))
INPUT("PRESS ENTER TO EXIT")
