import numpy as np
import pandas as pd

file_path = 'data/example_data.xlsx'
data = pd.read_excel(file_path, header=None)

data_as_numpy = data.to_numpy()

gaussian_filter = np.array([[1, 2, 1],
                            [2, 4, 2],
                            [1, 2, 1]]) / 16

filtered_data = np.zeros((data_as_numpy.shape[0] - 2, data_as_numpy.shape[1] - 2))

filter_size = gaussian_filter.shape[0]
offset = filter_size // 2

for i in range(offset, data_as_numpy.shape[0] - offset):
    for j in range(offset, data_as_numpy.shape[1] - offset):
        region = data_as_numpy[i - offset:i + offset + 1, j - offset:j + offset + 1]
        filtered_value = np.sum(region * gaussian_filter)
        filtered_data[i - offset, j - offset] = filtered_value

print("Smoothed data matrix:")
print(filtered_data)

smoothed_data_df = pd.DataFrame(filtered_data)

output_file_path = 'data/smoothed_image.xlsx'
smoothed_data_df.to_excel(output_file_path, header=False, index=False)

print("------------------------------------")
print("Original data size:", data_as_numpy.shape)
print("Smoothed data size:", filtered_data.shape)
print("The smoothed data was saved successfully:", output_file_path)