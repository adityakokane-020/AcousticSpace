import librosa
import numpy as np
import os


def analyze_alignment(audio_path):

    if not os.path.exists(audio_path):
        return {
            "error": "Audio file not found"
        }

    # Load audio
    audio, sr = librosa.load(
        audio_path,
        sr=16000
    )

    # ==========================================
    # 1. SPEECH ACTIVITY
    # ==========================================

    speech_segments = librosa.effects.split(
        audio,
        top_db=30
    )

    speech_list = []

    for start, end in speech_segments:

        start_time = start / sr
        end_time = end / sr

        speech_list.append({
            "start": round(float(start_time), 2),
            "end": round(float(end_time), 2)
        })

    # ==========================================
    # 2. SILENCE / BREATHING DETECTION
    # ==========================================

    rms = librosa.feature.rms(
        y=audio,
        frame_length=1024,
        hop_length=512
    )[0]

    threshold = np.max(rms) * 0.08

    silent_frames = np.where(
        rms < threshold
    )[0]

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
                        "duration": round(
                            float(duration_pause),
                            2
                        )
                    })

                start = current

            previous = current

        # Last silence
        duration_pause = previous - start

        if duration_pause >= 0.10:

            breathing_events.append({
                "start": round(float(start), 2),
                "end": round(float(previous), 2),
                "duration": round(
                    float(duration_pause),
                    2
                )
            })

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

    # ==========================================
    # 4. BREATHING - SPEECH ALIGNMENT
    # ==========================================

    aligned_events = 0

    for breath in breathing_events:

        breath_end = breath["end"]

        for onset in onset_times:

            difference = onset - breath_end

            if 0 <= difference <= 1.0:

                aligned_events += 1
                break

    # ==========================================
    # 5. ALIGNMENT SCORE
    # ==========================================

    if len(breathing_events) > 0:

        alignment_score = (
            aligned_events /
            len(breathing_events)
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

        alignment_status = (
            "Insufficient Breathing Events"
        )

    elif alignment_score >= 70:

        alignment_status = (
            "Good Breathing-Speech Alignment"
        )

    elif alignment_score >= 40:

        alignment_status = (
            "Moderate Breathing-Speech Alignment"
        )

    else:

        alignment_status = (
            "Poor Breathing-Speech Alignment"
        )

    # ==========================================
    # 7. RESULT
    # ==========================================

    result = {

        "breathing_events": len(
            breathing_events
        ),

        "speech_events": len(
            onset_times
        ),

        "aligned_events": aligned_events,

        "alignment_score": alignment_score,

        "status": alignment_status

    }

    return result


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    audio_path = input(
        "Enter Audio Path : "
    )

    result = analyze_alignment(
        audio_path
    )

    print("\n==============================")
    print("Breathing-Speech Alignment")
    print("==============================")

    print(result)

    print("==============================")