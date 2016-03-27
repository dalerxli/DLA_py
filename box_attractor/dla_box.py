import random as rd
import matplotlib.pyplot as plt
import numpy as np
import time
import csv

class dla(object):
	def __init__(self, N, m):
		self.size = N
		self.arena = [[0 for i in xrange(N)] for j in xrange(N)]
		for j in range(N):
			self.arena[j][0] = 1
		for j in range(N):
			self.arena[0][j] = 1
		for j in range(N):
			self.arena[j][N-1] = 1
		for j in range(N):
			self.arena[N-1][j] = 1
		self.particles = m
	
	def start(self, edge):
		return (self.size/2, self.size/2)
	
	def neighbours(self, pos):
		l = [(pos[0], (pos[1]-1)%N), ((pos[0]-1)%N, pos[1]), (pos[0], (pos[1]+1)%N), ((pos[0]+1)%N, pos[1])]
		return l
	
	def walk(self, seed):
		while(True):
			ney = self.neighbours(seed)
			for x in ney:
				if(self.arena[x[0]][x[1]]==1):
					self.arena[seed[0]][seed[1]] = 1
					self.particles -= 1
					return seed
			seed = ney[rd.randint(0,len(ney)-1)]
	
	def simulate(self):
		while(self.particles>0):
			t0 = time.time()
			print self.particles
			edge = 1
			seed = self.start(edge)
			seed = self.walk(seed)
			u = time.time()-t0
			t.append(u)
			data.writerow([m-self.particles, u, seed[0], seed[1]])

t = []
N = 500
m = 25000

output = open('times.csv', 'w+')
data = csv.writer(output)
data.writerow(['Particle#', 'Stick Time', 'Row', 'Column'])

model = dla(N, m)
model.simulate()

plt.imshow(np.asmatrix(model.arena), cmap = 'prism')
plt.show()

plt.plot(range(1, len(t)+1), t)
plt.show()
