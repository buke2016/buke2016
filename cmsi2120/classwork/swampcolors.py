def swap_color(color):
    n = len(color)
    i = 1
    firstcolor = color[0]
    lastcolor = color[n - 1]

    while i < n - 1:
        if firstcolor > lastcolor:
            firstcolor, lastcolor = lastcolor, firstcolor
        else:
            color[i], color[n - i] = color[n - i], color[i]
        i += 1
        firstcolor = color[i]
        lastcolor = color[n - i - 1]

    color[0], color[n - 1] = firstcolor, lastcolor