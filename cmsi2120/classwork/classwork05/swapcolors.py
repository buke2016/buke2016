def swap_color(color: list[int]) -> list[int]:
    n = len(color)
    i = 1
    firstcolor = color[0]
    lastcolor = color[n-1]

    while i < n-1:
        if firstcolor > lastcolor:
            firstcolor, lastcolor = lastcolor, firstcolor
        i += 1
        firstcolor = color[i]
        lastcolor = color[n-i]

    color[0] = firstcolor
    color[n-1] = lastcolor
    return color

my_color = [2,0,2,1,1,0]
swap_color(my_color)
print(my_color)