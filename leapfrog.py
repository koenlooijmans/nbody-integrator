import gravity

class LeapfrogIntegrator(object):
	def __init__(self, particles):
		self.particles = particles
		self.time = 0
		self.previous_acceleration = gravity.get_acceleration(self.particles)

	def evolve(self, timestep):
		self.particles.positions += self.particles.velocities * timestep + 0.5 * self.previous_acceleration * timestep**2
		next_acceleration = gravity.get_acceleration(self.particles)
		self.particles.velocities += 0.5 * (self.previous_acceleration + next_acceleration) * timestep
		self.previous_acceleration = next_acceleration.copy()

		self.time += timestep

	def get_positions(self):
		return self.particles.positions.copy()

	def get_velocities(self):
		return self.particles.velocities.copy()