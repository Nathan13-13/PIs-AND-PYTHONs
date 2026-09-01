def calculate_mars_weight(weight):
    weight = (weight * 0.378)
    return(weight) 

e_weight = int(input("Earth Weight: "))
m_weight = calculate_mars_weight(e_weight)
print(f"Mars Weight: {m_weight}")





