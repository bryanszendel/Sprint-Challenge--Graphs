"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

# MEMORIZE THIS for DFT and BFT:   
        # Create a queue/stack as appropriate
        # Put the starting point in that
        # Make a set to track where we've been
        # While there is stuff in the queue/stack
        #   If not visited:
        #       DO THE THING!
        #       Add to visited
        #       For each edge in the item
        #           Add that edge to the queue/stack

class Graph:

    """Represent a graph as a dictionary of rooms mapping labels to edges."""
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_id):
        """
        Add a room to the graph.
        """
        self.rooms[room_id] = {}

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.

        If both exist, add a connection from v1 to v2.
        """
        if v1 in self.rooms and v2 in self.rooms:
            self.rooms[v1].add(v2)
        else:
            raise IndexError("That room does not exist.")

    def get_neighbors(self, room_id):
        """
        Get all neighbors (edges) of a room.
        """
        exits = []
        for direction in self.rooms[room_id]:
            # return self.rooms[room_id][direction]
            exits.append(direction)
        return exits

    def bft(self, starting_room):
        """
        Print each room in breadth-first order
        beginning from starting_room.
        """
# Create a queue/stack as appropriate
        queue = Queue()

        # Put the starting point in that
        queue.enqueue(starting_room)
        
        # Make a set to track where we've been
        visited = set()
        
        # While there is stuff in the queue/stack
        while queue.size() > 0:
        #   Pop the first item
            room = queue.dequeue()
        #   If not visited:
            if room not in visited:
        #       DO THE THING!
        #       Add to visited
                print(room)
                visited.add(room)
        #       For each edge in the item
                for next_room in self.get_neighbors(room):
        #           Add that edge to the queue/stack
                    queue.enqueue(next_room)

    def dft(self, starting_room):
        """
        Print each room in depth-first order
        beginning from starting_room.
        """
        # Create a queue/stack as appropriate
        stack = Stack()

        # Put the starting point in that
        stack.push(starting_room)
        
        # Make a set to track where we've been
        visited = set()
        
        # While there is stuff in the queue/stack
        while stack.size() > 0:
        #   Pop the first item
            room = stack.pop()
        #   If not visited:
            if room not in visited:
        #       DO THE THING!
        #       Add to visited
                print('ROOM', room)
                visited.add(room)
        #       For each edge in the room
                # print('NEIGHBS', self.get_neighbors(room))
                for next_room in graph.get_neighbors(room):
        #           Add that edge to the queue/stack
                    print('next_room', next_room)
                    stack.push(next_room)
                    # for next_next_room in self.get_neighbors(next_room):
                    #     stack.push(next_next_room)
                print(stack.stack)

    def dft_recursive(self, starting_room, visited=None):
        """
        Print each room in depth-first order
        beginning from starting_room.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_room)
        print(starting_room)
        for child_vert in self.rooms[starting_room]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_room, destination_room):
        """
        Return a list containing the shortest path from
        starting_room to destination_room in
        breath-first order.
        """
        # Create a queue/stack as appropriate
        queue = Queue()

        # Put the starting point in that
        queue.enqueue([starting_room])
        
        # Make a set to track where we've been
        visited = set()
        
        # While there is stuff in the queue/stack
        while queue.size() > 0:
        #   Pop the first item
            path = queue.dequeue()
            room = path[-1]
        #   If not visited:
            if room not in visited:
                if room == destination_room:
        #           DO THE THING!
                    return path
                visited.add(room)
        #       For each edge in the item
                for next_room in self.get_neighbors(room):
        #           Copy path to avoid pass by reference bug
                    new_path = list(path) # make a 'copy' rather than 'reference'
                    new_path.append(next_room)
                    queue.enqueue(new_path)

    def dfs(self, starting_room, destination_room):
        """
        Return a list containing a path from
        starting_room to destination_room in
        depth-first order.
        """
        # Create a queue/stack as appropriate
        stack = Stack()

        # Put the starting point in that
        stack.push([starting_room])
        
        # Make a set to track where we've been
        visited = set()
        
        # While there is stuff in the queue/stack
        while stack.size() > 0:
        #   Pop the first item
            path = stack.pop()
            room = path[-1]
        #   If not visited:
            if room not in visited:
                if room == destination_room:
        #           DO THE THING!
                    return path
                visited.add(room)
        #       For each edge in the item
                for next_room in self.get_neighbors(room):
        #           Copy path to avoid pass by reference bug
                    new_path = list(path) # make a 'copy' rather than 'reference'
                    new_path.append(next_room)
                    stack.push(new_path)
                    

    def dfs_recursive(self, starting_room, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_room to destination_room in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_room)
        path = path + [starting_room]
        if starting_room == target_value:
            return path
        for child_vert in self.rooms[starting_room]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_room(1)
    graph.add_room(2)
    graph.add_room(3)
    graph.add_room(4)
    graph.add_room(5)
    graph.add_room(6)
    graph.add_room(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.rooms)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('running bft')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('running dft')
    graph.dft(1)

    print('running dft_recursive')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('running BFS')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('running DFS')
    print(graph.dfs(1, 6))
    print('running dfs_recursive')
    print(graph.dfs_recursive(1, 6))
