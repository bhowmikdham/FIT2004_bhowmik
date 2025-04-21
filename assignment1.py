#approach :
'''
Our Approach is like this :

we have our cyclic loop of train stations , to get where we are we will first calculate the total time to go through one loop.
Now as we have the total time , for any given point of time we can calculkate where we are using the Mod function :

for this we will do :  driven_time mod total_loop_time

this would now give us the node/state where friend would be at on the loop at any point of driven_time

now as we have got this , we would basically craft our graph

our Graph would be structured like this , as now we have three things to worrry about.

Node : location , time mod (to get where would the friend be in the loop)

edge : Cost , time 

why cost and time here : Cost is the primary metric to minimise here and then time ensures correct train schedule alignment 

we would implement our graph using the adjacency list 

When finding an optimal intercept , we will take care of these things:

 * does the location match with the friend
 * is the time taken the same to reach that node as by the friend
 * is path that we chose is the minimal cost path

 We will then pass this graph to dijkstras to get the most optimal path / intercept between driver and the friend

If no such state exists where the driver and friend align on both time and location, the function returns None.

we will use heap for dijsktras 

'''
import heapq
import math 
def compute_time(stations, start_idx):
    '''
    Compute total_loop_time and list_arrival containing the time at when the friend first arrives at a station based on where he starts from.

    stations: list of (location , travel_time)
    start_idx: index where the friend starts from in the stations

    Returns:
        total_loop_time, list_arrival

    Time complexity: O(|T|) here T is number of stations
    Space complexity: O(|T|)
    '''
    #computing total_loop_time
    
    travel_times= [time for _,time in stations]
    total_loop_time=sum(travel_times) #O(n) #this is the time that we will be using as a mod divisor
    
    #computing time to each station 
    n=len(stations)
    current_time=0
    list_arrival = [0] * n
    idx = start_idx
    for _ in range(n):
        list_arrival[idx] = current_time
        current_time += travel_times[idx]
        idx = (idx + 1) % n

    return total_loop_time,list_arrival

def graphing(roads,stations):
    '''
    This function is used here for graphing what we have as adjacency list for maintaining the paths.

    Parameters passed:

        roads: List of tuples (initial_location, next_location, cost, travel_time)
        stations: List of tuples (station_loc, travel_time_to_next)

    Returns:
        graph: List of lists of (neighbor, cost, travel_time)
        loc_to_station: List mapping each location to its station index, or -1

    Time complexity: O(|R| + |L|)  |R| is the number of roads 
    Space complexity: O(|R| + |L|) for adjacency list
    '''
    #for the graph handling we will be makign use of adjacency list which would help in tracking of all the nodes when we pass it to the dijkstras
    max_road_node = max(max(initial_location, next_location) for initial_location, next_location, _, _ in roads)
    max_station_node = max(station_loc for station_loc, _ in stations)
    max_node = max(max_road_node, max_station_node)

    graph = [[] for _ in range(max_node + 1)]

    #here we are populating the road edges
    for initial_location, next_location, cost, travel_time in roads:
        graph[initial_location].append((next_location, cost, travel_time))

    #here we are just making an array that correspondss to the the stations in the graph drafted above
    #we coudl haev either used None here aswell , for that we can also update the if condition in the intercept function
    loc_to_station = [-1] * (max_node + 1)
    for idx, (station_loc, _) in enumerate(stations):
        loc_to_station[station_loc] = idx

    return graph, loc_to_station

def intercept(roads,stations,initial_location,friend_start):
    '''
    Implementing Dijkstra's Algorihtm to get the most cost effective intercept between the driver and the friend

    Data Structure used: Min Heap

    ParameterS:
        roads: list of (initial_location, next_location, cost, travel_time)
        stations: list of (station location, travel time to next location )
        initial_location: starting location of driver
        friend_start: location where friend begins


    Time Complexity:O(|R|*T*log(L*T)) now since T here is the loop durwation , which atmost could just be 20*100 which turnsdown to just a constant value ,
    we can just ignore it and say that the Time complexity is O(|R|*log(L))
    
    Aux Space Complexity: O(|L|*T) + O(|R|) now T again is just a loop duration , which again would just be constant val. we can just say O(|L|)+O(|R|) or just O(|L|+|R|)

    
    '''
    #here we will build the graph
    graph, loc_to_station = graphing(roads, stations)
    if loc_to_station[friend_start] < 0:#checks if the start mentioned as an argument is a station or not [if not return none]
        return None
    
    #Compute time loop of friend using the compute_time fuction
    total_loop_time, list_arrival = compute_time(stations, loc_to_station[friend_start])

    #Dijkstra's implementaion 
    num_locations = len(graph)
    INF = math.inf
    cost_table = [[INF] * total_loop_time for _ in range(num_locations)]
    time_table = [[INF] * total_loop_time for _ in range(num_locations)]
    prev_node = [[-1] * total_loop_time for _ in range(num_locations)]
    prev_time_mod = [[-1] * total_loop_time for _ in range(num_locations)]

    # Min-heap layout: (cost, time, location, time_mod)
    heap = []
    cost_table[initial_location][0] = 0
    time_table[initial_location][0] = 0
    heapq.heappush(heap, (0, 0, initial_location, 0))

    while heap:
        current_cost, current_time, current_loc, time_mod = heapq.heappop(heap)
        if current_cost != cost_table[current_loc][time_mod] or current_time != time_table[current_loc][time_mod]:
            continue
        
        station_idx = loc_to_station[current_loc]
        if station_idx >= 0 and current_time % total_loop_time == list_arrival[station_idx]:#this si where we are checking the intercept
        
            path = []
            loc, mod = current_loc, time_mod
            while loc >= 0:
                path.append(loc)
                next_loc = prev_node[loc][mod]
                mod = prev_time_mod[loc][mod]
                loc = next_loc
            return current_cost, current_time, list(reversed(path)) #why reversed ? this is herew to backtrack the route so that we can display the route

        
        for neighbor, edge_cost, edge_time in graph[current_loc]:
            new_cost = current_cost + edge_cost
            new_time = current_time + edge_time
            new_mod = (time_mod + edge_time) % total_loop_time
            if (new_cost < cost_table[neighbor][new_mod] or
               (new_cost == cost_table[neighbor][new_mod] and new_time < time_table[neighbor][new_mod])):#this is here if we found another better path we will basically update it.
                cost_table[neighbor][new_mod] = new_cost
                time_table[neighbor][new_mod] = new_time
                prev_node[neighbor][new_mod] = current_loc
                prev_time_mod[neighbor][new_mod] = time_mod
                heapq.heappush(heap, (new_cost, new_time, neighbor, new_mod))

    return None #this is here , if the heap empties and doesnt find any intercept it will basically return None