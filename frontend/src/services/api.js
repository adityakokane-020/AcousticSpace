const API_URL = "http://127.0.0.1:8000";

export const detectAudio = async (audioFile) => {
  const formData = new FormData();
  formData.append("file", audioFile);

  const response = await fetch(`${API_URL}/predict`, {
    method: "POST",
    body: formData,
  });

  console.log("Backend status:", response.status);

  const data = await response.json();

  console.log("Backend response:", data);

  if (!response.ok) {
    throw new Error(data.detail || "Backend request failed");
  }

  return {
    result: data.prediction?.prediction ?? "Unknown",
    confidence: data.prediction?.confidence ?? 0,
    status:
      data.prediction?.prediction === "Real"
        ? "Authentic"
        : "AI Generated",
    filename: data.filename,
    audioInfo: data.audio_info,
    inferenceTime: data.inference_time,
  };
};