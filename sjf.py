def sjf():
    n = int(input("Enter number of processes: "))
    
    processes = []
    burst_times = []
    
    for i in range(n):
        burst_time = int(input(f"Enter burst time for P{i+1}: "))
        processes.append(f"P{i+1}")
        burst_times.append(burst_time)

    sorted_processes = sorted(zip(processes, burst_times), key=lambda x: x[1])
    processes, burst_times = zip(*sorted_processes)

    waiting_times = [0] * n
    turnaround_times = [0] * n

    for i in range(1, n):
        waiting_times[i] = waiting_times[i - 1] + burst_times[i - 1]

    for i in range(n):
        turnaround_times[i] = waiting_times[i] + burst_times[i]

    print("\nProcess\tBurst Time\tWaiting Time\tTurn Around Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")

    avg_waiting_time = sum(waiting_times) / n
    avg_turnaround_time = sum(turnaround_times) / n
    print(f"\nAverage Waiting Time : {avg_waiting_time:.2f} msec")
    print(f"Average Turn Around Time : {avg_turnaround_time:.2f} msec")

sjf()
