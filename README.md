# Resonance: Audio-Image Interconversion for AI Diffusion Models

Welcome to Resonance, a Python-based tool that enables the conversion of audio files into images and vice versa. This project aims to bridge the gap between audio and visual domains, facilitating the use of AI diffusion models for audio generation from images.

![AUDIO]((https://i.imgur.com/Jb8xa2z.png)

## Features

- Convert WAV audio files into a sequence of RGB images
- Convert a sequence of RGB images back into a WAV audio file
- Customize image dimensions and pixel expansion factor
- Retain the stereo field of audio by writing byte data to RGB channels
- Compatible with AI diffusion models for audio generation from images
- Train AI models using the generated images and play the output audio

## Advantages over Spectrograms

Unlike using spectrograms for audio representation, Project Resonance preserves the stereo field of the audio by writing the byte data directly to the RGB channels of the images. This approach allows for more accurate audio reconstruction and provides a better representation of the spatial information in the audio.

## Pixel Expansion and Fidelity

The pixel expansion factor in Project Resonance allows you to control the size of the generated images. While increasing the pixel expansion factor reduces the fidelity of the audio representation, it can make the audio training process more accurate. By expanding each pixel, the model can capture more granular details of the audio, leading to better generation results.

## Requirements

- Python 3.x
- NumPy
- Pillow (PIL)
- tqdm

## Installation

```
TODO
```

## Usage

1. Place your input WAV file in the project directory.

2. Open `main.py` and modify the following parameters if needed:
   - `WIDTH`: The width of the generated images (default: 768)
   - `HEIGHT`: The height of the generated images (default: 768)
   - `PIXEL_EXPANSION`: The factor by which each pixel is expanded (default: 1)

3. Run the script:

```
python main.py
```

4. The script will convert the WAV file into a sequence of images and save them in the `images` folder.

5. The script will then load the generated images from the `images` folder and convert them back into a WAV file named `output.wav`.

6. Use the generated images to train your AI diffusion model for audio generation.

7. Once the model is trained, you can generate new images and use Project Resonance to convert them back into audio.

## How It Works

1. The `wav_to_images` function reads the WAV file and converts it into a sequence of RGB images. Each pixel in the image represents a specific part of the audio data, with the byte data written to the RGB channels.

2. The `images_to_wav` function takes a sequence of RGB images and converts them back into a WAV audio file. It reconstructs the audio data from the pixel values of the images, preserving the stereo field.

3. The `test` function demonstrates the usage of the conversion functions by converting a test WAV file into images, saving the images, loading them back, and converting them into a WAV file.

## Customization

You can customize the image dimensions and pixel expansion factor by modifying the `WIDTH`, `HEIGHT`, and `PIXEL_EXPANSION` variables in the `main.py` file. Adjusting these parameters will affect the quality and size of the generated images and the resulting audio.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Pillow library for image processing
- NumPy for efficient numerical operations
- tqdm for progress tracking

If you have any questions, suggestions, or issues, please feel free to open an issue or submit a pull request. Embark on your audio-image interconversion journey with Resonance!
