import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import itertools

filename = 'tft.txt'
lines = [line.split(':') for line in open(filename, 'r')]
connections_list = []
for line in lines:
    key = line[0].strip()
    for elem in line[1].split(','):
        connections_list.append((key, elem.strip()))

connections_dict = defaultdict(set)
for (elem1, elem2) in connections_list:
    connections_dict[elem1].add(elem2)
    connections_dict[elem2].add(elem1)

G = nx.Graph()
G.add_edges_from(connections_list)
G.nodes(data=True)
nx.draw_spring(G, with_labels=True)

print("stopnie:", nx.degree(G))
print("rząd:", nx.number_of_nodes(G))
print("rozmiar:", nx.number_of_edges(G))
print("gestosc:", nx.density(G))
print("bliskosc:", nx.closeness_centrality(G))
print("posrednictwo:", nx.betweenness_centrality(G))
print("srednica:", nx.diameter(G))
print("srednia dlugosc sciezki:", nx.average_shortest_path_length(G))
for x in nx.connected_components(G):
    print("skladowa spojna:", x)
print("czy jest k spojny dla k = 3:", nx.is_k_edge_connected(G, 3))
print("spojnosc krawedziowa:", nx.edge_connectivity(G))
print("spojnosc wierzcholkowa:", nx.node_connectivity(G))
print("Kliki maksymalne:", list(nx.find_cliques(G)))
kliki = list(nx.enumerate_all_cliques(G))
kliki1 = []

for i in range(len(kliki)):
    if len(kliki[i]) >= 3:
        kliki1.append(kliki[i])

print("kliki >=3:", kliki1)


plt.show()


nodes = list(G)
max = 0



temp_list = []

for i in range(8,9):
    all_combinations = itertools.combinations(nodes, i)
    lista = (list(all_combinations))
    for j in range(len(lista)):
        tmp = 0
        x = lista[j]
        y = itertools.combinations(x,2)
        lista2 = list(y)

        for z in range(len(lista2)):
            d = lista2[z]
            if G.number_of_edges(d[0],d[1]) == 1:
                tmp += 1
        if tmp > max:

            max = tmp
            temp_list = [x]
        elif tmp == max:
            temp_list.append(x)

    print('Najwięcej połączeń dla maksymalnie ' + str(i) + ' postaci: ' + str(max))
    print('Dla postaci: ', temp_list)
    print('Ilość możliwości: ', len(temp_list))
    max = 0
    temp_list = []
