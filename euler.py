import gravity

class EulerIntegrator(object):
	def __init__(self, particles):
		self.particles = particles
		self.time = 0

	def evolve(self, timestep):
		acceleration = gravity.get_acceleration(self.particles)
		self.particles.velocities += acceleration * timestep
		self.particles.positions += self.particles.velocities * timestep
		self.time += timestep

	def get_positions(self):
		return self.particles.positions.copy()

	def get_velocities(self):
		return self.particles.velocities.copy()