import numpy as np

class PlanetarySystem(object):
	'''
	Generates a simple planetary system for testing purposes
	'''
	def __init__(self, N):
		self.N = N
		self.masses = self.masses = 1e-4 / (N - 1) * np.ones(shape=N)
		self.masses[0] = 0.9999

		self.positions = np.zeros((N, 3))
		self.velocities = np.zeros((N, 3))

		for i in range(1, N):
			r = np.random.uniform(1e-3, 2)
			phi = np.random.uniform(0, 2 * np.pi)
			x = r * np.cos(phi)
			y = r * np.sin(phi)
			v = np.sqrt(self.masses[0]/r)
			vx = v * -y/r
			vy = v * x/r

			self.positions[i] = np.array([x, y, 0])
			self.velocities[i] = np.array([vx, vy, 0])