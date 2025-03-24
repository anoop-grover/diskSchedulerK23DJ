from src.algorithms import fcfs, sstf, scan, c_scan

def run_algorithm(requests, head, algorithm):
    if algorithm == "FCFS":
        return fcfs(requests, head)
    elif algorithm == "SSTF":
        return sstf(requests, head)
    elif algorithm == "SCAN":
        return scan(requests, head, max_cylinder=200)
    elif algorithm == "C-SCAN":
        return c_scan(requests, head, max_cylinder=200)
    else:
        return None, "Invalid Algorithm"
