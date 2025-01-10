class Process:
    def __init__(self, no, burst_time):
        self.no = no
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def calculate_waiting_time(processes, quantum):
    remaining_burst_time = [p.burst_time for p in processes]
    time = 0

    while True:
        all_done = True
        for i in range(len(processes)):
            if remaining_burst_time[i] > 0:
                all_done = False

                if remaining_burst_time[i] > quantum:
                    time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    time += remaining_burst_time[i]
                    processes[i].waiting_time = time - processes[i].burst_time
                    remaining_burst_time[i] = 0

        if all_done:
            break

def calculate_turnaround_time(processes):
    for p in processes:
        p.turnaround_time = p.burst_time + p.waiting_time

def round_robin(processes, quantum):
    calculate_waiting_time(processes, quantum)
    calculate_turnaround_time(processes)

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    total_waiting_time = 0
    total_turnaround_time = 0

    for p in processes:
        total_waiting_time += p.waiting_time
        total_turnaround_time += p.turnaround_time
        print(f"{p.no}\t{p.burst_time}\t\t{p.waiting_time}\t\t{p.turnaround_time}")

    print(f"\nAverage Waiting Time: {total_waiting_time / len(processes):.2f}")
    print(f"Average Turnaround Time: {total_turnaround_time / len(processes):.2f}")

def main():
    n = int(input("Enter number of processes: "))
    burst_times = [int(input(f"Enter burst time for process {i + 1}: ")) for i in range(n)]
    quantum = int(input("Enter time quantum: "))

    processes = [Process(i + 1, burst_times[i]) for i in range(n)]
    round_robin(processes, quantum)

if __name__ == "__main__":
    main()
