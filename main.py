import matplotlib.pyplot as plt

from FIFO import *
from LRU import *
from Optimal import *

ref_string = [3, 1, 1, 6, 1, 5, 6, 4, 7, 2, 3, 4, 5, 5, 3, 6, 5, 5, 0, 6, 6, 7, 7, 1, 4, 2, 5, 7, 5, 4]
number_of_frames = 3


def fixExperiment(ref_string, number_of_frames):
    pageFaultsFIFO(ref_string, number_of_frames)
    pageFaultsOptimal(ref_string, number_of_frames)
    pageFaultsLRU(ref_string, number_of_frames)


def changeNumberOfFrames(ref_string_x, max_of_frames, show_graph=False):
    number_of_frames_x_axis = [i for i in range(1, max_of_frames + 1)]
    page_faults_fifo_y_axis = []
    page_faults_optimal_y_axis = []
    page_faults_lru_y_axis = []

    for _, i in enumerate(number_of_frames_x_axis):
        page_faults_fifo_y_axis.append(pageFaultsFIFO(ref_string_x, i))
        page_faults_optimal_y_axis.append(pageFaultsOptimal(ref_string_x, i))
        page_faults_lru_y_axis.append(pageFaultsLRU(ref_string_x, i))

    if show_graph:
        plt.plot(number_of_frames_x_axis, page_faults_fifo_y_axis, label='FIFO')
        plt.plot(number_of_frames_x_axis, page_faults_optimal_y_axis, label='Optimal')
        plt.plot(number_of_frames_x_axis, page_faults_lru_y_axis, label='LRU')
        plt.xlabel('Number of Frames')
        plt.ylabel('Page Faults')
        plt.title('Number of Frames vs Page Faults')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    # fixExperiment(ref_string, number_of_frames)
    changeNumberOfFrames(ref_string, 15, show_graph=True)
