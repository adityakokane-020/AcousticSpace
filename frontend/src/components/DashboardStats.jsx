function DashboardStats({ prediction }) {
  const isFake = prediction.result.includes("Fake");
  const hasPrediction = prediction.result !== "No Prediction Yet";

  return (
    <section className="dashboard-stats">
      <div className="stat-card">
        <span className="stat-icon">🔍</span>
        <h3>Detection Status</h3>
        <p>
          {hasPrediction ? "Analysis Complete" : "Waiting"}
        </p>
      </div>

      <div className="stat-card">
        <span className="stat-icon">🎯</span>
        <h3>Confidence</h3>
        <p>
          {prediction.confidence}
        </p>
      </div>

      <div className="stat-card">
        <span className="stat-icon">
          {isFake ? "🚨" : "🎙️"}
        </span>
        <h3>Prediction</h3>
        <p>
          {hasPrediction
            ? isFake
              ? "Fake Audio"
              : "Real Audio"
            : "No Result"}
        </p>
      </div>

      <div className="stat-card">
        <span className="stat-icon">🧠</span>
        <h3>Model</h3>
        <p>AcousticCNN</p>
      </div>
    </section>
  );
}

export default DashboardStats;