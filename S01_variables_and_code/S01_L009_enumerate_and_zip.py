workDays=[19,21,22,21,20,22]

print(workDays[2])

enumerateDays = list(enumerate(workDays))
print(enumerateDays)

for pos, value in enumerateDays:
    print('Position ', pos, 'value', value)

months = ['I', 'II', 'III', 'IV', 'V', 'VI']
monthsDays=list(zip(months, workDays)) #zip łączy
print(monthsDays)

for m, d in monthsDays:
    print('Month ', m , 'days',d)

for pos, (m, d) in enumerate(zip(months, workDays)):
    print('Position', pos, 'month', m, 'days',d)