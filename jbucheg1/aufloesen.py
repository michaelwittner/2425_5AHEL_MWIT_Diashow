from PIL import Image
import numpy as np
import random
import os


from PIL import Image
import numpy as np
import random
import os


def pixelize(picture1, picture2, time, fps, output_dir):
    """
        Pixilize two images together one block at a time.
        Images have to be time same size.

        Parameters:
        - picture1: The first image (PIL Image) to blend.
        - picture2: The second image (PIL Image) to blend into.
        - time: Duration of the blending in seconds.
        - fps: Frames per second for the output.
        - output_dir: Directory where to save the blended images.
        """

    # Convert both images to RGBA
    image1 = picture1.convert("RGBA")
    image2 = picture2.convert("RGBA")

    # Convert images to numpy arrays
    image1_array = np.array(image1)
    image2_array = np.array(image2)

    # Get image dimensions
    height, width, _ = image1_array.shape

    # Number of total frames
    num_images = int(time * fps)

    # Define number of blocks per side based on total frames
    num_blocks_per_side = int(np.sqrt(num_images) * 2)
    block_size = min(width, height) // num_blocks_per_side

    # Generate a shuffled list of block positions
    blocks = [(x, y) for x in range(0, width, block_size) for y in range(0, height, block_size)]
    random.shuffle(blocks)

    # Ensure we have enough blocks for blending
    total_blocks = len(blocks)
    blocks_per_frame_progression = np.linspace(1, total_blocks, num_images, dtype=int)


    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize the blended image (start fully with image1)
    blended_image = np.copy(image1_array)

    # List to save frame path and show duration
    frame_list = []

    # Blending images block by block for `num_images` frames
    for step_idx in range(num_images):
        blended_image_step = np.copy(blended_image)

        # Determine how many blocks to blend in this frame
        current_blocks_count = blocks_per_frame_progression[step_idx]

        # Blend blocks up to this count
        for i in range(current_blocks_count):
            if i >= total_blocks:
                break
            x, y = blocks[i]

            # Copy the block from image2
            blended_image_step[y:y + block_size, x:x + block_size] = image2_array[y:y + block_size, x:x + block_size]

        # Save the current blended image
        output_path = os.path.join(output_dir, f'output_{step_idx:04d}.png')
        Image.fromarray(blended_image_step).save(output_path)

        # Update blended image for the next iteration
        blended_image = np.copy(blended_image_step)
        frame_list.append(f"{output_path}, {1}/{fps}")
    return frame_list


# Example usage
list = pixelize(Image.open('foto.jpg'), Image.open('foto2.jpg'), 6, 10, 'output_images')

print(list)