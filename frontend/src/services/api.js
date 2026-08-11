export const detectAudio = async (audioFile) => {
  // Backend API will be added here later

  console.log("Selected File:", audioFile);

  // Temporary mock response
  return {
    result: "✅ Real Audio",
    confidence: "98.4%",
    status: "Authentic",
  };
};