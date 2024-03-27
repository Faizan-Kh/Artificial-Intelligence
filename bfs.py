from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)
 
    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)  # Consider adding this line for an undirected graph
 
    # Function to perform Breadth First Search on a graph represented using adjacency list
    def bfs(self, startNode):
        # Create a queue for BFS
        queue = deque()
        
        # Initialize visited list with a size that covers all possible nodes in the graph
        max_node = max(self.adjList.keys(), default=0)
        visited = [False] * (max_node + 1)
 
        # Mark the current node as visited and enqueue it
        visited[startNode] = True
        queue.append(startNode)
 
        # Iterate over the queue
        while queue:
            # Dequeue a vertex from queue and print it
            currentNode = queue.popleft()
            print(currentNode, end=" ")
 
            # Get all adjacent vertices of the dequeued vertex currentNode
            # If an adjacent has not been visited, then mark it visited and enqueue it
            for neighbor in self.adjList[currentNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
 
 
# Create a graph
graph = Graph()
 
# Add edges to the graph
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 4) 
 
# Perform BFS traversal starting from vertex 0
print("Breadth First Traversal starting from vertex 0:", end=" ")
graph.bfs(0)
