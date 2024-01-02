import matplotlib.pyplot as plt
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    
def dfs(graph, start_city):
    stack = Stack()
    visited = set()

    stack.push(start_city)

    while not stack.is_empty():
        current_city = stack.pop()
        visited.add(current_city)

        # Process the current city
        print("Visiting", current_city)

        # Get the neighboring cities of the current city from the graph
        neighbors = graph[current_city]

        for neighbor_city in neighbors:
            if neighbor_city not in visited:
                stack.push(neighbor_city)

# Example usage
graph = {
    'Addis Ababa': ['Ambo', 'Debre Birhan', 'Adama'],
    'Ambo': ['Addis Ababa', 'Wolkite', 'Nekemete'],
    'Nekemete': ['Ambo', 'Gimbi', 'Bedelle'],
    'Gimbi': ['Nekemete', 'Dembi Dollo'],
    'Dembi Dollo': ['Gimbi', 'Gambela'], 
    'Debre Birhan': ['Addis Ababa'],  
    'Awash': ['Chiro', 'Matahara'], 
    'Chiro': ['Awash', 'Dire Dawa'], 
    'Dire Dawa': ['Chiro', 'Harar'], 
    'Harar': ['Dire Dawa', 'Babile'], 
    'Babile': ['Harar', 'Jigjiga'], 
    'Jigjiga': ['Babile', 'Dega Habur'], 
    'Dega Habur': ['Jigjiga', 'Goba', 'Kebri Dehar'], 
    'Goba': ['Dega Habur', 'Sor Oumer', 'Bale'],
    'Sor Oumer': ['Goba', 'Kebri Dehar', 'Bale'],
    'Kebri Dehar': ['Sor Oumer', 'Dega Habur', 'Gode'],
    'Gode': ['Kebri Dehar'],
    'Bale': ['Goba', 'Sor Oumer', 'Dodolla'],
    'Dodolla': ['Bale', 'Assasa', 'Shashemene'],
    'Assasa': ['Dodolla', 'Assella'],
    'Assella': ['Assasa', 'Adama'],
    'Adama': ['Assella', 'Addis Ababa', 'Matahara', 'Batu'],    
    'Matahara': ['Adama', 'Awash'],
    'Batu': ['Adama', 'Buta Jirra', 'Shashemene'],
    'Buta Jirra': ['Batu', 'Worabe'],
    'Worabe': ['Buta Jirra', 'Wolkite', 'Hossana'],
    'Wolkite': ['Worabe', 'Ambo', 'Jimma'],
    'Jimma': ['Wolkite', 'Bedelle', 'Bonga'],
    'Bedelle': ['Jimma', 'Nekemete', 'Gore'],
    'Gore': ['Bedelle', 'Gambela', 'Tepi'],
    'Gambela': ['Gore', 'Dembi Dollo'],
    'Tepi': ['Gore', 'Bonga', 'Mizan Teferi'],
    'Bonga': ['Tepi', 'Jimma', 'Mizan Teferi', 'Dawro'],
    'Mizan Teferi': ['Bonga', 'Tepi'],
    'Arba Minch': ['Wolaita Sodo'],
    'Wolaita Sodo': ['Arba Minch', 'Dawro', 'Hossana'],
    'Hossana': ['Wolaita Sodo', 'Worabe', 'Shashemene'],
    'Shashemene': ['Hossana', 'Batu', 'Hawassa', 'Dodolla'],
    'Hawassa': ['Shashemene', 'Dilla'],
    'Dilla': ['Hawassa']
}


coordinates = {
    'Addis Ababa': (7, 6),
    'Ambo': (6, 6),
    'Nekemete': (4, 6),
    'Gimbi': (3, 6),
    'Dembi Dollo': (1, 6),
    'Debre Birhan': (8, 7),
    'Awash': (10, 6),
    'Chiro': (11, 6), 
    'Dire Dawa': (12, 6),
    'Harar': (13, 5), 
    'Babile': (14, 5),
    'Jigjiga': (15, 5),
    'Dega Habur': (15, 4),
    'Goba': (11, 2),
    'Sor Oumer': (12, 1),
    'Kebri Dehar': (17, 2),
    'Gode': (16, 0),
    'Bale': (10, 0),
    'Dodolla': (9, 1),
    'Assasa': (9, 2),
    'Assella': (8, 4),
    'Adama': (7, 5),   
    'Matahara': (9, 5),
    'Batu': (7, 4),
    'Buta Jirra': (6, 4),
    'Worabe': (6, 3),
    'Wolkite': (5, 4),
    'Jimma': (4, 4),
    'Bedelle': (4, 5),
    'Gore': (2, 4),
    'Gambela': (0, 4),
    'Tepi': (2, 3),
    'Bonga': (3, 3),
    'Mizan Teferi': (2, 2),
    'Arba Minch': (5, 0),
    'Wolaita Sodo': (5, 2),
    'Hossana': (5, 3),
    'Shashemene': (7, 3),
    'Hawassa': (7, 2),
    'Dilla': (7, 0),
}  # Dictionary to store the coordinates of each state




# Extract x and y coordinates
x_coords = [coord[0] for coord in coordinates.values()]
y_coords = [coord[1] for coord in coordinates.values()]

# Plot the states
plt.scatter(x_coords, y_coords)

# Add labels to the states
for state, coord in coordinates.items():
    plt.annotate(state, coord)

# Set plot limits and labels
plt.xlim(-1, 18)
plt.ylim(-1, 8)
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')

# Show the plot
plt.show()