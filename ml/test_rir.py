from rir import extract_rir

audio = "ml/audio/Recording.wav"

rir = extract_rir(audio)

print("Length :", len(rir))

print("First 10 Values")

print(rir[:10])