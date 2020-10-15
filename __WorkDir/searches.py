from search import *
from collections import deque


romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))


romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)


# bfs su albero
def breadth_first_search_tree(problem:Problem) -> Node:
    frontier = deque([Node(problem.initial)])

    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        else:
            frontier.extend(node.expand(problem))


def breadth_first_search_graph(problem:Problem) -> Node:
    frontier = deque([Node(problem.initial)])
    explored = set()

    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        if problem.goal_test(node.state):
            return node
        else:
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    frontier.append(child)
        print(len(frontier))


def dfs_tree(problem:Problem) -> Node:
    frontier = deque([Node(problem.initial)])

    while frontier:
        node = frontier.pop() #LIFO

        if problem.goal_test(node.state):
            return node
        else:
            frontier.extend(node.expand(problem))


def dfs_graph(problem:Problem) -> Node:
    frontier = deque([Node(problem.initial)])
    explored = set()

    while frontier:
        node = frontier.pop()
        explored.add(node.state)
        if problem.goal_test(node.state):
            return node
        else:
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    frontier.append(child)


def best_first_search_graph(problem:Problem, f):

    if problem.goal_test(problem.initial):
        return Node(problem.initial)

    f = memoize(f, 'f')
    frontier = PriorityQueue(order='min', f = f)
    frontier.append(Node(problem.initial))
    explored = set()

    while frontier:
        node = frontier.pop() # estrae nodo con f minima
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                next_node = frontier.get_item(child)
                if f(child) < f(next_node):
                    del frontier[next_node]
                    frontier.append(child)


goal = best_first_search_graph(romania_problem, lambda n: n.path_cost)
print(goal.solution())