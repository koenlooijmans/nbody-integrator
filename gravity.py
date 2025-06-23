from settings import *

#Assumes G = 1

def get_acceleration(particles):
	dr = particles.positions[:, np.newaxis, :] - particles.positions
	dr2 = np.sum(dr**2, axis=-1) + eps2
	np.fill_diagonal(dr2, np.inf) #Set the diagonal to inf to zero out any self-interaction
	inv_dr3 = 1.0/dr2**1.5
	acc = -dr * particles.masses[np.newaxis, :, np.newaxis] * inv_dr3[:, :, np.newaxis]
	total_acceleration = np.sum(acc, axis=1)
	return total_acceleration


def get_potential_energy(particles):
	dr = particles.positions[:, np.newaxis, :] - particles.positions
	dr2 = np.sum(dr**2, axis=-1) + eps2
	np.fill_diagonal(dr2, np.inf)  # Set the diagonal to inf to zero out any self-interaction
	inv_dr = 1.0/np.sqrt(dr2)
	potential = -particles.masses[np.newaxis, :, np.newaxis] * inv_dr[:, :, np.newaxis]
	total_potential = np.sum(potential, axis=1)
	return total_potential
