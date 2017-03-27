import heapq
class Node:
    name=None
    parent=None
    distance=0
    visited=False
    weight=0
    estdist=0
    sunday_trafficline=0
    def __init__(self,name):
        self.name=name
        
def setstraffic(name):
        for x in objlist:
            if x.name in suntrafficdict:
                x.sunday_trafficline=suntrafficdict[x.name]
def returnstraffic(name):
    for x in objlist:
        if x.name==name:
            return x.sunday_trafficline

def returnobj(objectname):
    for x in objlist:
        if x.name==objectname:
            return x

def backtrace(start,current):
    path=[current.name]
    distance=[current.distance]
    while path[-1] != start.name:
        for i in objlist:
            if i.name==current.parent:
                current=i
                path.append(current.name)
                distance.append(current.distance)
    path.reverse()
    for i in range(0,len(distance)):
        distance[i]=distance[i]-start.distance
    distance.reverse()
    return path, distance   


def bfs(s,end):
    queue=[]
    start=returnobj(s)
    start.distance=0
    start.visited=True
    start.parent=None
    queue.append(start)
    while queue:
        current_node=queue.pop(0)
        presentnode=current_node.name
        if presentnode==end:
          return backtrace(start,current_node)
        else:
          for neighbour in graph[presentnode]:
                 gg=returnobj(neighbour)
                 if gg.visited==False:
                     gg.visited=True
                     gg.parent=presentnode
                     gg.distance=current_node.distance+1
                     queue.append(gg)
    
    if not queue:
        return None, None
   
def dfs(s,end):
    stack=[]
    start=returnobj(s)
    start.distance=0
    start.visited=True
    start.parent=None
    stack.append(start)
    while stack:
        current_node=stack.pop()
        presentnode=current_node.name
        if presentnode==end:
          return backtrace(start,current_node)
        else:
            children=[]
            for neighbour in graph[presentnode]:
                children.append(neighbour)
            children.reverse()    
            for child in children:
                    gg=returnobj(child)
                    if gg.visited==False:
                         gg.visited=True
                         gg.parent=presentnode
                         gg.distance=current_node.distance+1
                         stack.append(gg)
    if not stack:
        return None,None

def ucs(s,end):
    queue=[]
    q=[]
    queue2=[]
    visited=[]
    start=returnobj(s)
    start.parent=None
    start.visited=True
    start.cost=0
    heapq.heappush(queue,[0,start])
    q.append(start)
    while queue:
        i,current_node=heapq.heappop(queue)
        presentnode=current_node.name
        if presentnode==end:
          return backtrace(start,current_node)
        else:
            children=[]
            for neighbour in graph[presentnode]:
                children.append(neighbour)
            while children:
                        child=children.pop(0)
                        childobj=returnobj(child)
                        childobj.parent=current_node.name
                        childobj.visited==True
                        childobj.weight=getdistance(current_node.name,child)
                        childobj.distance=current_node.distance+childobj.weight
                        childobj.sunday_trafficline=returnstraffic(child)
                        if childobj not in visited and childobj not in queue2:
                            heapq.heappush(queue,(childobj.distance,childobj))
                            visited.append(childobj)
                        else:
                          for i,j in queue:
                            if j.name==childobj.name:
                              if childobj.distance<j.distance:
                                 heapq.heappop(queue)
                                 heapq.heappush(queue,(childobj.distance,childobj))
                                 visited.append(childobj)
                                 
                          for i in queue2:
                                if i.name==childobj.name:
                                    if childobj.distance<i.distance:
                                        queue2.remove(i)
                                        heapq.heappush(queue,(childobj.distance,childobj))
                                        visited.append(childobj)
                                        
    queue2.append(current_node)
    if not queue2:
        return None,None

def astar(s,end):
    queue=[]
    q=[]
    queue2=[]
    visited=[]
    start=returnobj(s)
    start.parent=None
    start.visited=True
    start.cost=0
    heapq.heappush(queue,[0,start])
    q.append(start)
    while queue:
        i,current_node=heapq.heappop(queue)
        presentnode=current_node.name
        if presentnode==end:
          return backtrace(start,current_node)
        else:
            children=[]
            for neighbour in graph[presentnode]:
                children.append(neighbour)
            while children:
                        child=children.pop(0)
                        childobj=returnobj(child)
                        childobj.parent=current_node.name
                        childobj.visited==True
                        childobj.weight=getdistance(current_node.name,child)
                        childobj.distance=current_node.distance+childobj.weight
                        childobj.sunday_trafficline=returnstraffic(child)
                        estdist=childobj.distance+childobj.sunday_trafficline
                        if childobj not in visited and childobj not in queue2:
                            heapq.heappush(queue,(estdist,childobj))
                            visited.append(childobj)
                            
                        else:
                          for i,j in queue:
                            if j.name==childobj.name:
                              if childobj.distance<j.distance:
                                 heapq.heappop(queue)
                                 heapq.heappush(queue,(childobj.distance,childobj))
                                 visited.append(childobj)
                                 
                          for i in queue2:
                                if i.name==childobj.name:
                                    if childobj.distance<i.distance:
                                        queue2.remove(i)
                                        heapq.heappush(queue,(childobj.distance,childobj))
                                        visited.append(childobj)
                                        
    queue2.append(current_node)
    if not queue2:
        return None,None
    
graph={}
listofvertices=[]
objlist=[]
dist={}
suntrafficdict={}
def add_vertex(name1,name2):
    if name1 not in graph:
         graph[name1]=[name2]
         listofvertices.append(name1)
    else:
        graph[name1].append(name2)
    if name2 not in graph:
        graph[name2]=[]
        listofvertices.append(name2)
def distancefn(n1,n2,d):
    str1=n1+n2
    dist[str1]=d
def heuristic(name,straffic):
    suntrafficdict[name]=straffic
filename= open('input.txt', 'r')
lines=filename.readlines()
algo=lines[0].rstrip()
source=lines[1].rstrip()
target=lines[2].rstrip()
trafficlines=lines[3].rstrip()
tline=int(trafficlines)
trafficline1=tline+4
sline=lines[trafficline1]
sunday_traffic=int(sline)
huline=trafficline1+sunday_traffic
j=trafficline1+1
for i in range(4,trafficline1):
   node1,node2,d=lines[i].split()
   add_vertex(node1,node2)
   distancefn(node1,node2,int(d))
for l in range(j,huline+1):
    node,st=lines[l].split()
    heuristic(node,int(st))


def getdistance(n1,n2):
        str1=n1+n2
        if str1 in dist:
            return dist[str1]
        else:
            return None
for vertex in listofvertices:
        objlist.append(Node(vertex))
        setstraffic(vertex)
        
def output():
    f=open('output.txt','w')
    if algo=='BFS':
       list1,list2=bfs(source,target)
    elif algo=='DFS':
       list1,list2=dfs(source,target)
    elif algo=='UCS':
        list1,list2=ucs(source,target)
    elif algo=='A*':
        list1,list2=astar(source,target)
    if not list1:
        f.write('0')
    else:
        for i in range(0,len(list1)):
           di=list2[i]
           strdis=str(di)
           f.write(list1[i]+" "+strdis+"\n")
output()
