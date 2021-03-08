"""Range example."""

start: int = 0
stop: int = 100
step: int = 10

a_range: range = range(start, stop, step)
print(a_range.start)
print(a_range.stop)
print(a_range.step)

a_range = range(10, 100) # default step valie is 1
print(a_range)
a_range = range(10) # Stop is 10, start is 1 by default, and step is 1 by default
print(a_range)