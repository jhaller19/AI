#search
'''
Output for hdistance1:

Pushes: 26081.58
Pops: 12413.78
Cost path: 15.81

*************************
Output for hdistance2:

Pushes: 2564.3
Pops: 1274.97
Cost path: 16.19

*************************
Output for weighted hdistance1:

Output for search(4)
Pushes: 14488.34
Pops: 6881.12
Cost path: 15.78
*************************
Output for weighted hdistance2:

Output for search(4)
Pushes: 2908.6
Pops: 1454.4
Cost path: 17.2




'''
import state
import frontier

def search(n):
    s=state.create(n)
    #print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return [s, f]
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
    return 0

#print (search(3))

pushes = 0
pops = 0
depth = 0
costPath = 0
for _ in range(100):
    answer=search(4)
    f = answer[1]
    pushes += f[2]
    pops += f[3]
    costPath += len(answer[0][1])
print('Output for search(' + str(4) + ')')
#print(answer)
print('Pushes: ' + str(pushes/100))
print('Pops: ' + str(pops/100))
print('Cost path: ' + str(costPath/100))
print('')