function UploadSection() {
  return (
    <section className="upload-section">
      <h2>Upload Audio File</h2>

      <div className="upload-box">
        <p>🎵 Drag & Drop your audio here</p>
        <p>or</p>

        <input
          type="file"
          accept=".wav,.mp3,.flac"
        />

        <button className="upload-btn">
          Detect Deepfake
        </button>
      </div>
    </section>
  );
}

export default UploadSection;