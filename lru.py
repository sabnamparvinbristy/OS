def lru_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0
    recently_used = {}

    for i, page in enumerate(pages):
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
    
                lru_page = min((p for p in frame), key=lambda x: recently_used[x])
                frame.remove(lru_page)
                frame.append(page)
            page_faults += 1
        recently_used[page] = i

    return page_faults

def main():
    
    pages = list(map(int, input("Enter the reference pages: ").split()))
 
    frame_size = int(input("Enter the frame size: "))
  
    lru_faults = lru_page_replacement(pages, frame_size)
    
    print("\nResults:")
    print(f"LRU Page Faults: {lru_faults}")

if __name__ == "__main__":
    main()
