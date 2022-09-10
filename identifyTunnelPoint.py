import numpy as np
import numpy.linalg as LA

def closestNode(node,nodes):
        np.asarray(nodes)
        deltas = nodes - node
        dist2 = np.einsum('ij,ij->i',deltas,deltas)
        return np.argmin(dist2)

def unpack(file): ## .xvg file
	t,x,y,z = np.loadtxt(file,unpack = True,comments = ['@','#'])
	return t,x * 10,y * 10,z * 10

def getCoordinates(file):
	data = open(file,'r').readlines()
	strCoords = []
	for item in data:
		strCoords.append(item.split()[6:9])
	strCoords.pop(0)
	strCoords.pop(-1)

	coordinates = []
	for coordinate in strCoords:
		coordinate = [float(q) for q in coordinate]
		coordinates.append(coordinate)

	def getQ(list,qi):
		return np.array([q[qi] for q in list])
	x = getQ(coordinates,0)
	y = getQ(coordinates,1)
	z = getQ(coordinates,2)

	return coordinates,x,y,z

def getClosestTunnel(xvg,tunnel):
	t,x,y,z = unpack(xvg)
	tunnelNodes,tunX,tunY,tunZ = getCoordinates(tunnel)
	index = closestNode(np.array([x[0],y[0],z[0]]),tunnelNodes)
	#if index + 1 >= len(tunnelNodes):
#	print(tunnelNodes[index])
	return index,np.array(tunnelNodes[index]),np.array(tunnelNodes[index + 1])
	#else:
	#	return index,np.array(tunnelNodes[index]),np.array(tunnelNodes[index])

def getDistance(tunnel):
	tN,tunX,tunY,tunZ = getCoordinates(tunnel)
	distances = [0]
	for i in range(1,len(tN)):
		dist = LA.norm(np.array(tN[i]) - np.array(tN[i - 1]))
		distances.append(dist)
	return np.cumsum(distances)
