def choose_pizza(x):
#reading input file
	fp = open(x)

	filedata= fp.readlines()
	max_slices_allowed , pizzatypes = filedata[0].rstrip().split(" ")
	max_slices_allowed = int(max_slices_allowed)
	pizzatypes = int(pizzatypes)

	ipline2 = filedata[1].rstrip().split(" ")
	slices_in_each_type = list(map(int, ipline2))
#input file loaded, finding value near max slices allowed
	index = 0
	estimate = slices_in_each_type[index]
	while estimate<max_slices_allowed:
		index = index + 1
		estimate = estimate + slices_in_each_type[index]
	buying_pizzatypes = list(range(0,index+1))

#found a value near max slices. checking the value
	if estimate == max_slices_allowed:
		pass
	else:
		excess_slices = estimate-max_slices_allowed
		for a in slices_in_each_type:
			if a>excess_slices:
				to_be_removed = a
				index_rem = slices_in_each_type.index(a)
				estimate = estimate-a
				break
		buying_pizzatypes.remove(index_rem)

	submit = open("output_"+x,"w+")
	submit.write(str(len(buying_pizzatypes))+"\n")
	for a in buying_pizzatypes:
		submit.write(str(a)+" ")
	submit.close()


choose_pizza('a_example.in')
choose_pizza('b_small.in')
choose_pizza('c_medium.in')
choose_pizza('d_quite_big.in')
choose_pizza('e_also_big.in')