dayType=2

weekend=1
workday=2
holiday=3

if dayType ==1:
    pass #pass nic nie robi
elif dayType ==2:
    pass
else :
    pass

dayDescription='weekend' if dayType == 1 else '?'
dayDescription='weekend' if dayType == 1 else 'workday' if dayType==2 else 'holiday'
print(dayDescription)

print('weekend') if dayType == 1 else print('workday') if dayType==2 else print('holiday')