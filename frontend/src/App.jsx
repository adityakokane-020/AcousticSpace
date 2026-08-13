import { useState } from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import UploadSection from "./components/UploadSection";
import ResultCard from "./components/ResultCard";
import Footer from "./components/Footer";

function App() {
  const [prediction, setPrediction] = useState({
    result: "No Prediction Yet",
    confidence: "--",
    status: "Waiting",
  });

  const [loading, setLoading] = useState(false);

  const handleDetect = () => {
    setLoading(true);

    // Simulate API call
    setTimeout(() => {
      setPrediction({
        result: "✅ Real Audio",
        confidence: "98.4%",
        status: "Authentic",
      });

      setLoading(false);
    }, 2000);
  };

  return (
    <>
      <Navbar />

      <div className="hero">
        <h1>🎵 AcousticSpace</h1>

        <h2>Deepfake Audio Detection System</h2>

        <p>
          Upload an audio recording and detect whether it is
          <strong> Real </strong>
          or
          <strong> AI Generated</strong>.
        </p>

        <button>Learn More</button>
      </div>

      <UploadSection onDetect={handleDetect} />

      {loading ? (
        <h2 className="loading-text">Analyzing Audio...</h2>
      ) : (
        <ResultCard
          result={prediction.result}
          confidence={prediction.confidence}
          status={prediction.status}
        />
      )}

      <Footer />
    </>
  );
}

export default App;