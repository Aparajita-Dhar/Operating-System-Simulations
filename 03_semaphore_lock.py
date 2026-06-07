import threading
import time
import random

"""
Topic 3: Semaphore Mutex and Synchronization Contracts
Uses counting Semaphores to manage cross-thread boundary access inside a shared buffer space.
"""

class SharedBufferChannel:
    def __init__(self, storage_capacity):
        self.buffer = []
        # Semaphores tracking filled slots, empty slots, and a mutex for atomic operations
        self.empty_slots = threading.Semaphore(storage_capacity)
        self.filled_slots = threading.Semaphore(0)
        self.mutex = threading.Lock()

    def produce_item(self, hardware_id, data_packet):
        # Decrement empty slots (blocks if buffer is completely full)
        self.empty_slots.acquire()
        
        # Lock the critical section
        self.mutex.acquire()
        self.buffer.append(data_packet)
        print(f"[Producer-{hardware_id}] Appended packet: {data_packet} | Buffer Size: {len(self.buffer)}")
        self.mutex.release()
        
        # Increment filled slots signal to wake up consumers
        self.filled_slots.release()

    def consume_item(self, consumer_id):
        # Decrement filled slots (blocks if buffer is completely empty)
        self.filled_slots.acquire()
        
        # Lock the critical section
        self.mutex.acquire()
        extracted_data = self.buffer.pop(0)
        print(f"[Consumer-{consumer_id}] Consumed packet: {extracted_data} | Buffer Size: {len(self.buffer)}")
        self.mutex.release()
        
        # Increment empty slots signal to wake up producers
        self.empty_slots.release()

# Thread execution wrappers
def producer_routine(channel, worker_id):
    for _ in range(3):
        data_load = random.randint(1000, 9999)
        channel.produce_item(worker_id, data_load)
        time.sleep(random.uniform(0.1, 0.4))

def consumer_routine(channel, client_id):
    for _ in range(3):
        channel.consume_item(client_id)
        time.sleep(random.uniform(0.2, 0.5))

if __name__ == "__main__":
    print("--- Instantiating Semaphore Synchronized Pipelines ---\n")
    shared_memory_pipe = SharedBufferChannel(storage_capacity=3)

    # Instantiating concurrent threads
    p1 = threading.Thread(target=producer_routine, args=(shared_memory_pipe, "P-101"))
    c1 = threading.Thread(target=consumer_routine, args=(shared_memory_pipe, "C-501"))

    p1.start()
    c1.start()

    p1.join()
    c1.join()
    print("\nSynchronization simulation cleanly terminated.")
