class Process:
    def __init__(self, no, burst_time=0, priority=0):
        self.no = no
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def read_process(i):
    print(f"\nProcess No: {i}")
    burst_time = int(input("Enter Burst Time: "))
    priority = int(input("Enter Priority: "))
    return Process(no=i, burst_time=burst_time, priority=priority)

def smaller_priority_first(processes):
    processes.sort(key=lambda x: x.priority)

    print("\nProcess\tBT\tPri\tCT\tTAT\tWT")
    current_time = 0
    total_tat = 0
    total_wt = 0

    for process in processes:
        current_time += process.burst_time
        process.completion_time = current_time
        process.turnaround_time = process.completion_time
        process.waiting_time = process.turnaround_time - process.burst_time

        total_tat += process.turnaround_time
        total_wt += process.waiting_time

        print(f"P{process.no}\t{process.burst_time}\t{process.priority}\t"
              f"{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

    avg_tat = total_tat / len(processes)
    avg_wt = total_wt / len(processes)
    print(f"\nAverage Turnaround Time = {avg_tat:.2f}")
    print(f"Average Waiting Time = {avg_wt:.2f}")

def main():
    n = int(input("Enter total number of processes: "))
    processes = []

    for i in range(1, n + 1):
        processes.append(read_process(i))

    smaller_priority_first(processes)

if __name__ == "__main__":
    main()
