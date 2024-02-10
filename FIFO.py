def pageFaultsFIFO(ref_string, number_of_frames):
    """
    :param ref_string: list of page_number
    :param number_of_frames: number of frames that os provides
    :return: none
    """
    dic_of_frames = {}
    page_faults = 0

    for index, page in enumerate(ref_string):
        if len(dic_of_frames) < number_of_frames:
            if page not in dic_of_frames:
                dic_of_frames[page] = index
                page_faults += 1
        else:
            if page not in dic_of_frames:
                min_value = min(dic_of_frames.values())
                dic_of_frames = {key: value for key, value in dic_of_frames.items() if value != min_value}
                dic_of_frames[page] = index
                page_faults += 1

    print("Experiment : FIFO")
    print("number_of_frames : ", number_of_frames)
    print("Page Faults FIFO : ", page_faults)
    print("\n")

    return page_faults
