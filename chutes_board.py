import networkx as nx

ladders = [
    (1, 38),
    (4, 14),
    (9, 31),
    (21, 42),
    (28, 84),
    (36, 44),
    (51, 67),
    (71, 91),
    (80, 100)
]

chutes = [
    (98, 78),
    (95, 75),
    (93, 73),
    (87, 24),
    (64, 60),
    (56, 53),
    (47, 26),
    (49, 11),
    (62, 19),
    (16, 6),
]

main_path = [(i, i+1) for i in range(0, 100)]

board = nx.DiGraph()
for a, b in main_path + chutes + ladders:
    board.add_edge(a, b)


print(board)