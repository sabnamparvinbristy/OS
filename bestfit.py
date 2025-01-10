def main():
    bno = int(input("Enter the number of blocks: "))
    bsize = []
    print("Enter the size of the blocks:")
    for i in range(bno):
        size = int(input(f"Block {i + 1}: "))
        bsize.append(size)

    pno = int(input("\nEnter the number of files: "))
    psize = []
    print("Enter the size of the files:")
    for i in range(pno):
        size = int(input(f"File {i + 1}: "))
        psize.append(size)

    allocation = [-1] * pno
    fragments = [0] * pno

    for i in range(pno):
        best_index = -1
        for j in range(bno):
            if bsize[j] >= psize[i]:
                if best_index == -1 or bsize[j] < bsize[best_index]:
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index + 1
            fragments[i] = bsize[best_index] - psize[i]
            bsize[best_index] = 0

    print("\nFile No.\tFile Size\tBlock No.\tBlock Size\tFragment")
    for i in range(pno):
        file_no = i + 1
        file_size = psize[i]
        if allocation[i] != -1:
            block_no = allocation[i]
            block_size = file_size + fragments[i]
            fragment = fragments[i]
            print(f"{file_no}\t\t{file_size}\t\t{block_no}\t\t{block_size}\t\t{fragment}")
        else:
            print(f"{file_no}\t\t{file_size}\t\tNot Allocated\t\t-\t\t-")

if __name__ == "__main__":
    main()
