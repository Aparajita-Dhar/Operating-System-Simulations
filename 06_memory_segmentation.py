"""
Topic 6: Memory Segmentation Architecture Simulation
Models how an OS MMU (Memory Management Unit) uses a Segment Table 
to map a logical variable space into contiguous physical memory.
"""

class SegmentTableEntry:
    def __init__(self, base_address, limit_size):
        self.base_address = base_address  # Physical memory starting location
        self.limit_size = limit_size      # Allocated length segment boundaries

class MemoryManagementUnit:
    def __init__(self):
        # Segment Table Map: Segment ID -> Properties Entry
        self.segment_table = {}

    def configure_segment(self, segment_id, base, limit):
        self.segment_table[segment_id] = SegmentTableEntry(base, limit)

    def translate_address(self, logical_segment, offset):
        print(f"[MMU Input] Querying Virtual Target -> Segment {logical_segment}, Offset {offset}")
        
        if logical_segment not in self.segment_table:
            return "ERROR: Segmentation Fault. Requested Segment Index does not exist."
        
        entry = self.segment_table[logical_segment]

        # Security Check: Ensure the requested memory offset does not bleed past segment limits
        if offset >= entry.limit_size:
            return f"ERROR: Segmentation Fault! Offset {offset} violates allocation boundary limit ({entry.limit_size})."

        # Translation Equation: Physical Address = Base Address + Offset
        physical_address = entry.base_address + offset
        return f"SUCCESS: Translated to Physical Memory Location Address -> {physical_address}"

if __name__ == "__main__":
    print("--- Memory Management Unit: Segmentation Engine ---")
    mmu = MemoryManagementUnit()

    # Populating the segment table properties map (Segment ID, Base Address, Limit)
    mmu.configure_segment(segment_id=0, base=1400, limit=400)  # Segment 0 (Code Block)
    mmu.configure_segment(segment_id=1, base=6300, limit=200)  # Segment 1 (Global Variables)
    mmu.configure_segment(segment_id=2, base=4300, limit=300)  # Segment 2 (Runtime Stack)

    print("\n--- Execution Case 1: Valid Reference Access ---")
    # Requesting offset 150 inside Segment 0 (Within 400 byte bounds)
    result_1 = mmu.translate_address(logical_segment=0, offset=150)
    print(result_1)

    print("\n--- Execution Case 2: Out-Of-Bounds Fault Intercept ---")
    # Requesting offset 250 inside Segment 1 (Exceeds 200 byte limit!)
    result_2 = mmu.translate_address(logical_segment=1, offset=250)
    print(result_2)
