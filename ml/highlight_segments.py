import os
import librosa


def detect_segments(audio_path):

    if not os.path.exists(audio_path):
        return {
            "error": "Audio file not found."
        }

    audio, sr = librosa.load(audio_path, sr=16000)

    intervals = librosa.effects.split(
        audio,
        top_db=30
    )

    segments = []

    for start, end in intervals:

        start_time = start / sr
        end_time = end / sr

        duration = end_time - start_time

        if duration >= 1.0:

            segment = {

                "start": float(round(start_time, 2)),

                "end": float(round(end_time, 2)),

                "duration": float(round(duration, 2))

            }

            segments.append(segment)

    return segments


if __name__ == "__main__":

    audio_path = input("Enter Audio Path : ")

    result = detect_segments(audio_path)

    print("\n==============================")
    print("Highlighted Segments")
    print("==============================")

    if len(result) == 0:
        print("No suspicious segments found.")

    else:

        for segment in result:

            print(segment)

    print("==============================")