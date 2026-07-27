import matplotlib.pyplot as plt
from rir import extract_rir

audio = "ml/audio/Recording.wav"

rir = extract_rir(audio)

plt.figure(figsize=(10,4))
plt.plot(rir)
plt.title("Room Impulse Response Features")
plt.xlabel("Frequency Bin")
plt.ylabel("Normalized Energy")
plt.grid(True)

plt.savefig("ml/rir_plot.png")
plt.show()