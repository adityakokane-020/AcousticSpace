import "./App.css";

function App() {
  return (
    <div className="app">
      <div className="hero">
        <h1>🎵 AcousticSpace</h1>

        <h2>Deepfake Audio Detection System</h2>

        <p>
          Upload an audio recording and detect whether it is
          <strong> Real</strong> or <strong>AI Generated</strong> using our
          deep learning model.
        </p>

        <div className="buttons">
          <button className="upload-btn">Upload Audio</button>
          <button className="learn-btn">Learn More</button>
        </div>
      </div>
    </div>
  );
}

export default App;