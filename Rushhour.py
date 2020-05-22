from solver import Solver

# Put your own data into `board_data` var.
# `rr` - means red car to be freed.
# Cars should use unique characters,
# so if you have AA car, do not repeat A char again.
# Red car can have exit only on the right side of the board.
board_data = '''
    ....AA
    ..BBCC
    rr..EF
    GGHHEF
    ...IEF
    ...IJJ
'''

solver = Solver()
solver.load_data(board_data)
print 'Loaded data'
print solver.format_data(solver.cars)
print 'Looking for solution.. (may take several secods)'
moves = solver.solve()
print solver.format_steps(solver.cars, moves)
