import os
import argparse
import cv2
from tqdm import tqdm
import imageio
from utils import edit_image_with_prompt

def create_gif_from_images(image_folder: str, output_path: str, duration_ms: int = 250):
    # Get all image files and sort them numerically
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpeg", ".jpg"))]
    images.sort(key=lambda x: int(os.path.splitext(x)[0]))
    
    if not images:
        print("No images found to create GIF.")
        return

    print(f"Found {len(images)} images to process:")
    for img in images:
        print(f"  - {img}")

    # Read first OpenAI-generated image (index 1) to get target dimensions
    if len(images) < 2:
        print("Error: Need at least one generated image to determine dimensions")
        return
        
    target_img_path = os.path.join(image_folder, images[1])  # Use first generated image
    target_img = cv2.imread(target_img_path)
    if target_img is None:
        print(f"Error: Could not read target image: {target_img_path}")
        return
    
    target_height, target_width = target_img.shape[:2]
    print(f"Resizing all images to: {target_width}x{target_height}")

    # Read all images and resize them
    frames = []
    for image in images:
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Error: Could not read image: {img_path}")
            continue
            
        # Resize image to match target dimensions
        img = cv2.resize(img, (target_width, target_height))
        
        # Convert BGR to RGB for GIF
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        frames.append(img)

    # Save as GIF
    imageio.mimsave(output_path, frames, duration=duration_ms/1000)  # Convert ms to seconds
    print(f"GIF saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Iteratively edit an image with OpenAI image model.")
    parser.add_argument("source", help="Path to the source image (e.g., inputs/source.jpg)")
    parser.add_argument("--prompt", default="Generate a copy of the attached image.", help="Prompt to apply")
    parser.add_argument("--runs", type=int, default=5, help="Number of iterations to apply")
    parser.add_argument("--out", default="outputs/videos/evolution.gif", help="Output GIF filename")
    args = parser.parse_args()

    os.makedirs("outputs/images", exist_ok=True)
    os.makedirs("outputs/videos", exist_ok=True)

    ext = os.path.splitext(args.source)[1]
    current_image = args.source
    initial_output = os.path.join("outputs/images", f"0{ext}")
    os.system(f"cp {current_image} {initial_output}")

    for i in tqdm(range(1, args.runs + 1), desc="Generating images"):
        input_path = os.path.join("outputs/images", f"{i-1}{ext}")
        output_path = os.path.join("outputs/images", f"{i}{ext}")
        edit_image_with_prompt(input_path, args.prompt, output_path)

    create_gif_from_images("outputs/images", args.out)
    print(f"\nGIF saved to: {args.out}")

if __name__ == "__main__":
    main()
