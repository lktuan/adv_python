from matplotlib import animation
from matplotlib import pyplot as plt


class Particle:
    """Particle simulation

    Attr:
        - x, y: define the position of the particle
        - ang_vel: angular velocity of the particle
        All sign of the attr are accepted, for ang_vel, it's the
        directtion of the particle.

    """

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


class ParticleSimulator:
    """Encapsulating the laws of motion, responsible for changing
    the positions of the particles over time.

    """

    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.000_01
        nsteps = int(dt / timestep)

        for i in range(nsteps):
            for p in self.particles:
                # 1. calculate the direction
                norm = (p.x**2 + p.y**2) ** 0.5
                v_x = -p.y / norm
                v_y = p.x / norm

                # 2. calculate the displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y

                # 3. repeat for all the time steps


def visualize(simulator):

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect="equal")
    (line,) = ax.plot(X, Y, "ro")

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # It will be run when the animation starts
    def init():
        line.set_data([], [])
        return (line,)  # the comma is important!

    def animate(i):
        # we let the particle evolve for 0.01 time units
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return (line,)

    # call the animate function for each 10ms
    anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True, interval=10)
    plt.show()


def test_visualize():
    particles = [
        Particle(0.3, 0.5, 1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, 3),
    ]

    simulator = ParticleSimulator(particles)
    visualize(simulator)


if __name__ == "__main__":
    test_visualize()
