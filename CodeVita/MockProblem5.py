import numpy as np
import scipy.signal

def find_widest_valley(n, A, B):
    # Define the function based on the given arrays A and B
    def surface_function(x):
        y = np.zeros_like(x)
        for i in range(n):
            y += np.sin(x + A[i]) + np.sin(2 * x + B[i])
        return y

    # Generate x values from 0 to 2*pi
    x = np.linspace(0, 2 * np.pi, 1000)
    y = surface_function(x)

    # Find local maxima (peaks)
    peaks, _ = scipy.signal.find_peaks(y)

    # Calculate the width of each valley
    max_width = 0
    valley_index = -1
    for i in range(len(peaks) - 1):
        width = x[peaks[i + 1]] - x[peaks[i]]
        if width > max_width:
            max_width = width
            valley_index = i + 1

    return valley_index + 1  # Counting valleys from 1

if __name__ == '__main__':
    # Read input
    n = int(input().strip())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    # Find and print the widest valley
    result = find_widest_valley(n, A, B)
    print(result)