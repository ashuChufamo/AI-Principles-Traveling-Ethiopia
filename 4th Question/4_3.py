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
class MiniMaxSearch:
    def __init__(self, graph, utilities):
        self.graph = graph
        self.utilities = utilities

    def minimax_decision(self, state, is_maximizing=True):
        """
        Returns the best achievable destination with utility values using the MiniMax algorithm.
        """
        if state in self.utilities:
            return self.utilities[state], [state], [], []

        best_utility = float('-inf') if is_maximizing else float('inf')
        best_destination = None
        best_path = []
        adversary_path = []
        adversary_moves = []

        for destination in self.graph[state]:
            path = []
            if is_maximizing:
                utility, path, adv_path, adv_moves = self.minimax_decision(destination, False)
                if utility > best_utility:
                    best_utility = utility
                    best_destination = destination
                    best_path = path + [destination]
                    adversary_path = adv_path
                    adversary_moves = adv_moves + [destination]
            else:
                utility, path, adv_path, adv_moves = self.minimax_decision(destination, True)
                if utility < best_utility:
                    best_utility = utility
                    best_destination = destination
                    best_path = path + [destination]
                    adversary_path = adv_path
                    adversary_moves = adv_moves + [destination]

        return best_utility, best_path, adversary_path, adversary_moves




search = MiniMaxSearch(graph, utilities)
best_utility, path, adversary_path, adversary_moves = search.minimax_decision('Addis Ababa')

best_destination = path[-1]
moves = path[1:]

print("Best achievable destination for good quality coffee:", best_destination)
print("Path:", path)
print("Agent's Moves:", moves)
print("Adversary's Path:", adversary_path)
print("Adversary's Moves:", adversary_moves)