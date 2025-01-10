def fifo_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0

    for page in pages:
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1

    return page_faults

def main():
    pages = list(map(int, input("Enter the reference pages: ").split()))

    frame_size = int(input("Enter the frame size: "))

    fifo_faults = fifo_page_replacement(pages, frame_size)

    print("\nResults:")
    print(f"FIFO Page Faults: {fifo_faults}")


if __name__ == "__main__":
    main()
# 7  0 1 2 0 3 0 4 2 3 0 3 0 3 2 1 2 01 7 0 1