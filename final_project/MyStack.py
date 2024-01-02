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
    'Dembi Dollo': ['Gimbi', 'Assosa', 'Gambela'],
    'Assosa': ['Dembi Dollo', 'Metekel'],
    'Metekel': ['Assosa', 'Bahirdar'],
    'Bahirdar': ['Injibara', 'Finote Selam', 'Azezo', 'Debre Tabor'],
    'Injibara': ['Bahirdar', 'Finote Selam'],
    'Finote Selam': ['Bahirdar', 'Injibara', 'Debre Markos'],
    'Debre Markos': ['Finote Selam', 'Debre Sina'],
    'Debre Sina': ['Debre Markos', 'Kemise', 'Debre Birhan'],
    'Kemise': ['Debre Sina', 'Dessie'],
    'Dessie': ['Kemise', 'Woldia'],
    'Woldia': ['Dessie', 'Lalibela', 'Alamata', 'Samara'],
    'Lalibela': ['Woldia', 'Sekota', 'Debre Tabor'],
    'Sekota': ['Lalibela', 'Mekelle', 'Alamata'],
    'Mekelle': ['Sekota', 'Adwa', 'Adigrat', 'Alamata'],
    'Adwa': ['Mekelle', 'Adigrat', 'Axum'],
    'Adigrat': ['Adwa', 'Mekelle', 'Asmera'],
    'Asmera': ['Adigrat', 'Axum'],
    'Axum': ['Adwa', 'Shire', 'Asmera'],
    'Shire': ['Axum', 'Humera', 'Debarke'],
    'Humera': ['Shire', 'Gondar', 'Khartoum'],
    'Gondar': ['Humera', 'Debarke', 'Metema', 'Azezo'],
    'Debarke': ['Gondar', 'Shire'],  
    'Metema': ['Gondar', 'Khartoum', 'Azezo'],
    'Khartoum': ['Humera', 'Metema'],  
    'Azezo': ['Metema', 'Gondar', 'Bahirdar'],  
    'Debre Tabor': ['Bahirdar', 'Lalibela'],  
    'Alamata': ['Mekelle', 'Sekota', 'Woldia', 'Samara'],  
    'Debre Birhan': ['Addis Ababa', 'Debre Sina'],  
    'Samara': ['Fanti Rasu', 'Alamata', 'Woldia', 'Gabi Rasu'],
    'Fanti Rasu': ['Samara', 'Kilbet Rasu'], 
    'Kilbet Rasu': ['Fanti Rasu'],
    'Gabi Rasu': ['Samara', 'Awash'], 
    'Awash': ['Gabi Rasu', 'Chiro', 'Matahara'], 
    'Chiro': ['Awash', 'Dire Dawa'], 
    'Dire Dawa': ['Chiro', 'Harar'], 
    'Harar': ['Dire Dawa', 'Babile'], 
    'Babile': ['Harar', 'Jigjiga'], 
    'Jigjiga': ['Babile', 'Dega Habur'], 
    'Dega Habur': ['Jigjiga', 'Goba', 'Kebri Dehar'], 
    'Goba': ['Dega Habur', 'Sor Oumer', 'Bale'],
    'Sor Oumer': ['Goba', 'Kebri Dehar', 'Bale'],
    'Kebri Dehar': ['Sor Oumer', 'Dega Habur', 'Gode', 'Weder'],
    'Weder': ['Kebri Dehar'],
    'Gode': ['Kebri Dehar', 'Dollo', 'Mokadishu'],
    'Mokadishu': ['Gode'],
    'Dollo': ['Gode'],
    'Bale': ['Goba', 'Sor Oumer', 'Liben', 'Dodolla'],
    'Liben': ['Bale'],
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
    'Mizan Teferi': ['Bonga', 'Tepi', 'Basketo'],
    'Basketo': ['Dawro', 'Mizan Teferi', 'Bench Maji', 'Arba Minch'],
    'Bench Maji': ['Basketo', 'Juba'], 
    'Juba': ['Bench Maji'],
    'Arba Minch': ['Basketo', 'Wolaita Sodo', 'Konso'],
    'Wolaita Sodo': ['Arba Minch', 'Dawro', 'Hossana'],
    'Hossana': ['Wolaita Sodo', 'Worabe', 'Shashemene'],
    'Shashemene': ['Hossana', 'Batu', 'Hawassa', 'Dodolla'],
    'Hawassa': ['Shashemene', 'Dilla'],
    'Dilla': ['Hawassa', 'Bule Hora'],
    'Bule Hora': ['Dilla', 'Yabello'],
    'Yabello': ['Bule Hora', 'Moyale', 'Konso'],
    'Moyale': ['Yabello', 'Nairobi'],
    'Nairobi': ['Moyale'],
    'Konso': ['Yabello', 'Arba Minch'],
    'Dawro': ['Wolaita Sodo', 'Bonga', 'Basketo'],
}

start_city = 'Addis Ababa'
dfs(graph, start_city)