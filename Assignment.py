#approach :
'''
Our Approach is like this :

we have our cyclic loop of train stations , to get where we are we will first calculate the total time to go through one loop.
Now as we have the total time , for any given point of time we can calculkate where we are using the Mod function :

for this we will do :  driven_time mod total_loop_time

this would now give us the node/state where friend would be at on the loop at any point of driven_time

now as we have got this , we would basically craft our graph

our Graph would be structured like this , as now we have three things to worrry about.

Node : location + time

edge : Cost (basically cost would be our weight)

When finding an optimal intercept , we will take care of these things:

 * does the location match with the friend
 * is the time taken the same to reach that node 
 * is path that we chose is the minimal cost path

 We will then pass this graph to dijkstras to get the most optimal path / intercept between driver and the friend

If no such state exists where the driver and friend align on both time and location, the function returns None.

'''
def compute_time(stations, start_idx):
    '''
    Compute total_loop_time and list_arrival containing the time at when the friend first arrives at a station based on where he starts from.

    stations: list of (location , travel_time)
    start_idx: index in stations where friend starts

    Returns:
        total_loop_time, list_arrival
    '''
    #computing total_loop_time
    
    travel_times= [time for _,time in stations]
    total_loop_time=sum(travel_times) #O(n) #this is the time that we will be using as a mod divisor
    
    #computing time to each station 
    n=len(stations)
    list_arrival=[]
    for time in range(len(stations)):
        time_to_station=0
        for j in range(time):
            index=(start_idx+j)%n
            time_to_station += travel_times[idx]
        list_arrival.append(time_to_station)

    return total_loop_time,list_arrival

def graph(roads,stations):
    '''
    
    '''
    #for the graph handling we will be makign use of adjacency list which would help in tracking of all the nodes when we pass it to the dijkstras
    max_road_node = max(max(initial_location, next_location) for initial_location, next_location, _, _ in roads)
    max_station_node = max(station_loc for station_loc, _ in stations)
    max_node = max(max_road_node, max_station_node)

    graph = [[] for _ in range(max_node + 1)]

    #here we are populating the road edges
    for initial_location, next_location, cost, travel_time in roads:
        graph[initial_location].append((next_location, cost, travel_time))

    #here we are just making an array that corresponds to the the station
    loc_to_station = [-1] * (max_node + 1)
    for idx, (station_loc, _) in enumerate(stations):
        loc_to_station[station_loc] = idx

    return graph, loc_to_station

def intercept()
    
