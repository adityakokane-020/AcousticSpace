function LandingPage({
  onLogin,
  onGetStarted,
  onDataset,
  onReport,
}) {
  return (
    <div className="landing-page">

      {/* =========================
          NAVIGATION
      ========================== */}
      <nav className="landing-navbar">
        <div className="landing-logo">
          <span className="logo-icon">🎵</span>
          <span>AcousticSpace</span>
        </div>

        <button
          type="button"
          className="landing-login-btn"
          onClick={onLogin}
        >
          🔐 Login
        </button>
      </nav>


      {/* =========================
          HERO SECTION
      ========================== */}
      <main className="landing-hero">

        <div className="hero-badge">
          ✨ AI-Powered Audio Intelligence
        </div>

        <h1>
          Detect the Voice.
          <br />
          <span>Know the Truth.</span>
        </h1>

        <p>
          AcousticSpace uses advanced AI-powered audio analysis
          to identify whether a voice recording is authentic
          or AI-generated.
        </p>

        <div className="hero-actions">

          <button
            type="button"
            className="primary-hero-btn"
            onClick={onGetStarted}
          >
            🎧 Get Started
          </button>

          <button
            type="button"
            className="secondary-hero-btn"
            onClick={onLogin}
          >
            🔐 Login
          </button>

        </div>

        <div className="trust-text">
          Secure • Intelligent • Audio Analysis
        </div>

      </main>


      {/* =========================
          FEATURES
      ========================== */}
      <section className="landing-features">

        {/* Audio Analysis */}
        <div
          className="feature-card"
          role="button"
          tabIndex={0}
          onClick={onGetStarted}
          onKeyDown={(event) => {
            if (event.key === "Enter" || event.key === " ") {
              onGetStarted();
            }
          }}
        >
          <div className="feature-icon">
            🎙️
          </div>

          <h3>
            Audio Analysis
          </h3>

          <p>
            Upload an audio recording and analyze
            its acoustic characteristics.
          </p>

          <span className="feature-link">
            Start Analysis →
          </span>
        </div>


        {/* AI Detection */}
        <div
          className="feature-card"
          role="button"
          tabIndex={0}
          onClick={onGetStarted}
          onKeyDown={(event) => {
            if (event.key === "Enter" || event.key === " ") {
              onGetStarted();
            }
          }}
        >
          <div className="feature-icon">
            🤖
          </div>

          <h3>
            AI Detection
          </h3>

          <p>
            Machine-learning models analyze the recording
            to identify synthetic audio.
          </p>

          <span className="feature-link">
            Try Detection →
          </span>
        </div>


        {/* Clear Results */}
        <div
          className="feature-card"
          role="button"
          tabIndex={0}
          onClick={onGetStarted}
          onKeyDown={(event) => {
            if (event.key === "Enter" || event.key === " ") {
              onGetStarted();
            }
          }}
        >
          <div className="feature-icon">
            📊
          </div>

          <h3>
            Clear Results
          </h3>

          <p>
            View predictions, confidence values and
            detection history in one place.
          </p>

          <span className="feature-link">
            View Dashboard →
          </span>
        </div>

      </section>

<section className="landing-resources">

  <div className="section-heading">

    <span>
      EXPLORE ACOUSTICSPACE
    </span>

    <h2>
      Research & Analysis Resources
    </h2>

    <p>
      Access project datasets and generated detection reports.
    </p>

  </div>

  <div className="resource-grid">

    <button
      type="button"
      className="resource-card"
      onClick={onDataset}
    >
      <span className="resource-icon">
        📥
      </span>

      <div>
        <h3>
          Dataset
        </h3>

        <p>
          Explore the audio dataset used for
          model development and analysis.
        </p>
      </div>

      <span className="resource-arrow">
        →
      </span>
    </button>


    <button
      type="button"
      className="resource-card"
      onClick={onReport}
    >
      <span className="resource-icon">
        📄
      </span>

      <div>
        <h3>
          Detection Reports
        </h3>

        <p>
          Generate and download reports from
          your audio detection sessions.
        </p>
      </div>

      <span className="resource-arrow">
        →
      </span>
    </button>

  </div>

</section>
      {/* =========================
          HOW IT WORKS
      ========================== */}
      <section className="how-it-works">

        <div className="section-heading">

          <span>
            HOW IT WORKS
          </span>

          <h2>
            Three simple steps
          </h2>

        </div>


        <div className="steps">

          {/* Step 1 */}
          <div className="step">
            <strong>
              01
            </strong>

            <h3>
              Upload
            </h3>

            <p>
              Select an audio recording from your device.
            </p>
          </div>


          {/* Step 2 */}
          <div className="step">
            <strong>
              02
            </strong>

            <h3>
              Analyze
            </h3>

            <p>
              Our AI pipeline processes the audio.
            </p>
          </div>


          {/* Step 3 */}
          <div className="step">
            <strong>
              03
            </strong>

            <h3>
              Discover
            </h3>

            <p>
              Receive the detection result and confidence.
            </p>
          </div>

        </div>

      </section>


      {/* =========================
          FOOTER
      ========================== */}
      <footer className="landing-footer">

        <div>
          🎵 <strong>AcousticSpace</strong>
        </div>

        <p>
          AI-powered deepfake audio detection.
        </p>

        <span>
          © 2026 AcousticSpace
        </span>

      </footer>

    </div>
  );
}

export default LandingPage;