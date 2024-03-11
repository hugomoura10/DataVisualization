import matplotlib.pyplot as plt
import numpy as np

layers = [['2', '7', '12'],
          ['4', '5', '11', 'l1_2_1', 'l1_7_8', 'l1_12_9', 'l1_12_10'],
          ['3', '6', '9', '10', 'l2_2_1', 'l2_7_8', 'l2_4_8', 'l2_5_8'],
          ['1', '8']]

# Create a dictionary to store the coordinates of each node
nodes = {}

# Assign y-coordinates based on layers
for i, layer in enumerate(layers):
    for j, node in enumerate(layer):
        nodes[node] = (j, i)

# Edges between nodes with colors ('from', 'to', color)
edges = [('3', '1'),
         ('4', '3'),
         ('4', '9'),
         ('5', '3'),
         ('5', '10'),
         ('6', '1'),
         ('7', '4'),
         ('7', '5'),
         ('9', '8'),
         ('10', '8'),
         ('11', '6'),
         ('12', '11'),
         ('2', 'l1_2_1'),
         ('7', 'l1_7_8'),
         ('12', 'l1_12_9'),
         ('l1_12_9', '9'),
         ('12', 'l1_12_10'),
         ('l1_12_10', '10'),
         ('l2_2_1', '1'),
         ('l1_2_1', 'l2_2_1'),
         ('l2_7_8', '8'),
         ('l1_7_8', 'l2_7_8'),
         ('4', 'l2_4_8'),
         ('l2_4_8', '8'),
         ('5', 'l2_5_8'),
         ('l2_5_8', '8')]

fig, ax = plt.subplots()

for node, coord in nodes.items():
    # Check if the node is a dummy node
    color = 'grey' if node.startswith('l') else 'brown'
    ax.plot(*coord, marker='o', markersize=10, linestyle='', 
            label='', zorder=2, color=color)  # Set zorder for nodes
    # Add text only if it's not a dummy node
    if not node.startswith('l'):
        ax.text(*coord, node, ha='center', va='center', fontsize=8, color='black', fontweight='bold')


for edge in edges:
    start_coord = np.array(nodes[edge[0]])
    
    # Get the coordinates of the node center
    end_node_center = np.array(nodes[edge[1]])
    
    # Calculate the direction vector from start to end
    direction = end_node_center - start_coord
    
    # Normalize the direction vector
    direction_normalized = direction / np.linalg.norm(direction)
    
    # Define the end coordinate to be slightly before the node border
    end_coord = end_node_center - 0.15 * direction_normalized

    ax.arrow(*start_coord,
             *(end_coord - start_coord),
             head_width=0.04, 
             head_length=0.05,
             fc='blue',
             ec='blue',
             zorder=3)

# Set constant intervals on both axes
ax.set_xticks(np.arange(0, max(len(layer) for layer in layers), 1))
ax.set_yticks(np.arange(0, len(layers), 1))

ax.grid(True)
ax.set_axisbelow(True)
ax.set_xlabel('Position in Layer')
ax.set_ylabel('Layer')
plt.show()
