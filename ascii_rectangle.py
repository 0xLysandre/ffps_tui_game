from time import sleep

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.presence = False

    def __str__(self):
        if self.presence:
            return "[x]"
        return "[ ]"


def delay_print(txt:str)->None:
    for char in txt:
        print(char,flush=True,end=' ')
        sleep(0.1)

def ascii_rectangle():
    SEP = "===="
    MID_GAP = " " * 11

    row0 = [Cell(0, c) for c in range(5)]
    row1 = [Cell(1, 0), Cell(1, 1), None, Cell(1, 3), Cell(1, 4)]
    row2 = [Cell(2, c) for c in range(5)]

    full_line = lambda cells: SEP.join(str(c) for c in cells)
    pipe_line = " |" + "      |" * 4

    mid_line = (
        str(row1[0]) + SEP + str(row1[1])
        + MID_GAP
        + str(row1[3]) + SEP + str(row1[4])
    )

    return (
        full_line(row0) + "\n"
        + pipe_line + "\n"
        + mid_line + "\n"
        + pipe_line + "\n"        
        + full_line(row2) + "\n"
    )


if __name__ == "__main__":
    print(ascii_rectangle())
