#search

'''
Output:

Output for search(2)
Pushes: 5.96
Pops: 5.58
Depth: 1.63

Output for search(3)
Pushes: 1055.54
Pops: 606.99
Depth: 5.69

search(4) took too long to print anything
'''

import state
import frontier

def search(n):
    s=state.create(n)
    # print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return [s, f] ###returning f not f[1]
        ns=state.get_next(s)
        #print(ns)
        for i in ns:
            frontier.insert(f,i)
    return 0
for i in range(2,5):
    pushes = 0
    pops = 0
    depth = 0
    for _ in range(100):
        answer=search(i)
        f = answer[1]
        pushes += f[4]
        pops += f[5]
        depth += f[1]
    print('Output for search(' + str(i) + ')')
    #print(answer)
    print('Pushes: ' + str(pushes/100))
    print('Pops: ' + str(pops/100))
    print('Depth: ' + str(depth/100))
    print('')

