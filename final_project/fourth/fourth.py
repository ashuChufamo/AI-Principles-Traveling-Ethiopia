class MiniMax:
    def __init__(self, graph, utilities, depth):
        self.graph = graph
        self.utilities = utilities
        self.depth = depth

    def get_max_utility(self, state, depth):
        maximums = {}
        for neighbor in self.graph[state]:
            utility = self.utilities[neighbor]
            if depth == 0 or utility > maximums.get(neighbor, -1):
                maximums[neighbor] = utility
        return maximums[state]

    def search(self, state):
        if self.depth == 0 or state in self.utilities:
            return state

        best_state = None
        best_utility = -1

        for neighbor in self.graph[state]:
            utility = self.get_max_utility(neighbor, self.depth - 1)
            if utility > best_utility:
                best_utility = utility
                best_state = neighbor

        return best_state
    
graph = {
    'Addis Ababa': ['Ambo', 'Buta Jirra', 'Adama'],
    'Ambo': ['Addis Ababa', 'Gedo', 'Nekemte'],
    'Nekemte': ['Ambo', 'Gimbi', 'Limu'],
    'Gimbi': ['Nekemte'],
    'Limu': ['Nekemte'],
    'Gedo': ['Ambo', 'Shambu', 'Fincha'],
    'Shambu': ['Gedo'],
    'Fincha': ['Gedo'],
    'Buta Jirra': ['Addis Ababa', 'Worabe', 'Wolkite'],
    'Worabe': ['Buta Jirra', 'Hossana', 'Durame'],
    'Hossana': ['Worabe'],
    'Durame': ['Worabe'],
    'Wolkite': ['Buta Jirra', 'Bench Maji', 'Tepi'],
    'Bench Maji': ['Wolkite'],
    'Tepi': ['Wolkite'],
    'Adama': ['Addis Ababa', 'Mojo', 'Dire Dawa'],
    'Mojo': ['Adama', 'Kaffa', 'Dilla'],
    'Kaffa': ['Mojo'],
    'Dilla': ['Mojo'],
    'Dire Dawa': ['Adama', 'Chiro', 'Harar'],
    'Chiro': ['Dire Dawa'],
    'Harar': ['Dire Dawa'],
}

utilities = {
    'Addis Ababa': None,
    'Ambo': None,
    'Nekemte': None,
    'Gimbi': 8,
    'Limu': 8,
    'Gedo': None,
    'Shambu': 4,
    'Fincha': 5,
    'Buta Jirra': None,
    'Worabe': None,
    'Hossana': 6,
    'Durame': 5,
    'Wolkite': None,
    'Bench Maji': 5,
    'Tepi': 6,
    'Adama': None,
    'Mojo': None,
    'Kaffa': 7,
    'Dilla': 7,
    'Dire Dawa': None,
    'Chiro': 6,
    'Harar': 10,
}

class MiniMaxAgent:
    def __init__(self, graph, utilities):
        self.graph = graph
        self.utilities = utilities

    def minimax_decision(self, state):
        best_action = None
        max_utility = float('-inf')

        for action in self.get_possible_actions(state):
            utility = self.min_value(action, set())
            if utility is not None and utility > max_utility:
                max_utility = utility
                best_action = action

        return best_action

    def max_value(self, state, visited):
        if self.is_terminal_state(state):
            return self.utilities[state]

        max_utility = float('-inf')
        visited.add(state)

        for action in self.get_possible_actions(state):
            if action not in visited:
                utility = self.min_value(action, visited)
                if utility is not None:
                    max_utility = max(max_utility, utility)

        visited.remove(state)
        return max_utility

    def min_value(self, state, visited):
        if self.is_terminal_state(state):
            return self.utilities[state]

        min_utility = float('inf')
        visited.add(state)

        for action in self.get_possible_actions(state):
            if action not in visited:
                utility = self.max_value(action, visited)
                if utility is not None:
                    min_utility = min(min_utility, utility)

        visited.remove(state)
        return min_utility

    def get_possible_actions(self, state):
        return self.graph[state]

    def is_terminal_state(self, state):
        if state in self.graph:
            return all(child not in self.graph or self.utilities[child] is not None for child in self.graph[state])
        return True


agent = MiniMax(graph, utilities, 5)

print(agent.search('Addis Ababa'))