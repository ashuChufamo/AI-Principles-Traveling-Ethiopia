class MiniMaxSearch:
    def __init__(self, graph, utilities):
        self.graph = graph
        self.utilities = utilities

    def minimax_decision(self, state):
        """
        Returns the best achievable destination with utility values using the MiniMax algorithm.
        """
        best_utility = float('-inf')
        best_destination = None
        path = []
        moves = []

        for destination in self.utilities.keys():
            if self.utilities[destination] is not None:
                utility, move = self.min_value(destination)
                if utility > best_utility:
                    best_utility = utility
                    best_destination = destination
                    path = self.get_path(destination)
                    moves = [move]

        return best_destination, path, moves

    def max_value(self, state):
        """
        Returns the maximum utility value for the agent in the given state.
        """
        if self.utilities[state] is not None:
            return self.utilities[state], None

        max_utility = float('-inf')
        best_move = None

        for action in self.graph[state]:
            utility, move = self.min_value(action)
            if utility > max_utility:
                max_utility = utility
                best_move = move

        return max_utility, best_move

    def min_value(self, state):
        """
        Returns the minimum utility value for the adversary in the given state.
        """
        if self.utilities[state] is not None:
            return self.utilities[state], None

        min_utility = float('inf')
        best_move = None

        for action in self.graph[state]:
            utility, move = self.max_value(action)
            if utility < min_utility:
                min_utility = utility
                best_move = move

        return min_utility, best_move

    def get_path(self, state):
        """
        Returns the path to the given state from the initial state.
        """
        path = [state]
        current_state = state

        while current_state != 'Addis Ababa':
            for parent_state, child_states in self.graph.items():
                if current_state in child_states:
                    path.append(parent_state)
                    current_state = parent_state
                    break

        path.reverse()
        return path
    
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
    'Addis Ababa': 0,
    'Ambo': 0,
    'Nekemte': 0,
    'Gimbi': 8,
    'Limu': 8,
    'Gedo': 0,
    'Shambu': 4,
    'Fincha': 5,
    'Buta Jirra': 0,
    'Worabe': 0,
    'Hossana': 6,
    'Durame': 5,
    'Wolkite': 0,
    'Bench Maji': 5,
    'Tepi': 6,
    'Adama': 0,
    'Mojo': 0,
    'Kaffa': 7,
    'Dilla': 9,
    'Dire Dawa': 0,
    'Chiro': 6,
    'Harar': 10,
}


search = MiniMaxSearch(graph, utilities)
best_destination, path, moves = search.minimax_decision('Addis Ababa')

print("Best achievable destination for good quality coffee:", best_destination)
print("Path:", path)