"""
Topic 5: Deadlock Detection for Multiple-Instance Resource Types
Implements the resource allocation matrix safety tracking routine to evaluate 
if unallocated system margins can safely fulfill outstanding requests.
"""

import numpy as np

class MultiResourceDeadlockDetector:
    def __init__(self, num_processes, num_resources, available, allocation, request):
        self.np = num_processes
        self.nr = num_resources
        self.available = np.array(available)       # Vector of unassigned resource instances
        self.allocation = np.array(allocation)     # Matrix of currently held resource links
        self.request = np.array(request)           # Matrix of outstanding resource demands

    def scan_for_deadlock(self):
        work = np.copy(self.available)
        finish = np.array([False] * self.np)

        # Optimization: Processes with zero allocation can be instantly flagged as True
        for i in range(self.np):
            if np.all(self.allocation[i] == 0):
                finish[i] = True

        while True:
            found_executable_process = False
            
            for i in range(self.np):
                # Look for an incomplete process whose request vector can be satisfied by current Work margins
                if not finish[i] and np.all(self.request[i] <= work):
                    # Simulate process execution, release its allocated resources back to Work vector
                    work += self.allocation[i]
                    finish[i] = True
                    found_executable_process = True
                    break  # Break out to restart the check loop with updated Work margins
            
            if not found_executable_process:
                break

        # If any process remains unfinished, a deadlock condition exists
        deadlocked_processes = [i for i, state in enumerate(finish) if not state]
        return deadlocked_processes

if __name__ == "__main__":
    print("--- Deadlock Detection: Multiple-Instance Resource Matrix ---")
    
    # 3 Processes (P0, P1, P2), 3 Resource Types (A, B, C)
    available_vector = [0, 0, 0]
    
    allocation_matrix = [
        [0, 1, 0],  # P0 holds 1 instance of B
        [2, 0, 0],  # P1 holds 2 instances of A
        [3, 0, 3]   # P2 holds 3 of A, 3 of C
    ]
    
    request_matrix = [
        [0, 0, 0],  # P0 needs no extra resources
        [2, 0, 2],  # P1 requests 2 of A, 2 of C (Exceeds available vector!)
        [0, 0, 1]   # P2 requests 1 instance of C
    ]

    detector = MultiResourceDeadlockDetector(3, 3, available_vector, allocation_matrix, request_matrix)
    deadlocked = detector.scan_for_deadlock()

    print("\nExecuting multi-instance matrix evaluation algorithm...")
    if deadlocked:
        print(f"CRITICAL FAULT: Deadlock identified! Impacted Processes: {['P'+str(pid) for pid in deadlocked]}")
    else:
        print("System Status: SAFE. All allocation dependencies can resolve naturally.")
