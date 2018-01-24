class CuttingPattern(object):
    """
    Class to determine number of standard lumber pieces are required to
    complete an order where size, quantity, cut width, length of the log are
    known.
    """
    def __init__(self, size_list, quantity_list, cut_width, log_length):
        # list of the sizes
        self.size = size_list
        # list of quantity
        self.quantity = quantity_list
        # width of cut
        self.cut_width = cut_width / 1000
        # list of single pieces
        self.pieces = []
        # length of the log
        self.log_length = float(log_length)
        # number of needed logs
        self.logs = 0
        # remaining after cutting
        self.remaining = []
        # list with final cutting pattern
        self.final_pattern = [[]]

    def prepare_pieces(self):
        """Prepare list of single pieces """
        self.pieces = []
        for j in range(len(self.size)):
            for i in range(self.quantity[j]):
                self.pieces.append(self.size[j])
        return self.pieces

    def prepare_pattern(self, pieces):
        """Using first-fit decreasing (FFD) heuristic method prepares
        pattern."""
        self.pieces = pieces
        self.remaining = [self.log_length]
        for element in sorted(self.pieces, reverse=True):
            if element < self.log_length:
                for j, free_space in enumerate(self.remaining):
                    if free_space >= element:
                        self.remaining[j] -= (self.cut_width + element)
                        self.final_pattern[j].append(element)
                        break
                else:
                    self.final_pattern.append([element])
                    self.remaining.append(self.log_length-self.cut_width-element)
            else:
                print("Can't prepare cut pattern for size {} because we don't "
                      "have such a long log.".format(element))
        return self.final_pattern

    def print_pattern(self):
        self.final_pattern
        for i in range(len(self.final_pattern)):
            log_number = i + 1
            print('Cutting pattern for log nr {} - {}'.format(
                log_number,
                self.final_pattern[i])
            )
