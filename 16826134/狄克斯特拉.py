graph ={}
graph["a"]={}
graph["a"]["b"]=0
graph["a"]["f"]=5
graph["f"]={}
graph["f"]["c"]=20
graph["f"]["e"]=15
graph["b"]={}
graph["b"]["e"]=30
graph["b"]["c"]=35
graph["e"]={}
graph["e"]["d"]=30
graph["c"]={}
graph["c"]["d"]=25
graph["d"]={}

"""a :music score b:post c:drun d:piano e:guiter f:fisc  """

costs ={}
infinity =float("inf")
costs["b"]=infinity
costs["c"]=infinity
costs["d"]=infinity
costs["e"]=infinity
costs["f"]=infinity



parents ={}
parents["b"]={}
parents["c"]={}
parents["d"]={}
parents["e"]={}
parents["f"]={}

processed=[]
def f(costs):
    lowest=float("inf")
    lowestnode=None
    for node in costs:
        cost =costs[node]
        if cost <lowest and node not in processed:
            lowest=cost
            lowestnode=node
    return lowestnode


node =f(costs)
while node is not None:
    cost=costs[node]
    nei=graph[node]
    for n in nei.keys():
        newcost =cost +nei[n]
        if costs[n] > newcost:
            parents[n]=node
    processed.append(node)
    node=f(costs)
