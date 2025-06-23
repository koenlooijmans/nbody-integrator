import numpy as np

class PlummerSphere(object):
		
	def __init__(self, N, cluster_mass, cluster_radius, savefile=None):
		self.positions = self.generate_positions(N, cluster_radius)
		self.velocities = self.generate_velocities(N, cluster_radius)
		self.masses = cluster_mass / N * np.ones(shape=N)
		self.N = N


	def generate_positions(self, N, cluster_radius):
		phis = np.random.uniform(0, 2 * np.pi, size=N)
		thetas = np.arccos(np.random.uniform(-1, 1, size=N))
		rs = cluster_radius / np.sqrt(np.random.uniform(0, 1) ** (-2. / 3) - 1)

		xs = rs * np.sin(phis) * np.cos(thetas)
		ys = rs * np.sin(phis) * np.sin(thetas)
		zs = rs * np.cos(phis)

		positions = np.array([xs, ys, zs]).T
		return positions

	def generate_velocities(self, N, cluster_radius):
		potential = 1.0/np.sqrt(np.sum(self.positions**2, axis=-1) + cluster_radius**2)
		v_esc = np.sqrt(2 * potential)

		rejected_samples = np.ones(N, dtype=bool)
		v = np.zeros(N, dtype=float)

		while rejected_samples.any():
			X = np.random.uniform(0, 1, size=N)
			v[rejected_samples] = X[rejected_samples] * v_esc[rejected_samples]
			E = potential - 0.5 * v**2
			f_E = E**3.5
			Y = np.random.uniform(0, 1, size=N)
			accepted = (f_E > Y)
			rejected_samples = np.logical_and(rejected_samples, ~accepted)

		phis = np.random.uniform(0, 2 * np.pi, size=N)
		thetas = np.arccos(np.random.uniform(-1, 1, size=N))

		vxs = v * np.sin(phis) * np.cos(thetas)
		vys = v * np.sin(phis) * np.sin(thetas)
		vzs = v * np.cos(phis)

		velocities = np.array([vxs, vys, vzs]).T
		return velocities