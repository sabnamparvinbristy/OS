def mvt_python():
    memory_size = int(input("Enter the total memory available (in Bytes): "))
    total_allocated = 0
    process_details = []

    while True:
        process_size = int(input("\nEnter memory required for process (in Bytes): "))

        if process_size <= memory_size:
            memory_size -= process_size
            total_allocated += process_size
            process_details.append((len(process_details) + 1, process_size, "YES"))
            print(f"Memory is allocated for Process {len(process_details)}")
        else:
            process_details.append((len(process_details) + 1, process_size, "NO"))
            print(f"Memory is not available for Process {len(process_details)}")

        choice = input("Do you want to continue (y/n): ").lower()
        if choice != 'y':
            break

    print("\nOUTPUT")
    print("PROCESS\tMEMORY ALLOCATED\tALLOCATED")
    for process in process_details:
        print(f"{process[0]}\t{process[1]}\t\t{process[2]}")

    print(f"\nTotal Memory Allocated is {total_allocated} Bytes.")
    print(f"Total External Fragmentation is {memory_size} Bytes.")

if __name__ == "__main__":
    mvt_python()
