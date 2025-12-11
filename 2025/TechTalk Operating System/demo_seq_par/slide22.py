"""
CPU-Bound Task Example: Batch Image Processing with Pillow
Problem: Resize and apply filters to hundreds of product images for an e-commerce site
"""

from PIL import Image, ImageFilter, ImageEnhance
import os
import time
from multiprocessing import Pool, cpu_count

def process_single_image(args):
    """Process a single image: resize, enhance, and apply filters"""
    input_path, output_dir = args
    filename = os.path.basename(input_path)
    
    try:
        # Open image
        img = Image.open(input_path)
        
        # Resize to thumbnail (CPU-intensive operation)
        img.thumbnail((400, 600), Image.LANCZOS)
        
        # Enhance sharpness (CPU-intensive)
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.5)
        
        # Apply unsharp mask filter (very CPU-intensive)
        img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150))
        
        # Save processed image
        output_path = os.path.join(output_dir, f"processed_{filename}")
        img.save(output_path, quality=95, optimize=True)
        
        return f"Processed: {filename}"
    except Exception as e:
        return f"Error processing {filename}: {str(e)}"

def process_images_sequential(image_paths, output_dir):
    """Process images one by one (slow for CPU-bound tasks)"""
    print("Processing images sequentially...")
    start = time.time()
    
    results = []
    for path in image_paths:
        result = process_single_image((path, output_dir))
        results.append(result)
    
    elapsed = time.time() - start
    print(f"Sequential processing took: {elapsed:.2f} seconds")
    return results

def process_images_parallel(image_paths, output_dir):
    """Process images in parallel using multiprocessing"""
    print(f"Processing images in parallel with {cpu_count()} cores...")
    start = time.time()
    
    # Create arguments for each image
    args = [(path, output_dir) for path in image_paths]
    
    # Use multiprocessing pool to distribute work across CPU cores
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_single_image, args)
    
    elapsed = time.time() - start
    print(f"Parallel processing took: {elapsed:.2f} seconds")
    return results

# Example usage
if __name__ == "__main__":
    # Simulate batch processing of product images
    folder="input_images"
    input_images = [f"{folder}/{i}.jpg" for i in range(1, 4) ]  # Add your images
    print(input_images)
    output_directory = "process_images_sequential"
    
    os.makedirs(output_directory, exist_ok=True)
    
    # Compare sequential vs parallel processing
    # Uncomment to test with real images:
    process_images_sequential(input_images, output_directory)
    #process_images_parallel(input_images, output_directory)
    
    print(f"\nYour system has {cpu_count()} CPU cores available")
    print("For CPU-bound tasks, parallel processing can provide near-linear speedup!")