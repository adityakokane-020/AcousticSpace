import Navbar from "./components/Navbar";
import UploadSection from "./components/UploadSection";
import ResultCard from "./components/ResultCard";

function App() {
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

      <UploadSection />

      <ResultCard />
    </>
  );
}

export default App;