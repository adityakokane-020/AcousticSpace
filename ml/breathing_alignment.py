import librosa
import numpy as np
import os


# ==========================================
# BREATHING - SPEECH ALIGNMENT
# ==========================================

audio_path = input("Enter Audio Path : ")

if not os.path.exists(audio_path):
    print("Audio file not found!")
    exit()


# Load audio
audio, sr = librosa.load(audio_path, sr=16000)

duration = len(audio) / sr


print("\n==============================")
print("Breathing - Speech Alignment")
print("==============================")

print("Duration :", round(duration, 2), "sec")


# ==========================================
# 1. SPEECH ACTIVITY
# ==========================================

speech_segments = librosa.effects.split(
    audio,
    top_db=30
)

print("\n==============================")
print("Speech Segments")
print("==============================")


speech_list = []

for start, end in speech_segments:

    start_time = start / sr
    end_time = end / sr

    speech_list.append({
        "start": start_time,
        "end": end_time
    })

    print(
        "Speech :",
        round(start_time, 2),
        "-",
        round(end_time, 2),
        "sec"
    )


# ==========================================
# 2. SILENCE / BREATHING DETECTION
# ==========================================

rms = librosa.feature.rms(
    y=audio,
    frame_length=1024,
    hop_length=512
)[0]

threshold = np.max(rms) * 0.08

silent_frames = np.where(rms < threshold)[0]

silent_times = librosa.frames_to_time(
    silent_frames,
    sr=sr,
    hop_length=512
)


breathing_events = []

if len(silent_times) > 0:

    start = silent_times[0]
    previous = silent_times[0]

    for current in silent_times[1:]:

        if current - previous > 0.06:

            duration_pause = previous - start

            if duration_pause >= 0.10:

                breathing_events.append({
                    "start": round(float(start), 2),
                    "end": round(float(previous), 2),
                    "duration": round(float(duration_pause), 2)
                })

            start = current

        previous = current


    # Last silence
    duration_pause = previous - start

    if duration_pause >= 0.10:

        breathing_events.append({
            "start": round(float(start), 2),
            "end": round(float(previous), 2),
            "duration": round(float(duration_pause), 2)
        })


print("\n==============================")
print("Breathing Candidates")
print("==============================")


if len(breathing_events) == 0:

    print("No breathing events detected.")

else:

    for event in breathing_events:

        print(
            "Breathing :",
            event["start"],
            "-",
            event["end"],
            "sec"
        )


# ==========================================
# 3. SPEECH ACTIVITY / SYLLABLE PROXY
# ==========================================

onset_frames = librosa.onset.onset_detect(
    y=audio,
    sr=sr,
    backtrack=True
)

onset_times = librosa.frames_to_time(
    onset_frames,
    sr=sr
)


print("\n==============================")
print("Speech Activity / Syllable Proxy")
print("==============================")

print(
    "Detected Speech Events :",
    len(onset_times)
)


# ==========================================
# 4. BREATHING - SPEECH ALIGNMENT
# ==========================================

aligned_events = 0


for breath in breathing_events:

    breath_end = breath["end"]

    for onset in onset_times:

        difference = onset - breath_end

        # Speech activity within 1 second
        # after breathing/pause

        if 0 <= difference <= 1.0:

            aligned_events += 1
            break


# ==========================================
# 5. ALIGNMENT SCORE
# ==========================================

if len(breathing_events) > 0:

    alignment_score = (
        aligned_events / len(breathing_events)
    ) * 100

else:

    alignment_score = 0


alignment_score = round(
    min(alignment_score, 100),
    2
)


# ==========================================
# 6. STATUS
# ==========================================

if len(breathing_events) == 0:

    alignment_status = "Insufficient Breathing Events"

elif alignment_score >= 70:

    alignment_status = "Good Breathing-Speech Alignment"

elif alignment_score >= 40:

    alignment_status = "Moderate Breathing-Speech Alignment"

else:

    alignment_status = "Poor Breathing-Speech Alignment"


# ==========================================
# 7. FINAL RESULT
# ==========================================

print("\n==============================")
print("Alignment Result")
print("==============================")

print(
    "Breathing Events :",
    len(breathing_events)
)

print(
    "Speech Events :",
    len(onset_times)
)

print(
    "Aligned Events :",
    aligned_events
)

print(
    "Alignment Score :",
    alignment_score,
    "%"
)

print(
    "Status :",
    alignment_status
)

print("==============================")