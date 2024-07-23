def Bake(what):
    print('Backing {}'.format(what))

def Add(what):
    print('Adding {}'.format(what))

def Mix(what):
    print('Mixing {}'.format(what))

cookbook = [(Add, 'milk'),(Add, 'eggs'),(Add, 'flour'),(Mix, 'ingredients'),(Bake, 'cookies')]

for activity, obj in cookbook:
    activity(obj)

print('-'*30)

def Cook (activity, obj):
    activity(obj)

Cook(Bake,'brovnies')
for activity, obj in cookbook:
    Cook(activity,obj)