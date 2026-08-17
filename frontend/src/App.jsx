import ReportDownload from "./components/ReportDownload";
import DatasetDownload from "./components/DatasetDownload";
import { useState } from "react";
import "./App.css";

import LandingPage from "./components/LandingPage";
import LoginPage from "./components/LoginPage";
import Navbar from "./components/Navbar";
import UploadSection from "./components/UploadSection";
import ResultCard from "./components/ResultCard";
import Footer from "./components/Footer";

import { detectAudio } from "./services/api";

function App() {
  // Current page
  const [page, setPage] = useState("landing");

  // Prediction state
  const [prediction, setPrediction] = useState({
    result: "No Prediction Yet",
    confidence: "--",
    status: "Waiting",
  });

  // Loading state
  const [loading, setLoading] = useState(false);

  // Detection history
  const [history, setHistory] = useState([]);

  // Handle audio detection
  const handleDetect = async (file) => {
    if (!file) return;

    setLoading(true);

    try {
      const response = await detectAudio(file);

      setPrediction(response);

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

  // Go directly to upload/dashboard
  const handleGetStarted = () => {
    setPage("dashboard");

    setTimeout(() => {
      document.getElementById("upload")?.scrollIntoView({
        behavior: "smooth",
      });
    }, 100);
  };

  // Login success
  const handleLogin = () => {
    setPage("dashboard");
  };

  // Landing page
  if (page === "landing") {
    return (
      <LandingPage
        onLogin={() => setPage("login")}
        onGetStarted={handleGetStarted}
      />
    );
  }

  // Login page
  if (page === "login") {
    return (
      <LoginPage
        onBack={() => setPage("landing")}
        onLogin={handleLogin}
      />
    );
  }

  // Dashboard
  return (
    <div className="app">

      {/* NAVBAR */}
      <Navbar
        onHome={() => setPage("landing")}
        onLogout={() => setPage("landing")}
      />

      {/* DASHBOARD HEADER */}
      <section className="dashboard-header">

        <div>
          <span className="dashboard-label">
            AI AUDIO INTELLIGENCE
          </span>

          <h1>
            Welcome to AcousticSpace
          </h1>

          <p>
            Analyze your audio recordings and detect
            AI-generated voices.
          </p>
        </div>

        <div className="dashboard-status">
          <span className="status-dot"></span>
          Detection System Ready
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
            {/* DATASET */}
      <DatasetDownload />

      {/* REPORT */}
      <ReportDownload
        prediction={prediction}
        history={history}
      />

      {/* DETECTION HISTORY */}
      <section className="history-section">

        <div className="section-heading">
          <span>ANALYSIS ACTIVITY</span>

          <h2>
            📜 Detection History
          </h2>

          <p className="history-subtitle">
            Previously analyzed audio files
          </p>
        </div>

        {history.length === 0 ? (

          <div className="empty-history">
            <span>🎵</span>

            <p>
              No audio analyzed yet.
            </p>

            <small>
              Upload an audio file to begin your first analysis.
            </small>
          </div>

        ) : (

          <div className="history-list">

            {history.map((item) => (

              <div
                className="history-card"
                key={item.id}
              >

                <div className="history-file">

                  <span>🎵</span>

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