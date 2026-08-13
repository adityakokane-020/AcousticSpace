import { useEffect, useState } from "react";

function UploadSection({ onDetect }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [error, setError] = useState("");
  const [dragging, setDragging] = useState(false);
  const [audioUrl, setAudioUrl] = useState("");

  const validExtensions = [".wav", ".mp3"];

  const validateFile = (file) => {
    if (!file) return false;

    const fileName = file.name.toLowerCase();

    const isValid = validExtensions.some((extension) =>
      fileName.endsWith(extension)
    );

    if (!isValid) {
      setError("Please select a .wav or .mp3 audio file.");
      return false;
    }

    setError("");
    return true;
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (!validateFile(file)) {
      return;
    }

    setSelectedFile(file);
    setAudioUrl(URL.createObjectURL(file));
  };

  const handleDrop = (event) => {
    event.preventDefault();
    setDragging(false);

    const file = event.dataTransfer.files[0];

    if (!validateFile(file)) {
      return;
    }

    setSelectedFile(file);
    setAudioUrl(URL.createObjectURL(file));
  };

  const handleDetect = () => {
    if (!selectedFile) {
      setError("Please select an audio file first.");
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
          accept=".wav,.mp3"
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
          Supported formats: .wav • .mp3
        </p>

        {selectedFile && (
          <div className="file-preview">
            <p className="selected-file">
              🎵 {selectedFile.name}
            </p>

            <audio
              controls
              className="audio-player"
              src={audioUrl}
            />

            <button
              className="remove-btn"
              onClick={removeFile}
            >
              ❌ Remove File
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