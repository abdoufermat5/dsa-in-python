def draw_line(tick_length, tick_label=None):
    """Draw one line with given tick length followed by optional label"""

    line = "-" * tick_length

    if tick_label:
        line += tick_label
    print(line)


def draw_interval(center_length):
    """Draw tick interval based upon a central tick length"""

    if center_length > 0:
        draw_interval(center_length - 1)  # draw top ticks
        draw_line(center_length)  # draw center tick
        draw_interval(center_length - 1)  # draw bottom ticks


def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches and major tick length"""
    draw_line(major_length, "0")
    for j in range(1, num_inches+1):
        draw_interval(major_length-1)
        draw_line(major_length, str(j)) # draw inch j line and label


if __name__ == "__main__":
    draw_ruler(5, 5)
    # output
    # -----0
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # ----1
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # -----2
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # ----3
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # -----4
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # ----5
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # -----6
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # ----7
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # -----8
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # ----9
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # -----10
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # ----11
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # -----12
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # ----13
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # -----14
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # ----15
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # -----16
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # ----17
    # -
    # --
    # -
    # ---
    # -
    # --
    # -
    # -----18
    # -
    # --
    # -
    # ---