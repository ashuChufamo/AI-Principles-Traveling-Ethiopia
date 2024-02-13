class MiniMaxSearch:
    def __init__(self, locations, utilities):
        self.locations = locations
        self.utilities = utilities

    def minimax(self, state, is_maximizing_player):
        if state in self.utilities:
            return self.utilities[state]

        if is_maximizing_player:
            best_utility = float('-inf')
            for neighbor in self.locations[state]:
                utility = self.minimax(neighbor, False)
                best_utility = max(best_utility, utility)
            return best_utility
        else:
            best_utility = float('inf')
            for neighbor in self.locations[state]:
                utility = self.minimax(neighbor, True)
                best_utility = min(best_utility, utility)
            return best_utility

    def get_best_destination(self, start_state):
        best_utility = float('-inf')
        best_destination = None

        for neighbor in self.locations[start_state]:
            utility = self.minimax(neighbor, False)
            if utility > best_utility:
                best_utility = utility
                best_destination = neighbor

        if best_destination is not None and best_destination in self.utilities:
            return best_destination
        else:
            return None

# Usage example
ethiopia_coffee_location = {
    "Addis Ababa": {"Ambo", "Buta Jirra", "Adama"},
    "Ambo": {"Gedo", "Nekemte"},
    "Buta Jirra": {"Worabe", "Wolkite"},
    "Adama": {"Dire Dawa", "Mojo"},
    "Gedo": {"Shambu", "Fincha"},
    "Nekemte": {"Gimbi", "Limu"},
    "Worabe": {"Hosana", "Durame"},
    "Wolkite": {"Benchi Naji", "Tepi"},
    "Mojo": {"Dilla", "Kaffa"},
    "Dire Dawa": {"Chiro", "Harar"},
    "Shambu": set(),
    "Fincha": set(),
    "Gimbi": set(),
    "Limu": set(),
    "Hosana": set(),
    "Durame": set(),
    "Benchi Naji": set(),
    "Tepi": set(),
    "Kaffa": set(),
    "Dilla": set(),
    "Chiro": set(),
    "Harar": set()
}

terminal_utilities = {
    "Shambu": 4,
    "Fincha": 5,
    "Gimbi": 8,
    "Limu": 8,
    "Hosana": 6,
    "Durame": 5,
    "Benchi Naji": 5,
    "Tepi": 6,
    "Kaffa": 7,
    "Dilla": 9,
    "Chiro": 6,
    "Harar": 10
}

search_problem = MiniMaxSearch(ethiopia_coffee_location, terminal_utilities)
start_state = "Addis Ababa"
best_destination = search_problem.get_best_destination(start_state)
print("Best achievable destination:", best_destination)