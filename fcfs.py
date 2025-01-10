def fcfs():
    n = int(input("Enter number of processes: "))
    burst_times = []
    
    for i in range(n):
        burst_time = int(input(f"Enter burst time for P{i+1}: "))
        burst_times.append(burst_time)

    print("\nProcess\t Burst Time\t Waiting Time\t Turn Around Time\n")
    waiting_time = 0
    total_tat = 0
    total_wt = 0

    for i in range(n):
        turn_around_time = burst_times[i] + waiting_time
        print(f"P{i+1} \t  {burst_times[i]} \t\t   {waiting_time} \t\t   {turn_around_time}")
        total_tat += turn_around_time
        total_wt += waiting_time
        waiting_time += burst_times[i]

    print(f"\nAverage Waiting Time : {total_wt / n:.2f} msec")
    print(f"Average Turn Around Time : {total_tat / n:.2f} msec")
fcfs()
