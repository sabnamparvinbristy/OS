def mft_python():
    memory_size = int(input("Enter the total memory available (in Bytes): "))
    block_size = int(input("Enter the block size (in Bytes): "))
    num_processes = int(input("Enter the number of processes: "))

    num_blocks = memory_size // block_size
    external_fragmentation = memory_size % block_size
    blocks = [False] * num_blocks  # Tracks if a block is free or allocated
    process_details = []
    total_internal_fragmentation = 0

    for process_id in range(1, num_processes + 1):
        process_size = int(input(f"Enter memory required for process {process_id} (in Bytes): "))
        allocated = False

        # Try to allocate the process to a free block
        for i in range(num_blocks):
            if not blocks[i]:  # Check if the block is free
                if process_size <= block_size:
                    blocks[i] = True
                    internal_fragmentation = block_size - process_size
                    total_internal_fragmentation += internal_fragmentation
                    process_details.append((process_id, process_size, "YES", internal_fragmentation))
                    allocated = True
                    break

        # If not allocated
        if not allocated:
            process_details.append((process_id, process_size, "NO", "N/A"))

    print("\nOUTPUT")
    print("PROCESS\tMEMORY REQUIRED\tALLOCATED\tINTERNAL FRAGMENTATION")
    for process in process_details:
        print(f"{process[0]}\t{process[1]}\t\t{process[2]}\t\t{process[3]}")

    free_blocks = blocks.count(False)
    print(f"\nMemory is Full, Remaining Processes cannot be accommodated.")
    print(f"Total Internal Fragmentation is {total_internal_fragmentation} Bytes.")
    print(f"Total External Fragmentation is {external_fragmentation} Bytes.")

if __name__ == "__main__":
    mft_python()
