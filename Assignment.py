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
