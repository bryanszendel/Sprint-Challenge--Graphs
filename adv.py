from room import Room
from player import Player
from world import World
from util import Stack, Queue
from graph import Graph
import pprint

import random
from ast import literal_eval

pp = pprint.PrettyPrinter(width=41, compact=True)

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

"""
player.current_room.id
player.current_room.get_exits()
player.travel(direction)

Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first search for a room with a '?' for an exit. If you use the bfs code from the homework, you will need to make a few modifications.

Instead of searching for a target vertex, you are searching for an exit with a '?' as the value. If an exit has been explored, you can put it in your BFS queue like normal.

BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.
"""

def flip_direction(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'

# DFT with a Stack
# travel any direction
## log it in the stack
## travel any direction available again until cannot move anymore
## 'Walk Back' through the last path (logging direction) until there is an unexplored path 
## i.e. do a BFS from that dead end room to find a direction with a '?'
## convert room ids to n/s/e/w and add to traversal path

graph = {0: {'n': '?', 's': '?', 'e': '?', 'w': '?'}}
graph_size = 18
room_counter = 0
current_room = player.current_room.id

stack = Stack()

last_move = 's'
direction = 's'
while room_counter < graph_size:
    print('Current Room: ', player.current_room.id)
    print('Direction: ', direction)
    exits = player.current_room.get_exits()
    current_room = player.current_room.id
    player.travel(direction)
    traversal_path.append(direction)
    stack.push(direction)
    # last_move = direction
    room_counter += 1
    graph[current_room][direction] = player.current_room.id
    if player.current_room.id not in graph:
        graph[player.current_room.id] = {} 
        for exit_int in exits:
            print(exit_int)
            graph[player.current_room.id][exit_int] = '?'
            # if exit_int != last_move:
            #     direction = exit_int
            #     last_move = direction
        print (graph[player.current_room.id])
    
    exits = player.current_room.get_exits()
    for exit_int in exits:
        graph[current_room][direction] = player.current_room.id
        graph[player.current_room.id][flip_direction(direction)] = current_room
        if exit_int != last_move:
            direction = exit_int
            last_move = direction
    print(graph[current_room])

    # exits = player.current_room.get_exits()
    # if new_move = 

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    for i in visited_rooms:
        print(i.id)


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
