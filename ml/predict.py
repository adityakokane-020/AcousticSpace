from inference import predict_audio

result = predict_audio("ml/audio/Recording.wav")

print("\nPrediction :", result["prediction"])
print("Confidence :", result["confidence"], "%")