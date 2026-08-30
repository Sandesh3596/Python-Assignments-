data = [6, 7, 8, 9, 10, 11, 12]

mean = 9
standard_deviation = 2

scaled_values = [(x - mean) / standard_deviation for x in data]

print("Scaled Values:", scaled_values)