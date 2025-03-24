import matplotlib.pyplot as plt

def plot_disk_movement(seek_sequence):
    plt.figure(figsize=(8, 5))
    plt.plot(seek_sequence, range(len(seek_sequence)), marker="o", linestyle="-", color="blue")
    plt.xlabel("Cylinder Number")
    plt.ylabel("Sequence Step")
    plt.title("Disk Head Movement")
    plt.show()
