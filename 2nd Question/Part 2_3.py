import heapq

# Example usage
graph = {
'Addis Ababa': {'Ambo' : 5, 'Debre Birhan' : 5, 'Adama' : 3},
'Ambo': {'Addis Ababa' : 5, 'Wolkite' : 6, 'Nekemete' : 9},
'Nekemete': {'Ambo' : 5, 'Gimbi' : 4, 'Bedelle' : 5},
'Gimbi': {'Nekemete' : 4, 'Dembi Dollo' : 6},
'Dembi Dollo': {'Gimbi' : 6, 'Assosa' : 12, 'Gambela' : 4},
'Assosa': {'Dembi Dollo' : 12},
'Metekel': {'Bahirdar' : 11},
'Bahirdar': {'Injibara' : 4, 'Finote Selam' : 6, 'Azezo' : 7, 'Debre Tabor' : 4, 'Metekel' : 11},
'Injibara': {'Bahirdar' : 4, 'Finote Selam' : 2},
'Finote Selam': {'Bahirdar' : 6, 'Injibara' : 2, 'Debre Markos' : 3},
'Debre Markos': {'Finote Selam' : 3, 'Debre Sina' : 17},
'Debre Sina': {'Debre Markos' : 17, 'Kemise' : 6, 'Debre Birhan' : 2},
'Kemise': {'Debre Sina' : 6, 'Dessie' : 4},
'Dessie': {'Kemise' : 4, 'Woldia' : 6},
'Woldia': {'Dessie' : 6, 'Lalibela' : 7, 'Alamata' : 3, 'Samara' : 8},
'Lalibela': {'Woldia' : 7, 'Sekota' : 6, 'Debre Tabor' : 8},
'Sekota': {'Lalibela' : 6, 'Mekelle' : 9, 'Alamata' :6 },
'Mekelle': {'Sekota' : 9, 'Adwa' : 7, 'Adigrat' : 4, 'Alamata' : 5},
'Adwa': {'Mekelle' : 7, 'Adigrat' : 4, 'Axum' : 1},
'Adigrat': {'Adwa' : 4, 'Mekelle' : 4, 'Asmera' : 6},
'Asmera': {'Adigrat' : 6, 'Axum' : 5},
'Axum': {'Adwa' : 1, 'Shire' : 2, 'Asmera' : 5},
'Shire': {'Axum' : 2, 'Humera' : 8, 'Debarke' : 7},
'Humera': {'Shire' : 8, 'Gondar' : 9, 'Khartoum' : 21},
'Gondar': {'Humera' : 9, 'Debarke' : 4, 'Metema' : 7, 'Azezo' : 1},
'Debarke': {'Gondar' : 4, 'Shire' : 7},
'Metema': {'Gondar' :7 , 'Khartoum' : 1, 'Azezo' : 7},
'Khartoum': {'Humera' : 21, 'Metema' : 19},
'Azezo': {'Metema' : 7, 'Gondar' : 1, 'Bahirdar' : 7},
'Debre Tabor': {'Bahirdar' : 4, 'Lalibela' : 8},
'Alamata': {'Mekelle' : 5, 'Sekota' : 6, 'Woldia' : 3, 'Samara' : 11},
'Debre Birhan': {'Addis Ababa' : 5, 'Debre Sina' : 2},
'Samara': {'Fanti Rasu' : 7, 'Alamata' : 11, 'Woldia' : 8, 'Gabi Rasu' : 9},
'Fanti Rasu': {'Samara' : 7, 'Kilbet Rasu' : 6},
'Kilbet Rasu': {'Fanti Rasu' : 6},
'Gabi Rasu': {'Samara' : 9, 'Awash' : 5},
'Awash': {'Gabi Rasu' : 5, 'Chiro' : 4, 'Matahara' : 1},
'Chiro': {'Awash' : 4, 'Dire Dawa' : 8},
'Dire Dawa': {'Chiro' : 8, 'Harar' : 4},
'Harar': {'Dire Dawa' : 4, 'Babile' : 2},
'Babile': {'Harar' : 2, 'Jigjiga' : 3, 'Goba' : 328},
'Jigjiga': {'Babile' : 3, 'Dega Habur' : 5},
'Dega Habur': {'Jigjiga' : 5, 'Kebri Dehar' : 6},
'Goba': {'Babile' : 28, 'Sof Oumer' : 6, 'Bale' : 18},
'Sof Oumer': {'Goba' : 6, 'Gode' : 23, 'Bale' : 23},
'Kebri Dehar': {'Dega Habur' : 6, 'Gode' : 5, 'Weder' : 6},
'Weder': {'Kebri Dehar' : 6},
'Gode': {'Kebri Dehar' : 5, 'Dollo' : 17, 'Mokadishu' : 22, 'Sof Oumer' : 23},
'Mokadishu': {'Gode' : 22},
'Dollo': {'Gode' : 17},
'Bale': {'Goba' : 18, 'Sof Oumer' : 23, 'Liben' : 11, 'Dodolla' : 13},
'Liben': {'Bale' : 11},
'Dodolla': {'Bale' : 13, 'Assasa' : 1, 'Shashemene' :3},
'Assasa': {'Dodolla' : 1, 'Assella' : 4},
'Assella': {'Assasa' : 4, 'Adama' : 4},
'Adama': {'Assella' : 4, 'Addis Ababa' : 3, 'Matahara' : 3, 'Batu' : 4},
'Matahara': {'Adama' : 3, 'Awash' : 1},
'Batu': {'Adama' : 4, 'Buta Jirra' : 2, 'Shashemene' : 3},
'Buta Jirra': {'Batu' : 2, 'Worabe' : 2},
'Worabe': {'Buta Jirra' : 2, 'Wolkite' : 5, 'Hossana' : 2},
'Wolkite': {'Worabe' : 5, 'Ambo' : 6, 'Jimma' : 8},
'Jimma': {'Wolkite' : 8, 'Bedelle' : 7, 'Bonga' : 4},
'Bedelle': {'Jimma' : 7, 'Nekemete' : 5, 'Gore' : 6},
'Gore': {'Bedelle' : 6, 'Gambela' : 5, 'Tepi' : 9},
'Gambela': {'Gore' : 5, 'Dembi Dollo' : 4},
'Tepi': {'Gore' : 9, 'Bonga' : 8, 'Mizan Teferi' : 4},
'Bonga': {'Tepi' : 8, 'Jimma' : 4, 'Mizan Teferi' : 4, 'Dawro' : 10},
'Mizan Teferi': {'Bonga' : 4, 'Tepi' : 4},
'Basketo': {'Bench Maji' : 5, 'Arba Minch' : 10},
'Bench Maji': {'Basketo' : 5, 'Juba' : 22},
'Juba': {'Bench Maji' : 22},
'Arba Minch': {'Basketo' : 10, 'Wolaita Sodo' : 5, 'Konso' : 4},
'Wolaita Sodo': {'Arba Minch' : 5, 'Dawro' : 6, 'Hossana' : 4},
'Hossana': {'Wolaita Sodo' : 4, 'Worabe' : 2, 'Shashemene' : 7},
'Shashemene': {'Hossana' : 7, 'Batu' : 3, 'Hawassa' : 1, 'Dodolla' : 3},
'Hawassa': {'Shashemene' : 1, 'Dilla' : 3},
'Dilla': {'Hawassa' : 3, 'Bule Hora' : 4},
'Bule Hora': {'Dilla' : 4, 'Yabello' :3 },
'Yabello': {'Bule Hora' : 3, 'Moyale' :6, 'Konso' : 3},
'Moyale': {'Yabello' : 6, 'Nairobi' : 22},
'Nairobi': {'Moyale' : 22},
'Konso': {'Yabello' : 3, 'Arba Minch' : 4},
'Dawro': {'Wolaita Sodo' : 6, 'Bonga' : 10},
}

