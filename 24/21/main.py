from shapely.geometry import Point, Polygon
import json
import networkx as nx
import re
import itertools
from tqdm import tqdm
import haversine

def dist(lon1, lat1, lon2, lat2):
    return haversine.haversine((lon1, lat1), (lon2, lat2))

def find_shops_in_norway():

    norway_json = None
    with open("grøtris/norge.geojson") as f:
        norway_json = json.load(f)

    land_masses = []
    for mass in norway_json["features"][0]["geometry"]["coordinates"]:
        land_masses.append(mass[0])

    polygons = []
    for mass in land_masses:
        polygons.append(Polygon(mass))

    shops_in_norway = []
    with open("grøtris/butikker.csv") as f:
        for line in f.read().rstrip().split("\n")[1:]:
            lat, lon, ris = re.findall(r'[-+]?\d*\.\d+|\d+', line)
            if ris == "0":
                continue
            
            shop = Point(float(lon), float(lat))
            if any(p.contains(shop) for p in polygons):
                shops_in_norway.append((lon, lat))
             
    # save result to file   
    with open("grøtris/butikker_norge.txt", "w") as f:
        for shop in shops_in_norway:
            f.write(f"{shop[0]}, {shop[1]}\n")
        


def main():
    find_shops_in_norway()
    
    G = nx.Graph()
    shops = [tuple(map(float, line.split(", "))) for line in open("grøtris/butikker_norge.txt").read().rstrip().split("\n")]
    
    for shop1 in shops:
        for shop2 in shops:
            if shop1 == shop2:
                continue
            G.add_edge(shop1, shop2, w=dist(*shop1, *shop2))
            
    nort_pole = (0.0, 90.0)
    G.add_node(nort_pole)
    for node in G.nodes:
        G.add_edge(nort_pole, node, w=dist(*nort_pole, *node))
    
    best_path = []
    best_weight = float("inf")
    for path in tqdm(itertools.permutations(shops)):
        path = list(path)
        path.insert(0, nort_pole)
        path.append(nort_pole)
        w = nx.path_weight(G, path, weight="w")
        if w < best_weight:
            best_weight = w
            best_path = path
    
    res = ""
    for long, lat in best_path[::-1]: # the mirrored path is the correct one
        res += f"({int(lat * 1000) / 1000:.3f},{int(long * 1000) / 1000:.3f}),"
    print(res)

main()
        