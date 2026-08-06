import librosa
import numpy as np
import os


def analyze_breathing(audio_path):

    if not os.path.exists(audio_path):
        return {"error": "Audio file not found."}

    audio, sr = librosa.load(audio_path, sr=16000)

    intervals = librosa.effects.split(
        audio,
        top_db=30
    )

    pause_list = []

    previous = 0

    for start, end in intervals:

        if start > previous:

            pause = (start - previous) / sr

            pause_list.append(pause)

        previous = end

    last_pause = (len(audio) - previous) / sr

    pause_list.append(last_pause)

    average_pause = np.mean(pause_list)

    maximum_pause = np.max(pause_list)

    minimum_pause = np.min(pause_list)

    if average_pause >= 0.20:
        status = "Natural Breathing"
    else:
        status = "Suspicious Breathing"

    score = min(100, average_pause * 400)

    return {

        "status": status,

        "average_pause": float(round(average_pause, 2)),

        "maximum_pause": float(round(maximum_pause, 2)),

        "minimum_pause": float(round(minimum_pause, 2)),

        "score": float(round(score, 2))

    }


if __name__ == "__main__":

    audio_path = input("Enter Audio Path : ")

    result = analyze_breathing(audio_path)

    print("\n==============================")
    print("Breathing Analysis")
    print("==============================")

    print(result)

    print("==============================")