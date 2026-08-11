import { useEffect, useState } from "react";

function UploadSection({ onDetect }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [error, setError] = useState("");
  const [dragging, setDragging] = useState(false);
  const [audioUrl, setAudioUrl] = useState("");

  const validExtensions = [".wav", ".mp3", ".flac"];

  const validateFile = (file) => {
    if (!file) return;

    const fileName = file.name.toLowerCase();

    const isValid = validExtensions.some((extension) =>
      fileName.endsWith(extension)
    );

    if (!isValid) {
      setError(
        "❌ Invalid file. Please upload a .wav, .mp3, or .flac file."
      );
      setSelectedFile(null);
      setAudioUrl("");
      return;
    }

    setError("");
    setSelectedFile(file);

    const url = URL.createObjectURL(file);
    setAudioUrl(url);
  };

  const handleFileChange = (event) => {
    validateFile(event.target.files[0]);
  };

  const handleDrop = (event) => {
    event.preventDefault();
    setDragging(false);

    const file = event.dataTransfer.files[0];
    validateFile(file);
  };

  const handleDetect = () => {
    if (!selectedFile) {
      setError("⚠️ Please select an audio file first.");
      return;
    }

    onDetect(selectedFile);
  };

  const removeFile = () => {
    setSelectedFile(null);
    setAudioUrl("");
    setError("");
  };

  useEffect(() => {
    return () => {
      if (audioUrl) {
        URL.revokeObjectURL(audioUrl);
      }
    };
  }, [audioUrl]);

  return (
    <section className="upload-section">
      <h2>Upload Audio File</h2>

      <p className="upload-subtitle">
        Upload an audio recording and let AcousticSpace analyze it.
      </p>

      <div
        className={`upload-box ${dragging ? "dragging" : ""}`}
        onDragOver={(event) => {
          event.preventDefault();
          setDragging(true);
        }}
        onDragLeave={() => setDragging(false)}
        onDrop={handleDrop}
      >
        <div className="upload-icon">🎧</div>

        {dragging ? (
          <h3>Drop your audio file here 🎵</h3>
        ) : (
          <>
            <h3>Drag & Drop your audio here</h3>
            <p>or</p>
          </>
        )}

        <input
          id="audio-upload"
          type="file"
          accept=".wav,.mp3,.flac"
          onChange={handleFileChange}
          hidden
        />

        <label
          htmlFor="audio-upload"
          className="custom-upload-btn"
        >
          📂 Choose Audio File
        </label>

        <p className="formats">
          Supported formats: .wav • .mp3 • .flac
        </p>

        {selectedFile && (
          <div className="file-preview">
            <p className="selected-file">
              🎵 {selectedFile.name}
            </p>

            {/* Waveform */}
            <div className="waveform">
              {Array.from({ length: 35 }).map((_, index) => (
                <span
                  key={index}
                  style={{
                    height: `${20 + Math.random() * 55}px`,
                  }}
                ></span>
              ))}
            </div>

            {/* Audio Player */}
            <audio
              controls
              className="audio-player"
              src={audioUrl}
            />

            <button
              className="remove-btn"
              onClick={removeFile}
            >
              ✕ Remove File
            </button>
          </div>
        )}

        {error && (
          <p className="error-text">
            {error}
          </p>
        )}

        <button
          className="detect-btn"
          onClick={handleDetect}
        >
          🔍 Detect Deepfake
        </button>
      </div>
    </section>
  );
}

export default UploadSection;