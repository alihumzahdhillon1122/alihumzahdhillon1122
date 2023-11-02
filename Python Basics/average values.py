import numpy as np

# Input for design_bed_level
design_bed_level = float(input("Enter design_bed_level: "))

# List of values
values = [603.39, 603.56, 603.59, 603.79, 603.79, 603.89, 604.19]

# Calculate the average of values
average = np.mean(values)

# Initialize a list to store the results
results = []

# Calculate the difference for each element in values
for value in values:
    result = average - design_bed_level
    results.append(result)

# Print the results
print(results)