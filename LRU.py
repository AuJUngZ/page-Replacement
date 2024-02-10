def pageFaultsLRU(ref_string, number_of_frames):
    list_of_pages = []
    page_faults = 0

    for index, page in enumerate(ref_string):
        if len(list_of_pages) < number_of_frames:
            if page not in list_of_pages:
                list_of_pages.append(page)
                page_faults += 1
        else:
            if page not in list_of_pages:
                distance = {}
                for i in list_of_pages:
                    distance[i] = ref_string[:index][::-1].index(i)
                list_of_pages[list_of_pages.index(max(distance, key=distance.get))] = page
                page_faults += 1

    print("Experiment : LRU algorithm")
    print("number_of_frames : ", number_of_frames)
    print("Page Faults LRU algorithm: ", page_faults)

    return page_faults
