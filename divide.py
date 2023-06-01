import json
import os
import numpy as np
import matplotlib.pyplot as plt

opening_data = []
middle_data = []
endgame_data = []

# Update the range based on the total number of game files
for i in range(2, 40):
    # Construct the file name
    file_name = f"game_{i}.json"

    # Read the JSON file
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
            list_string = data[0]

            # Remove the surrounding square brackets
            list_string = list_string.strip("[]")

            # Convert the string into a list of integers
            cop_values = [float(x) for x in list_string.split(",")]

            # Extract values for each stage
            opening_values = [v for v in cop_values[:30] if 0 < v]
            middle_values = [v for v in cop_values[90:120] if 0 < v]
            endgame_values = [v for v in cop_values[-30:] if 0 < v]

            # Add extracted values to the corresponding lists
            opening_data.extend(opening_values)
            middle_data.extend(middle_values)
            endgame_data.extend(endgame_values)
    else:
        print(f"File {file_name} not found.")

# Convert the lists to numpy arrays for further analysis
opening_data = np.array(opening_data)
middle_data = np.array(middle_data)
endgame_data = np.array(endgame_data)

# Save the data as a JSON file
data_to_save = {
    "opening_data": opening_data.tolist(),
    "middle_data": middle_data.tolist(),
    "endgame_data": endgame_data.tolist()
}

with open("cop_data.json", "w") as outfile:
    json.dump(data_to_save, outfile)

# Print the results


cop = middle_data
moves=list(range(0, len(middle_data)))
x = np.arange(0,len(middle_data),40)
plt.bar(moves,cop,color=['black'], width = 0.5)
plt.xticks(x)
plt.xlabel('total moves')
plt.ylabel('cop')
plt.title('opening')

plt.show()