def uniform_cost_search(graph, start, goal):
    # Priority queue to store nodes with their cumulative costs
    priority_queue = [(0, start)]  # (cumulative_cost, node)
    # Dictionary to keep track of visited nodes and their cumulative costs
    visited = {start: 0}
    # Dictionary to keep track of the parent node for each visited node
    parent = {start: None}

    while priority_queue:
        cumulative_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            # Reached the goal, construct the path
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path

        for neighbor, cost in graph[current_node].items():
            new_cost = visited[current_node] + cost

            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor))
                parent[neighbor] = current_node

    # No path found
    return None

# Define your graph

start_node = 'Addis Ababa'
goal_states = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minch"]

current_node = start_node
path = []

while goal_states:
    nearest_goal = None
    nearest_distance = float('inf')

    for goal in goal_states:
        goal_path = uniform_cost_search(graph, current_node, goal)
        if goal_path is not None:
            distance = len(goal_path) - 1  # Calculate the distance as the number of edges
            if distance < nearest_distance:
                nearest_goal = goal
                nearest_distance = distance

    if nearest_goal is None:
        print("No path found passing through remaining goal states.")
        break

    goal_states.remove(nearest_goal)
    goal_path = uniform_cost_search(graph, current_node, nearest_goal)
    path.extend(goal_path[:-1])  # Exclude the last node to avoid duplication
    current_node = nearest_goal

if goal_states:
    print("No path found passing through all goal states.")
else:
    path.append(goal_path[-1])
    print("Path found:", ' -> '.join(path))