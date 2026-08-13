function ResultCard({ result, confidence, status }) {
  const progress = parseFloat(confidence) || 0;

  return (
    <section className="result-section">
      <h2>Prediction Result</h2>

      <div className="result-card">
        <h3>{result}</h3>

        <p>
          Confidence: <strong>{confidence}</strong>
        </p>

        <div className="progress-bar">
          <div
            className="progress-fill"
            style={{ width: `${progress}%` }}
          ></div>
        </div>

        <p>
          Status:
          <span
            className={
              status === "Authentic"
                ? "success"
                : status === "Fake"
                ? "warning"
                : ""
            }
          >
            {" "}
            {status}
          </span>
        </p>
      </div>
    </section>
  );
}

export default ResultCard;