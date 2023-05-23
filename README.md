# Moodify

Moodify is a simple application that suggests songs based on the user's mood captured through a webcam using OpenCV. It utilizes computer vision techniques to detect the user's facial expression and classify their emotion. Based on the detected emotion, Moodify recommends a curated list of songs that match the user's mood.

## Features

- Real-time emotion detection through webcam using OpenCV.
- Classification of emotions into Happy, Sad, Angry, and more.
- Integration with the Spotify API to fetch personalized song recommendations.
- User-friendly interface displaying the detected emotion and recommended songs.
- Easy setup and usage.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/moodify.git`
2. Navigate to the project directory: `cd moodify`

## Usage

1. Ensure you have a working webcam connected to your system.
2. Run the `main.py` script: `python main.py`
3. A new window will open displaying the webcam feed and the detected emotion.
4. Based on the detected emotion, Moodify will suggest a list of songs that match the mood.
5. Enjoy the recommended songs and adjust your mood accordingly!

## Credits

Moodify utilizes the following technologies and libraries:

- OpenCV: https://opencv.org/
- Spotify API: https://developer.spotify.com/
- Spotipy: https://spotipy.readthedocs.io/
- Haar Cascade Classifier: https://docs.opencv.org/4.5.3/d7/d8b/tutorial_py_face_detection.html
- DeepFace: https://pypi.org/project/deepface/

## Contributing

Contributions to Moodify are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

