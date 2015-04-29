import graph_tool.all as gt
import graph_tool
import scipy
from numpy.random import poisson,randint
import time
import math

start = time.time()
def corr(a,b):                                                                                                                                         
    if a==b:
        return 0.999
    else:
        return 0.001
        
g, bm = gt.random_graph(10000000, 
                        lambda: poisson(20), 
                        directed=False,
                        block_membership=lambda: randint(50),
                        vertex_corr=corr)
                        
                        
print(g.num_vertices(), g.num_edges())
pagerank = graph_tool.centrality.pagerank(g)


diff = time.time() - start

nodes = g.num_vertices()
edges = g.num_edges()

filename = 'pagerank_undirected_%dMN_%dME' % (nodes/1000000,edges/1000000)
with open(filename+'.txt','w+') as f:
    f.write("test: %d nodes %d edges\n" % (nodes,edges))

    hours = math.floor(diff/3600.0)
    min = math.floor((diff % 3600)/60.0)
    sec = math.floor((diff % 60))
    
    timetocomplete = "time to complete = %0.0f hrs %0.0f min %0.0f sec\n" % (hours,min,sec)
    print timetocomplete

    f.write(timetocomplete)
    f.write("time=%0.2f seconds\n" % diff)
