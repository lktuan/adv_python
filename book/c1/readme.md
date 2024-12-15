# c1: Benchmarking and Profiling

How to assess the performance of Python programs & how to identify and isolate the slow sections of your code.

## 1 designing your application

Make it run, make it right (re-factoring), make it fast (optimization), in that order.

We constructed an object `Particle` representing the particle in reality, and `ParticleSimulator` representing the motion of it. A particle just constantly rotates **perpendicularly** around a central point ~ like a hand of a clock.

Visualize the simulation, run:

```bash
python .\book\c1\particle_simul.py
```

## 2 writing tests and benchmarks

- a test checks whether the results produced is correct or not;
- a benchmark assess the application in term of running time efficiency.

We can write test functions for specific functions to check if they produce the same output with desireable results.

For benchmarking, the simplest way is to use the `time` command for Unix-like OS. In Window, we can you `cygwin` shell, or `Measure-Command` in PowerShell.

Another approach is using `timeit` built-in Python. We can use it in either Python/Ipython Interface or CLI.

## 3 writing better tests and benchmarks with `pytest-benchmark`

The modern approach is to use `pytest` for testing and `pytest-benchmark` for benchmarking.

```bash
# syntax: pytest path/to/module.py::function_name
pytest book\c1\test_simul.py::test_evolve
```

We include `benchmark()` function to test functions and the benchmarking will be covered in `pytest` command:

```python
def test_evolve(benchmark): # as an argument!
    # ... previous code
    benchmark(simulator.evolve, 0.1)
```

## 4 finding bottlenecks with `cProfile`

After testing and benchmarking our code, we are ready to indentify parts of code that need to be tuned for performance. Python provides 2 profiling modules as standard:

- `profile` module: written in pure Python and adds significant overhead.
- `cProfile` modeul: writtend in C, small overhead.

`cProfile`  can be used in CLI, with IPython, or as a Python module. Actually observing the output of `cProfile`/`%prun`, etc is daunting. But we noticed that `evovle` is the most time consuming function.

There is also a graphical way to assess our parts of code: **KCachegrind** with `pyprof2calltree` package.

We will dive into method with `line_profiler`, first we must decorate our function `evolve`:


```python
from line_profiler import profile

@profile
def evolve(self, dt):
    # code
```

and run with `kernprof`

```bash
python -m kernprof -l -v  .\book\c1\particle_simul.py
# -l to use line profiler
# -v to immediately print the result to the screen
# this also make a binary .py.lprof file
```

The output is:

```md
Wrote profile results to particle_simul.py.lprof
Timer unit: 1e-06 s

Total time: 27.2929 s
File: .\book\c1\particle_simul.py
Function: evolve at line 42

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    42                                               @profile
    43                                               def evolve(self, dt):
    44         1          0.5      0.5      0.0          timestep = 0.000_01
    45         1          2.3      2.3      0.0          nsteps = int(dt / timestep)
    46
    47     10001       3080.5      0.3      0.0          for i in range(nsteps):
    48  10010000    2381595.5      0.2      8.7              for p in self.particles:
    49                                                           # 1. calculate the direction
    50  10000000    6832873.2      0.7     25.0                  norm = (p.x**2 + p.y**2) ** 0.5
    51  10000000    2969509.8      0.3     10.9                  v_x = -p.y / norm
    52  10000000    2677994.6      0.3      9.8                  v_y = p.x / norm
    53
    54                                                           # 2. calculate the displacement
    55  10000000    3009884.5      0.3     11.0                  d_x = timestep * p.ang_vel * v_x
    56  10000000    2973172.5      0.3     10.9                  d_y = timestep * p.ang_vel * v_y
    57
    58  10000000    3244962.8      0.3     11.9                  p.x += d_x
    59  10000000    3199775.3      0.3     11.7                  p.y += d_y
    60
    61                                                           # 3. repeat for all the time steps
```

By looking at `%Time` column, we can have a good idea of somewhat a few statements in for loop are consuming most of cost. 

## 5 optimizing your code

There are multiple ways to optimize our code:

- change the algo: express the motion in terms of radius (more correct);
- pre-calculate parts that do not change over time, outside the loop;
- reduce the assignment operators.

We end up writing `evolve_fast` function. I also use a `timeit` decorator to measure and compare the time consumed for 2 versions (suggested by [HuyenChip](https://github.com/chiphuyen/python-is-cool?tab=readme-ov-file#6-decorator-to-time-your-functions)). The by simply run:

```python
python .\book\c1\particle_simul.py
# Time taken in evolve: 5.4799218
# Time taken in evolve_fast: 4.5114696
```

The speed improved near 20%.

## 6 using `dis` module

We will be more delve into how Python code is interpreted into **bytecode** in CPython interpreter using `dis` module - **disassemble**.

Jump into interative mode by:

```bash
ipython -i .\book\c1\particle_simul.py 
```

then:

```python
In [1]: import dis
In [2]: dis.dis(ParticleSimulator.evolve)
```

this will print, for each line in the function, a list of bytecode instructions. By inspecting the number of bytecode instructions, we can further optimize our Python code by reducing it.

## 7 profiling memory usage with `memory_profiler`

After time complexity, we are continuing to investigate memory complexicty. Same with `line_profiler`, we also decorate the function with `@profile`. We adjust the numder of particles to 100_000, and reduce the evolving time. Then using the `%mprun` magic in IPython, we can obtain statistics about memory usage:

```Python
In [1]: %load_ext memory_profiler
In [2]: %mprun -f benchmark_memory benchmark_memory()
```

below is the result:

```md
Time taken in evolve: 35.2993779
Filename: C:\Users\Tuan Le\git\adv_python\book\c1\particle_simul.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   176     95.1 MiB     95.1 MiB           1   def benchmark_memory():
   177    115.5 MiB      1.5 MiB      200004       particle = [
   178    115.5 MiB     13.7 MiB      200000           Particle(
   179    115.5 MiB      0.0 MiB      100000               uniform(-1.0, 1.0),
   180    115.5 MiB      0.0 MiB      100000               uniform(-1.0, 1.0),
   181    115.5 MiB      3.1 MiB      100000               uniform(-1.0, 1.0),
   182                                                 )
   183    115.5 MiB      2.1 MiB      100001           for i in range(100000)
   184                                             ]
   185
   186    115.5 MiB      0.0 MiB           1       simulator = ParticleSimulator(particle)
   187    115.4 MiB     -0.1 MiB           1       simulator.evolve(0.001)
```

We can see now 100k particles consumed 13.7 MiB (not MB) memory. We can use `__slots__` dunder method to avoid storing variables of the instance in an internal memory. 

## Summary

- testing and benchmarking: `pytest`, `pytest-benchmarking`;
- profiling: `cProfile`, `line_profiler`, `memory_profiler`.


