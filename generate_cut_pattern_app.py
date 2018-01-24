import timeit

from cutting_pattern import CuttingPattern

if __name__ == "__main__":
    print("Generating pattern for log's cutting.")
    print("Needed data size [m] and quantity [pieces] e.g. 1.5, 10")
    pair_of_data = input("How many pairs of data [size, quantity] you "
                         "have?: ")
    size_list = []
    quantity_list = []

    for i in range(int(pair_of_data)):
        size, quantity = input("Enter size, quantity: ").split(',')
        if float(size) > 0 and int(quantity) > 0:
            size_list.append(float(size))
            quantity_list.append(int(quantity))
        else:
            print("Enter correct data!")
            size, quantity = input("Enter size, quantity: ").split()

    cut_width = input("\nEnter cut width [mm]: ")
    cut_width = float(cut_width)
    log_length = input("\nEnter the length of the log [m]: ")
    print("")

    c_pattern = CuttingPattern(size_list, quantity_list, cut_width, log_length)

    # start time measurement for prepare_pattern method
    start_time = timeit.default_timer()
    pieces = c_pattern.prepare_pieces()
    pattern = c_pattern.prepare_pattern(pieces)
    # end time measurement and print result
    print('Time: ', timeit.default_timer() - start_time)

    logs = len(pattern)
    print('\nYou need to prepare: {} logs.'.format(logs))
    c_pattern.print_pattern()
