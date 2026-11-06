def draw_pattern(n):
    if n == 0:
        #When n reaches 0, the function stops calling itself.
        return

    print("*" * n)
    draw_pattern(n - 1)
    #print("*" * n) prints the number of stars equal to n.
    #draw_pattern(n - 1) calls the function again with a smaller number.
    print("*" * n)


draw_pattern(3)
#Code after the recursive call executes in reverse order because each function has to finish its recursive call before continuing. The most recent function call finishes first, and then the program works its way backward through the earlier calls. This is called unwinding recursion.