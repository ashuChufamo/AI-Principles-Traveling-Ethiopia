class GraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, initial_state, goal_state):
        # Initialize the queue with the initial state
        queue = [(initial_state, [])]
        visited = set()

        while queue:
            current_state, path = queue.pop(0)
            visited.add(current_state)

            if current_state == goal_state:
                return path + [current_state]

            neighbors = self.graph.get(current_state, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [current_state]))

        # No path found
        return None

    def dfs(self, initial_state, goal_state):
        # Initialize the stack with the initial state
        stack = [(initial_state, [])]
        visited = set()

        while stack:
            current_state, path = stack.pop()
            visited.add(current_state)

            if current_state == goal_state:
                return path + [current_state]

            neighbors = self.graph.get(current_state, [])
            # Reverse the order of neighbors to prioritize exploring 'B' before 'C'
            neighbors.reverse()
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [current_state]))

        # No path found
        return None


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
    'Adwa': ['Mekelle', 'Adigrat', 'Axum'],
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
    'Shashemene': ['Hossana', 'Batu', 'Hawassa'],
    'Hawassa': ['Shashemene', 'Dilla'],
    'Dilla': ['Hawassa', 'Bule Hora'],
    'Bule Hora': ['Dilla', 'Yabello'],
    'Yabello': ['Bule Hora', 'Moyale', 'Konso'],
    'Moyale': ['Yabello', 'Nairobi'],
    'Nairobi': ['Moyale'],
    'Konso': ['Yabello', 'Arba Minch'],
    'Dawro': ['Wolaita Sodo', 'Bonga', 'Basketo'],
}

search = GraphSearch(graph)

# Perform BFS
bfs_path = search.bfs('Addis Ababa', 'Debarke')
print("BFS Path:", bfs_path)

# Perform BFS
bfs_path = search.bfs('Asmera', 'Khartoum')
print("BFS Path:", bfs_path)

# Perform DFS
dfs_path = search.dfs('Asmera', 'Khartoum')
print("DFS Path:", dfs_path)