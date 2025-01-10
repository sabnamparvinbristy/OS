def get_user_input():
    processes = int(input("Enter the number of processes: "))
    resources = int(input("Enter the number of resource: "))

    print("Enter the maximum value as matrix:")
    max_matrix = []
    for _ in range(processes):
        max_matrix.extend(list(map(int, input().split())))

    print("Enter the allocation as matrix:")
    alloc_matrix = []
    for _ in range(processes):
        alloc_matrix.extend(list(map(int, input().split())))

    avail = list(map(int, input("Enter the available resources: ").split()))

    return processes, resources, max_matrix, alloc_matrix, avail

def calculate_needs(processes, resources, max_matrix, alloc_matrix):
    needs = []
    for i in range(processes * resources):
        needs.append(max_matrix[i] - alloc_matrix[i])
    return needs

def print_info(processes, resources, max_matrix, alloc_matrix, needs, avail):
    print(f"\nProcess\tMaximum\t\tAllocation\t\tCurrent Needs")
    for i in range(processes):
        max_slice = max_matrix[i * resources:(i + 1) * resources]
        alloc_slice = alloc_matrix[i * resources:(i + 1) * resources]
        needs_slice = needs[i * resources:(i + 1) * resources]

        print(f"P{i}\t{max_slice}\t{alloc_slice}\t{needs_slice}")

    print("\nAvailable: ", avail)

def is_safe_state(processes, resources, alloc_matrix, needs, avail):
    finish = [False] * processes
    sequence = []

    for _ in range(processes):
        allocated = False
        for i in range(processes):
            if not finish[i]:
                if all(needs[i * resources + j] <= avail[j] for j in range(resources)):
                    for j in range(resources):
                        avail[j] += alloc_matrix[i * resources + j]

                    finish[i] = True
                    sequence.append(f"P{i}")
                    allocated = True

        if not allocated:
            break

    if all(finish):
        print("\nSystem is safe!")
        print("Safe sequence: ", ", ".join(sequence))
    else:
        print("\nSystem is not safe!")

def main():
    processes, resources, max_matrix, alloc_matrix, avail = get_user_input()
    needs = calculate_needs(processes, resources, max_matrix, alloc_matrix)

    print_info(processes, resources, max_matrix, alloc_matrix, needs, avail)
    is_safe_state(processes, resources, alloc_matrix, needs, avail)

if __name__ == "__main__":
    main()
