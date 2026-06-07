import threading
import time

"""
Topic 2: Thread Creation and Concurrency Management
Demonstrates the initialization, asynchronous execution, and lifecycle join routines of OS worker threads.
"""

class KernelWorkerThread(threading.Thread):
    def __init__(self, task_id, load_weight):
        super().__init__()
        self.task_id = task_id
        self.load_weight = load_weight

    # The entry point of execution for the thread
    def run(self):
        print(f"[Thread Alpha-{self.task_id}] Spawned. State: RUNNING.")
        
        for step in range(1, 4):
            print(f"[Thread Alpha-{self.task_id}] Executing sub-compute stack cycle #{step}...")
            time.sleep(self.load_weight)  # Simulates operational I/O wait states
            
        print(f">> [Thread Alpha-{self.task_id}] Finalized work cycles. State: ZOMBIE/TERMINATED.")

if __name__ == "__main__":
    print("--- Booting Multi-Threaded Concurrent Operations ---")

    # Instantiating two distinct thread objects
    worker_1 = KernelWorkerThread(task_id=101, load_weight=0.3)
    worker_2 = KernelWorkerThread(task_id=102, load_weight=0.5)

    # Launching threads concurrently in the background
    worker_1.start()
    worker_2.start()

    print("[Main Thread] Moving forward with background engine verification loops...")

    # Wait barriers: Synchronizes execution by pausing main until worker threads finish
    worker_1.join()
    worker_2.join()

    print("\nAll background concurrent worker tracks have safely rejoined the master core thread.")
