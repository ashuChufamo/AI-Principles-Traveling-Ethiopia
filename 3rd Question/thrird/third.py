import heapq

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
'Goba': {'Babile' : 28, 'Sof Oumer' : 6, 'Robe' : 18},
'Sof Oumer': {'Goba' : 6, 'Gode' : 23, 'Robe' : 23},
'Kebri Dehar': {'Dega Habur' : 6, 'Gode' : 5, 'Weder' : 6},
'Weder': {'Kebri Dehar' : 6},
'Gode': {'Kebri Dehar' : 5, 'Dollo' : 17, 'Mokadishu' : 22, 'Sof Oumer' : 23},
'Mokadishu': {'Gode' : 22},
'Dollo': {'Gode' : 17},
'Robe': {'Goba' : 18, 'Sof Oumer' : 23, 'Liben' : 11, 'Dodolla' : 13},
'Liben': {'Robe' : 11},
'Dodolla': {'Robe' : 13, 'Assasa' : 1, 'Shashemene' :3},
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

heuristic = {
    'Addis Ababa': 26,
    'Ambo': 31,
    'Nekemete': 39,
    'Gimbi': 43,
    'Dembi Dollo': 49,
    'Assosa': 51,
    'Metekel': 59,
    'Bahirdar': 48,
    'Injibara': 44,
    'Finote Selam': 42,
    'Debre Markos': 39,
    'Debre Sina': 33,
    'Kemise': 40,
    'Dessie': 44,
    'Woldia': 50,
    'Lalibela': 57,
    'Sekota': 59,
    'Mekelle': 58,
    'Adwa': 65,
    'Adigrat': 62,
    'Asmera': 68,
    'Axum': 66,
    'Shire': 67,
    'Humera': 65,
    'Gondar': 56,
    'Debarke': 60,
    'Metema': 62,
    'Khartoum': 81,
    'Azezo': 55,
    'Debre Tabor': 52,
    'Alamata': 53,
    'Debre Birhan': 31,
    'Samara': 42,
    'Fanti Rasu': 49,
    'Kilbet Rasu': 55,
    'Gabi Rasu': 32,
    'Awash': 27,
    'Chiro': 31,
    'Dire Dawa': 31,
    'Harar': 35,
    'Babile': 37,
    'Jigjiga': 40,
    'Dega Habur': 45,
    'Goba': 40,
    'Sof Oumer': 45,
    'Kebri Dehar': 40,
    'Weder': 46,
    'Gode': 35,
    'Mokadishu': 40,
    'Dollo': 18,
    'Robe': 22,
    'Liben': 11,
    'Dodolla': 19,
    'Assasa': 18,
    'Assella': 22,
    'Adama': 23,
    'Matahara': 26,
    'Batu': 19,
    'Buta Jirra': 21,
    'Worabe': 22,
    'Wolkite': 25,
    'Jimma': 33,
    'Bedelle': 40,
    'Gore': 46,
    'Gambela': 51,
    'Tepi': 41,
    'Bonga': 33,
    'Mizan Teferi': 37,
    'Basketo': 23,
    'Bench Maji': 28,
    'Juba': 50,
    'Arba Minch': 13,
    'Wolaita Sodo': 17,
    'Hossana': 21,
    'Shashemene': 16,
    'Hawassa': 15,
    'Dilla': 12,
    'Bule Hora': 8,
    'Yabello': 6,
    'Moyale': 0,
    'Nairobi': 22,
    'Konso': 9,
    'Dawro': 23,
}

class AStarSearch:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def astar_search(self, start, goal):
        priority_queue = [(0, start)]  # (cumulative_weight + heuristic, node)
        visited = {start: 0}
        parent = {start: None}

        while priority_queue:
            cumulative_weight, current_node = heapq.heappop(priority_queue)

            if current_node == goal:
                return self._reconstruct_path(parent, current_node)

            for neighbor, weight in self.graph[current_node].items():
                new_weight = visited[current_node] + weight
                if neighbor not in visited or new_weight < visited[neighbor]:
                    visited[neighbor] = new_weight
                    priority = new_weight + self.heuristic[neighbor]
                    heapq.heappush(priority_queue, (priority, neighbor))
                    parent[neighbor] = current_node

        return None

    def _reconstruct_path(self, parent, goal):
        path = []
        current_node = goal
        while current_node is not None:
            path.append(current_node)
            current_node = parent[current_node]
        path.reverse()
        return path
    

search = AStarSearch(graph, heuristic)

# Perform A* search
start_state = 'Addis Ababa'
goal_state = 'Moyale'
path = search.astar_search(start_state, goal_state)

# Print the resulting path
if path is not None:
    print("Path found:", ' -> '.join(path))
else:
    print("No path found from", start_state, "to", goal_state)
