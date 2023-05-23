import cv2
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotipy client credentials
client_id = '0b03ea7db99d42ec942e00127c9d4288'
client_secret = 'bd73f390741d4ec1ac4c22d0717a5761'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load the trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Function to capture user's emotion using webcam
def capture_emotion():
    # Open webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Display rectangle around detected face(s)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Emotion Detection', frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

    return "Happy"  # Simulated emotion for now

# Function to recommend music based on emotion
def recommend_music(emotion):
    # Simulated music recommendation
    recommended_songs = []

    # Search tracks based on the user's emotion
    results = sp.search(q=emotion, type='track', limit=5)

    # Extract track information
    for track in results['tracks']['items']:
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        recommended_songs.append(f"{track_name} by {artist_name}")

    return recommended_songs

# Main program
def main():
    # Capture user's emotion
    user_emotion = capture_emotion()

    # Get personalized music recommendations based on the user's emotion
    recommended_songs = recommend_music(user_emotion)

    # Print the recommended songs
    print("Recommended Songs:")
    for song in recommended_songs:
        print(song)

if __name__ == "__main__":
    main()
