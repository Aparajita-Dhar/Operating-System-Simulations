"""
Topic 1: Preemptive CPU Scheduling (Shortest Remaining Time First - SRTF)
Simulates how an OS kernel context-switches processes based on remaining burst execution cycles.
"""

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

class SRTFSimulator:
    @staticmethod
    def run_simulation(processes):
        current_time = 0
        completed = 0
        n = len(processes)
        last_selected = None
        execution_order = []

        print("--- CPU Execution Timeline (Gantt Pattern) ---")
        
        while completed < n:
            # Filter processes that have arrived and are not yet finished
            available = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]
            
            if not available:
                current_time += 1
                continue

            # Selection rule: Choose process with the minimum remaining burst time
            current_process = min(available, key=lambda p: p.remaining_time)
            
            if last_selected != current_process.pid:
                execution_order.append(f"[Time {current_time}: P{current_process.pid}]")
                last_selected = current_process.pid

            # Preemptive step: Execute the selected process for 1 time unit
            current_process.remaining_time -= 1
            current_time += 1

            # Check if process has finished executing
            if current_process.remaining_time == 0:
                completed += 1
                current_process.completion_time = current_time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time

        print(" -> ".join(execution_order) + f" -> [Time {current_time}: Terminated]")
        
        # Display performance matrices
        print("\n--- SRTF Performance Metrics Table ---")
        print("PID\tArrival\tBurst\tDrop/End\tTurnaround\tWaiting")
        for p in processes:
            print(f"P{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t\t{p.turnaround_time}\t\t{p.waiting_time}")

if __name__ == "__main__":
    # Defining core process metrics (PID, Arrival Time, Burst Time)
    job_pool = [
        Process(1, 0, 8),
        Process(2, 1, 4),
        Process(3, 2, 9),
        Process(4, 3, 5)
    ]
    SRTFSimulator.run_simulation(job_pool)
