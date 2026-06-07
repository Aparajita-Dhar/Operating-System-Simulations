# Core Operating System Component Simulations in Python

This repository functions as an advanced academic portfolio mapping out the architectural workflows of modern operating system kernels. It tracks simulated low-level components including scheduling dispatchers, concurrent thread models, atomic semaphore bridges, deadlock detection matrices, and virtual segment addressing layouts.

##  System Core Modules Index

### Phase 1: Micro-Kernel Process & Synchronization Management
* **`01_preemptive_scheduling.py`**
  * Simulates a dynamic Shortest Remaining Time First (SRTF) preemptive CPU scheduler that tracks arrival/burst times and manages real-time context switching.
* **`02_thread_concurrency.py`**
  * Deploys asynchronous multi-threaded computing workers via native Python `threading` libraries to outline thread lifecycles and thread join operations.
* **`03_semaphore_lock.py`**
  * Resolves race conditions and critical section bottlenecks using atomic Counting Semaphores and Mutex locks within a classic Producer-Consumer pipeline.
    ### Phase 2: Structural Deadlocks & Virtual Memory Management
* **`04_deadlock_detection_single.py`**
  * Models single-instance hardware dependencies as Resource Allocation Graphs (RAG) and identifies cycle jams via recursive Depth-First Search (DFS).
* **`05_deadlock_detection_multiple.py`**
  * Evaluates multi-instance resource vectors against process requirement tables using matrix calculations to determine system dependency resolution states.
* **`06_memory_segmentation.py`**
  * Simulates kernel Memory Management Unit (MMU) routing behavior by validating logical segment offsets against base address translation tables.
