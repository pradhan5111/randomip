from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def skewness(data):
    n = len(data)
    mean = np.mean(data)
    std_dev = np.std(data)
    skew = np.sum(((data - mean) / std_dev) ** 3) / n
    return skew

def kurtosis(data):
    n = len(data)
    mean = np.mean(data)
    std_dev = np.std(data)
    kurt = np.sum(((data - mean) / std_dev) ** 4) / n - 3  # Excess kurtosis
    return kurt

def binary_image_statistics(image_path):
    # Load and convert image to grayscale
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)

    # Apply simple thresholding (e.g., Otsu's can be added if needed manually)
    threshold = 128
    binary_image = (image_array > threshold) * 255
    binary_image = binary_image.astype(np.uint8)

    # Flatten image to 1D array
    pixel_values = binary_image.ravel()

    # Compute statistics
    stats_values = {
        'Mean': np.mean(pixel_values),
        'Median': np.median(pixel_values),
        'Standard Deviation': np.std(pixel_values),
        'Skewness': skewness(pixel_values),
        'Kurtosis': kurtosis(pixel_values)
    }

    # Display the binary image
    plt.imshow(binary_image, cmap='gray')
    plt.axis('off')
    plt.title('Binary Image')
    plt.show()

    # Print statistics
    print("Statistics values for binary image:")
    for stat, value in stats_values.items():
        print(f"{stat}: {value:.2f}")

    return stats_values

# Example usage
image_path = r"C:/Users/gaura/Downloads/flower.png"  # Replace with your image path
stats_values = binary_image_statistics(image_path)
