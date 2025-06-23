from leapfrog import LeapfrogIntegrator
from settings import *
from plummer_sphere import PlummerSphere

import matplotlib.pyplot as plt

def main():
	planetary_system = PlummerSphere(n_stars, cluster_mass, cluster_radius)
	integrator = LeapfrogIntegrator(planetary_system)

	positions = []
	velocities = []

	while integrator.time < simulation_time:
		integrator.evolve(timestep)
		positions.append(integrator.get_positions())
		velocities.append(integrator.get_velocities())
		print(integrator.time)

	positions = np.array(positions)
	velocities = np.array(velocities)

	for i in range(n_stars):
		plt.plot(positions[:, i, 0], positions[:,i, 1])
	plt.show()

if __name__ == '__main__':
	main()