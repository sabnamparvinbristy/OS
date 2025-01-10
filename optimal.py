def optimal_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                farthest = -1
                index_to_replace = -1
                for j, f in enumerate(frame):
                    if f not in pages[i + 1:]:  
                        index_to_replace = j
                        break
                    else:
                        next_index = pages[i + 1:].index(f) + i + 1
                        if next_index > farthest:
                            farthest = next_index
                            index_to_replace = j

                frame[index_to_replace] = page
            page_faults += 1
    return page_faults

def main():
    try:
        pages = list(map(int, input("Enter the reference pages: ").split()))
        if not pages:
            print("Error: No pages entered.")
            return
        frame_size = int(input("Enter the frame size: "))
        if frame_size <= 0:
            print("Error: Frame size must be greater than 0.")
            return

        optimal_faults = optimal_page_replacement(pages, frame_size)

        print("\nResults:")
        print(f"Optimal Page Faults: {optimal_faults}")

    except ValueError:
        print("Error: Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()
