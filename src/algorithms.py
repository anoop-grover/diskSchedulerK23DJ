def fcfs(requests, head):
    """ First-Come-First-Serve Disk Scheduling """
    seek_sequence = [head] + requests
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

def sstf(requests, head):
    """ Shortest Seek Time First Disk Scheduling """
    seek_sequence = [head]
    remaining = requests.copy()
    
    while remaining:
        closest = min(remaining, key=lambda x: abs(x - seek_sequence[-1]))
        seek_sequence.append(closest)
        remaining.remove(closest)
    
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

def scan(requests, head, max_cylinder):
    """ SCAN Disk Scheduling (Elevator Algorithm) """
    requests.append(head)
    requests.sort()
    direction = 1  # Move towards higher values
    seek_sequence = []

    if head in requests:
        idx = requests.index(head)

    if direction == 1:  # Moving right
        seek_sequence.extend(requests[idx:])
        seek_sequence.append(max_cylinder)  # Go to max limit
        seek_sequence.extend(reversed(requests[:idx]))  # Then go back

    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time

def c_scan(requests, head, max_cylinder):
    """ C-SCAN Disk Scheduling """
    requests.append(head)
    requests.sort()
    seek_sequence = []

    idx = requests.index(head)
    seek_sequence.extend(requests[idx:])  # Move towards max cylinder
    seek_sequence.append(max_cylinder)  # Go to max limit
    seek_sequence.append(0)  # Jump to min
    seek_sequence.extend(requests[:idx])  # Serve remaining requests

    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, seek_time
