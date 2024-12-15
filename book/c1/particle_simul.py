import time
from random import uniform

from line_profiler import profile
from matplotlib import animation
from matplotlib import pyplot as plt


def timeit(fn):
    # *args and **kwargs are to support positional and named arguments of fn
    def get_time(*args, **kwargs):
        start = time.time()
        output = fn(*args, **kwargs)
        print(f"Time taken in {fn.__name__}: {time.time() - start:.7f}")
        return output  # make sure that the decorator returns the output of fn

    return get_time


class Particle:
    """Particle simulation

    Attr:
        - x, y: define the position of the particle
        - ang_vel: angular velocity of the particle
        All sign of the attr are accepted, for ang_vel, it's the
        directtion of the particle.

    """

    __slots__ = ("x", "y", "ang_vel")

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


class ParticleSimulator:
    """Encapsulating the laws of motion, responsible for changing
    the positions of the particles over time.

    Attr:
        - particles: Particles to be simulated

    Method:

        - evolve(): evolving motion of the particles over a time `dt`

    """

    def __init__(self, particles):
        self.particles = particles

    @profile
    @timeit
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

    @timeit
    def evolve_fast(self, dt):
        timestep = 0.000_01
        nsteps = int(dt / timestep)

        # Loop order is changed
        for p in self.particles:
            t_x_ang = timestep * p.ang_vel
            for i in range(nsteps):
                norm = (p.x**2 + p.y**2) ** 0.5
                p.x, p.y = (p.x - t_x_ang * p.y / norm, p.y + t_x_ang * p.x / norm)


def visualize(simulator):
    """Animate the motion of particles in x, y coordinate"""

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

    def animate(_):
        # we let the particle evolve for 0.01 time units
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return (line,)

    # call the animate function for each 10ms
    _ = animation.FuncAnimation(
        fig, animate, init_func=init, blit=True, interval=10
    )  # _ to pass ruff F841
    plt.show()


def test_visualize():
    """Simulating 3 particles"""
    particles = [
        Particle(0.3, 0.5, 1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, 3),
    ]

    simulator = ParticleSimulator(particles)
    visualize(simulator)


def test_evolve():
    """Test if evolve() method of ParticleSimulator is functioning
    correctly"""

    particles = [
        Particle(0.3, 0.5, 1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, 3),
    ]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)

    p0, p1, p2 = particles

    def fequal(a, b, eps=1e-5):
        return abs(a - b) < eps

    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)
    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y, -0.490034)
    assert fequal(p2.x, 0.191358)
    assert fequal(p2.y, -0.365227)


def benchmark():
    particle = [
        Particle(
            uniform(-1.0, 1.0),
            uniform(-1.0, 1.0),
            uniform(-1.0, 1.0),
        )
        for i in range(1000)
    ]

    simulator = ParticleSimulator(particle)
    simulator.evolve(0.1)
    simulator.evolve_fast(0.1)


def benchmark_memory():
    particle = [
        Particle(
            uniform(-1.0, 1.0),
            uniform(-1.0, 1.0),
            uniform(-1.0, 1.0),
        )
        for i in range(100000)
    ]

    simulator = ParticleSimulator(particle)
    simulator.evolve(0.001)


if __name__ == "__main__":
    benchmark_memory()
