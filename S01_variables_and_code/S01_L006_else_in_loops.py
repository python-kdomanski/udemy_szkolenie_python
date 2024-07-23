instruction = ['say hello','say how are you','abort','ask for money','say thank you','say bye']
instryctionApproved=[]

for instr in instruction:
    print('Addning instruction:' , instr)
    instryctionApproved.append(instr)

    if instr=='abort':
        print('Aborting!!!')
        instryctionApproved.clear()
        break
    else:
        #else wykonuje się tylko gdy w pętli nie było break
        print('Following actions will be taken:', instryctionApproved)

print('--------------------------------------')
i=0
while i< len(instruction):
    print('Addning instruction:', instruction[i])
    instryctionApproved.append(instruction[i])

    if instruction[i] == 'abort':
        print('Aborting!!!')
        instryctionApproved.clear()
        break
    i=i+1
else:
    # else wykonuje się tylko gdy w pętli nie było break
    print('Following actions will be taken:', instryctionApproved)
