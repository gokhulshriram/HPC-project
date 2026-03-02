import matplotlib.pyplot as plt
import os

# List of files to read
files = ['72threads/cg_2000x20000.txt', '72threads/cg_20000x2000.txt',  '72threads/cg_1000x400000.txt']# #['72threads/pcg_2000x20000.txt', '72threads/pcg_20000x2000.txt', '72threads/pcg_1000x400000.txt'] ,    # Add more files if needed

# Loop over each file and plot the data
for file_name in files:
    num_threads = []
    performance = []

    # Read data from each file
    with open(file_name, 'r') as file:
        for line in file:
            # Split each line into two parts
            x, y = line.split()
            # Convert the values to float and append to the lists
            num_threads.append(float(x))
            performance.append(float(y))

    # Plot the data for the current file
    plt.plot(num_threads, performance, marker='o', label=f'{os.path.basename(file_name)}')

# Label the axes
plt.xlabel('Number of Threads')
plt.ylabel('Performance in [MLUP/s]')

# Set x-axis limits from 1 to 20
plt.xlim(1, 73)
plt.ylim(0, 3000)
# Set x-axis ticks using gca().set_xticks() for an increment of 1
plt.gca().set_xticks([i for i in range(0, 73, 5)])
plt.gca().set_yticks([i for i in range(0, 3000,300)])


# plt.axhline(y=488, color='r', linestyle='--', linewidth=1)

# plt.axhline(y=446, color='g', linestyle='--', linewidth=1)

# plt.annotate('Roofline PCG for 2000x20000 & 20000x2000', xy=(1, 488), xytext=(10, 0), textcoords='offset points', ha='left', va='center', color='r')

# plt.annotate('Roofline PCG for 1000x400000', xy=(1, 446), xytext=(10, 0), textcoords='offset points', ha='left', va='center', color='g')


# Add a title and a legend
plt.title('Performance CG - 72 threads')
plt.legend()

# Show the plot with grid
plt.grid(True)
plt.show()

