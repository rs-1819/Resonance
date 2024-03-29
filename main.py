import numpy as np
from PIL import Image
import os
import wave
from tqdm import tqdm

WIDTH, HEIGHT = 768, 768
PIXELS = WIDTH * HEIGHT
RGB = 3
IMAGE_FOLDER = "images"
PIXEL_EXPANSION = 1  # How much to expand each pixel

def wav_to_images(filename):
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)

    with wave.open(filename, 'rb') as f:
        nframes = f.getnframes()
        frames = f.readframes(nframes)
    
    total_images = len(frames) // ((PIXELS * RGB) // (PIXEL_EXPANSION * PIXEL_EXPANSION)) + \
                   (1 if len(frames) % ((PIXELS * RGB) // (PIXEL_EXPANSION * PIXEL_EXPANSION)) != 0 else 0)

    images = []
    pbar = tqdm(total=total_images, desc="Converting audio to images", unit="image")
    for img_num in range(total_images):
        image = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        for i in range(HEIGHT // PIXEL_EXPANSION):
            for j in range(WIDTH // PIXEL_EXPANSION):
                idx = img_num * (PIXELS * RGB) // (PIXEL_EXPANSION * PIXEL_EXPANSION) + i * (WIDTH // PIXEL_EXPANSION) * RGB + j * RGB
                if idx < len(frames):
                    val = [frames[idx], frames[idx+1], frames[idx+2] if idx + 2 < len(frames) else 0]
                else:
                    val = [0, 0, 0]
                for x in range(PIXEL_EXPANSION):
                    for y in range(PIXEL_EXPANSION):
                        image[i * PIXEL_EXPANSION + x][j * PIXEL_EXPANSION + y] = val
        images.append(Image.fromarray(image, 'RGB'))
        pbar.update(1)
    pbar.close()
    return images

def images_to_wav(images, output_filename):
    frames = bytearray()
    pbar = tqdm(total=len(images), desc="Converting images to audio", unit="image")
    for image in images:
        np_array = np.array(image)
        for i in range(HEIGHT // PIXEL_EXPANSION):
            for j in range(WIDTH // PIXEL_EXPANSION):
                frames.extend(np_array[i * PIXEL_EXPANSION][j * PIXEL_EXPANSION])
        pbar.update(1)
    pbar.close()

    while frames[-3:] == bytearray([0, 0, 0]):
        del frames[-3:]

    with wave.open(output_filename, 'wb') as f:
        # Set audio file parameters
        f.setnchannels(2)  # stereo
        f.setsampwidth(2)  # 2 bytes per sample
        f.setframerate(48000)  # 48000 Hz sample rate
        f.writeframes(frames)

def test(filename):
    # Convert WAV to images
    images = wav_to_images(filename)
    
    # Save images
    for i, image in enumerate(images):
        image.save(os.path.join(IMAGE_FOLDER, f'lorned_{i}.png'))

    # Load images from the specified folder
    image_files = sorted([f for f in os.listdir(IMAGE_FOLDER) if f.endswith('.png')], key=lambda f: int(f.split('_')[1].split('.')[0]))
    loaded_images = [Image.open(os.path.join(IMAGE_FOLDER, f)) for f in image_files]

    # Convert images to WAV
    images_to_wav(loaded_images, 'output.wav')
    
    print("Test completed. Check the output file and the images.")

# Testing the functions
test('test.wav')