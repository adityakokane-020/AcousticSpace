const API_URL = "http://localhost:8000";

export const detectAudio = async (audioFile) => {
  const formData = new FormData();

  formData.append("file", audioFile);

  const response = await fetch(`${API_URL}/predict`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Failed to analyze audio");
  }

  const data = await response.json();

  return {
    result: data.prediction.prediction,
    confidence: data.prediction.confidence,
    status:
      data.prediction.prediction === "Real"
        ? "Authentic"
        : "AI Generated",
    filename: data.filename,
    audioInfo: data.audio_info,
    inferenceTime: data.inference_time,
  };
};