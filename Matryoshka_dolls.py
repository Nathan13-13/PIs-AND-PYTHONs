def open_doll(doll):
    if doll["inner_doll"] is None:
        return doll["size"]
#This checks whether the doll has another doll inside it.
    return open_doll(doll["inner_doll"])
    #The integer travels back through the recursive calls using the return statement. Each function call passes the result back to the previous call until it eventually reaches the original function. This allows the original function to receive the final size.
