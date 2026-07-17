function ResultCard() {
  return (
    <section className="result-section">
      <h2>Prediction Result</h2>

      <div className="result-card">
        <h3>✅ Real Audio</h3>

        <p>
          Confidence:
          <strong> 98.4%</strong>
        </p>

        <p>
          Status:
          <span className="success"> Authentic</span>
        </p>
      </div>
    </section>
  );
}

export default ResultCard;