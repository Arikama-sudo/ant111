class grid:
    def __init__(self, n=3):
        self.n = n
        self.table = [[((i * n + i / n + j) % (n * n) + 1) for j in range(n * n)] for i in range(n * n)]
        print
        "The base table is ready!"

    def __del__(self):
        pass

    def show(self):
        for i in range(self.n * self.n):
            print
            self.table[i]
    def transposing(self):
		self.table = map(list, zip(*self.table))

    def swap_rows_small(self):
        area = random.randrange(0, self.n, 1)
        line1 = random.randrange(0, self.n, 1)
        N1 = area * self.n + line1
        line2 = random.randrange(0, self.n, 1)
        while (line1 == line2):
            line2 = random.randrange(0, self.n, 1)

        N2 = area * self.n + line2

        self.table[N1], self.table[N2] = self.table[N2], self.table[N1]
    def swap_colums_small(self):
        grid.transposing(self)
        grid.swap_rows_small(self)
        grid.transposing(self)
    def swap_rows_area(self):
        area1 = random.randrange(0, self.n, 1)

        area2 = random.randrange(0, self.n, 1)
        while (area1 == area2):
            area2 = random.randrange(0, self.n, 1)

        for i in range(0, self.n):
            N1, N2 = area1 * self.n + i, area2 * self.n + i
            self.table[N1], self.table[N2] = self.table[N2], self.table[N1]
    def swap_colums_small(self):
        grid.transposing(self)
        grid.swap_rows_area(self)
        grid.transposing(self)
    def mix(self, amt=10):
        mix_func = ['self.transposing()',
                    'self.swap_rows_small()',
                    'self.swap_colums_small()',
                    'self.swap_rows_area()',
                    'self.swap_colums_area()']
        for i in xrange(1, amt):
            id_func = random.randrange(0, len(mix_func), 1)
            eval(mix_func[id_func])
flook = [[0 for j in range(example.n*example.n)] for i in range(example.n*example.n)]
iterator = 0
difficult = example.n ** 4

while iterator < example.n ** 4:
	i,j = random.randrange(0, example.n*example.n ,1), random.randrange(0, example.n*example.n ,1)
	if flook[i][j] == 0:
		iterator += 1
		flook[i][j] = 1

		temp = example.table[i][j]
		example.table[i][j] = 0
		difficult -= 1

		table_solution = []
		for copy_i in range(0, example.n*example.n):
			table_solution.append(example.table[copy_i][:])

		i_solution = 0
		for solution in solver.solve_sudoku((example.n, example.n), table_solution):
			i_solution += 1

		if i_solution != 1:
			example.table[i][j] = temp
			difficult += 1

example.show()
print ("difficult = ",difficult)