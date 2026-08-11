import { useState } from "react";
import "./App.css";

import Navbar from "./components/Navbar";
import UploadSection from "./components/UploadSection";
import ResultCard from "./components/ResultCard";
import Footer from "./components/Footer";

import { detectAudio } from "./services/api";

function App() {
  const [prediction, setPrediction] = useState({
    result: "No Prediction Yet",
    confidence: "--",
    status: "Waiting",
  });

  const [loading, setLoading] = useState(false);

  const [history, setHistory] = useState([]);

  const handleDetect = async (file) => {
    if (!file) return;

    setLoading(true);

    try {
      const response = await detectAudio(file);

      setPrediction(response);

      // Add prediction to history
      const newHistoryItem = {
        id: Date.now(),
        fileName: file.name,
        result: response.result,
        confidence: response.confidence,
        status: response.status,
      };

      setHistory((previousHistory) => [
        newHistoryItem,
        ...previousHistory,
      ]);
    } catch (error) {
      console.error("Detection Error:", error);

      setPrediction({
        result: "Detection Failed",
        confidence: "--",
        status: "Error",
      });
    } finally {
      setLoading(false);
    }
  };

  const scrollToUpload = () => {
    document.getElementById("upload")?.scrollIntoView({
      behavior: "smooth",
    });
  };

  return (
    <div className="app">

      <Navbar />

      {/* HERO */}
      <section id="home" className="hero">
        <div className="hero-content">

          <div className="hero-icon">
            🎵
          </div>

          <h1>AcousticSpace</h1>

          <h2>
            AI Powered Deepfake Audio Detection
          </h2>

          <p>
            Upload an audio recording and let our AI analyze
            whether the voice is <strong>Real</strong> or{" "}
            <strong>AI Generated</strong>.
          </p>

          <button
            className="hero-btn"
            onClick={scrollToUpload}
          >
            🎧 Get Started
          </button>

        </div>
      </section>

      {/* UPLOAD */}
      <section id="upload">
        <UploadSection onDetect={handleDetect} />
      </section>

      {/* RESULT */}
      <section id="result">

        {loading ? (
          <div className="loading-container">

            <div className="spinner"></div>

            <h2 className="loading-text">
              Analyzing Audio...
            </h2>

            <p>
              Please wait while AcousticSpace processes
              your audio.
            </p>

          </div>
        ) : (
          <ResultCard
            result={prediction.result}
            confidence={prediction.confidence}
            status={prediction.status}
          />
        )}

      </section>

      {/* DETECTION HISTORY */}
      <section className="history-section">

        <h2>📜 Detection History</h2>

        <p className="history-subtitle">
          Previously analyzed audio files
        </p>

        {history.length === 0 ? (

          <div className="empty-history">
            <span>🎵</span>
            <p>No audio analyzed yet.</p>
          </div>

        ) : (

          <div className="history-list">

            {history.map((item) => (

              <div
                className="history-card"
                key={item.id}
              >

                <div className="history-file">
                  🎵
                  <div>
                    <strong>
                      {item.fileName}
                    </strong>

                    <small>
                      {item.status}
                    </small>
                  </div>
                </div>

                <div className="history-result">
                  <span>
                    {item.result}
                  </span>

                  <strong>
                    {item.confidence}
                  </strong>
                </div>

              </div>

            ))}

          </div>

        )}

      </section>

      {/* FOOTER */}
      <section id="contact">
        <Footer />
      </section>

    </div>
  );
}

export default App;