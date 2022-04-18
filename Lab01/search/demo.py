import searchTestClasses
import search

# space = """start_state: A 
# goal_states: F
# A 0:A->C C 10.0
# A 1:A->B B 15.0
# A 2:A->D D 17.0
# C 0:C->B B 4.0
# C 1:C->E E 5.0
# C 2:C->F F 6.0
# B 0:B->E E 3.0
# E 0:E->F F 4.0
# D 0:D->E E 8.0
# D 1:D->F F 5.0"""

space = """start_state: A 
goal_states: F
A 0:A->C C 10.0
A 1:A->B B 15.0
A 2:A->D D 17.0
B 0:B->E E 3.0
C 0:C->B B 4.0
C 1:C->E E 5.0
C 2:C->F F 6.0
D 0:D->E E 8.0
D 1:D->F F 5.0
E 0:E->F F 4.0"""

print(space)
problem = searchTestClasses.GraphSearch(space)
actions = search.ucs(problem)
actions2 = search.bfs(problem)
a3 = search.astar(problem)
a4 = search.brfs(problem)
a5 = search.dfs(problem)
print('ucs: ', actions)
print('bfs: ', actions2)
print('dfs: ', a5)
print('astart: ', a3)
print('brfs: ', a4)