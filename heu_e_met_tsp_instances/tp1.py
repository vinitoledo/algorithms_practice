import os
import math
import time



def read_file(path):
    file = open(path,'r')
    vert_info = file.readlines()
    coords_type = vert_info[4].split(':')[1].strip()
    coords = []
    for i in range(6, len(vert_info) - 2):
        x, y = float(vert_info[i].split()[1]), float(vert_info[i].split()[2])
        coords.append([x,y])
    return coords, coords_type

def gen_ditance_matrix(coords):
    m = len(coords)

    dist = {}
    for i in range(m):
        dist[i] = {}
        for j in range(m):
            if i != j:
                Xd = coords[i][0] - coords[j][0]
                Yd = coords[i][1] - coords[j][1]
                dij = round(math.sqrt(Xd**2 + Yd**2))
                dist[i][j] = dij
                
    return dist

def gen_non_euclidian_ditance_matrix(coords):
    m = len(coords)

    dist = {}
    for i in range(m):
        dist[i] = {}
        for j in range(m):
            if i != j:
                Xd = coords[i][0] - coords[j][0]
                Yd = coords[i][1] - coords[j][1]
                
                rij= math.sqrt( (Xd**2 + Yd**2)/10.0 )
                
                tij= int(round(rij))
                
                if tij<rij:
                    dij= tij+1
                    
                else:
                    dij= tij
   
                dist[i][j] = dij
                
    return dist



def cost_function(dist):
    unvisited_cities = dist.keys()
    cost = 0
    current_city = 0

    choosen = [0]

    while len(unvisited_cities) > 1:

        #print(unvisited_cities)
        smallest_distance = float("inf")

        for next_city in unvisited_cities:

            if next_city != current_city:
                if dist[current_city][next_city] < smallest_distance:

                    smallest_distance = dist[current_city][next_city]
                    chosen_city = next_city

        dist.pop(current_city)
        cost += smallest_distance
        choosen.append(chosen_city)

        current_city = chosen_city

        unvisited_cities = dist.keys()
        #print(cost)

    return cost + dist[current_city][0]


files = sorted(os.listdir('./heu_e_met_tsp_instances/EUC_2D'))


for file in files:
    
    t0 = time.time()
    coords, coords_type = read_file('./heu_e_met_tsp_instances/EUC_2D/'+file)
    
    if coords_type == 'EUC_2D':
        dist = gen_ditance_matrix(coords)
    
    else:
        dist = gen_non_euclidian_ditance_matrix(coords)
        
    cost = cost_function(dist)
    
    t1 = time.time()
    total = round(t1-t0,4)
    print(file.split('.')[0] , cost, total)
