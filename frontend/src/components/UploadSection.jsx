import { useState } from "react";

function UploadSection({ onDetect }) {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  return (
    <section className="upload-section">
      <h2>Upload Audio File</h2>

      <div className="upload-box">
        <p>🎵 Drag & Drop your audio here</p>
        <p>or</p>

        <input
          type="file"
          accept=".wav,.mp3,.flac"
          onChange={handleFileChange}
        />

        {selectedFile && (
          <p className="file-name">
            Selected File: <strong>{selectedFile.name}</strong>
          </p>
        )}

        <button
          className="upload-btn"
          onClick={onDetect}
        >
          Detect Deepfake
        </button>
      </div>
    </section>
  );
}

export default UploadSection;