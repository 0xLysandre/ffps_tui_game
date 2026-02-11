def ascii_rectangle():
    full_row = "[ ]====[ ]====[ ]====[ ]====[ ]"
    pipe_row = " |      |      |      |      |"
    mid_row  = "[ ]====[ ]           [ ]====[ ]"

    return (
        full_row + "\n" +
        pipe_row + "\n" +
        mid_row + "\n" +
        full_row + "\n"
    )


if __name__ == "__main__":
    print(ascii_rectangle())
