import librosa
import numpy as np

# ===========================
# Load Audio
# ===========================

audio_path = input("Enter Audio Path: ")

audio, sr = librosa.load(audio_path, sr=16000)

duration = librosa.get_duration(y=audio, sr=sr)

print("\n==============================")
print("     Audio Information")
print("==============================")

print("Sample Rate :", sr)
print("Duration :", round(duration, 2), "seconds")
print("Total Samples :", len(audio))

# ===========================
# Silence Analysis
# ===========================

threshold = 0.01

silent_samples = np.sum(np.abs(audio) < threshold)

silent_percentage = (silent_samples / len(audio)) * 100

print("\n==============================")
print("    Silence Analysis")
print("==============================")

print("Silent Samples :", silent_samples)
print(f"Silence Percentage : {silent_percentage:.2f}%")

# ===========================
# Silence Intervals
# ===========================

print("\n==============================")
print("    Silence Intervals")
print("==============================")

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

        print(f"Silence : {pause:.2f} sec")

    previous = end

last_pause = (len(audio) - previous) / sr

pause_list.append(last_pause)

print(f"Last Silence : {last_pause:.2f} sec")

# ===========================
# Breathing Statistics
# ===========================

average_pause = np.mean(pause_list)

maximum_pause = np.max(pause_list)

minimum_pause = np.min(pause_list)

print("\n==============================")
print("  Breathing Statistics")
print("==============================")

print("Total Pauses :", len(pause_list))
print("Average Pause :", round(average_pause, 2), "sec")
print("Maximum Pause :", round(maximum_pause, 2), "sec")
print("Minimum Pause :", round(minimum_pause, 2), "sec")

# ===========================
# Breathing Result
# ===========================

if average_pause >= 0.20:
    status = "Natural Breathing"
else:
    status = "Suspicious Breathing"

print("\n==============================")
print("   Breathing Result")
print("==============================")

print("Status :", status)

# ===========================
# Breathing Score
# ===========================

score = min(100, average_pause * 400)

print("\n==============================")
print("   Breathing Score")
print("==============================")

print(f"Score : {score:.0f}%")

# ===========================
# Backend JSON Output
# ===========================

result = {

    "status": status,

    "average_pause": float(round(average_pause, 2)),

    "maximum_pause": float(round(maximum_pause, 2)),

    "minimum_pause": float(round(minimum_pause, 2)),

    "score": float(round(score, 2))

}

print("\n==============================")
print(" Backend JSON Output")
print("==============================")

print(result)

print("\n==============================")
print("Breathing Analysis Completed")
print("==============================")