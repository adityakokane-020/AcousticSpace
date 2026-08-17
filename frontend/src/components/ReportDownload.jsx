function ReportDownload({ prediction, history }) {

  const latestResult =
    prediction?.result &&
    prediction.result !== "No Prediction Yet"
      ? prediction.result
      : "No prediction available";

  const confidence =
    prediction?.confidence || "--";

  const status =
    prediction?.status || "Waiting";


  const handleDownloadReport = () => {

    const generatedAt =
      new Date().toLocaleString();

    const reportContent = `
ACOUSTICSPACE
AI-POWERED DEEPFAKE AUDIO DETECTION
====================================

DETECTION REPORT

Generated:
${generatedAt}

LATEST ANALYSIS
---------------

Result:
${latestResult}

Confidence:
${confidence}

Status:
${status}


DETECTION HISTORY
-----------------

${
  history.length === 0
    ? "No previous detections."
    : history
        .map(
          (item, index) =>
            `${index + 1}. ${item.fileName}
Result: ${item.result}
Confidence: ${item.confidence}
Status: ${item.status}
`
        )
        .join("\n")
}


ABOUT ACOUSTICSPACE
-------------------

AcousticSpace is an AI-powered system designed
to analyze audio recordings and identify whether
they are authentic or AI-generated.

This report represents the current detection session.
`;

    const blob = new Blob(
      [reportContent],
      {
        type: "text/plain;charset=utf-8",
      }
    );

    const url =
      URL.createObjectURL(blob);

    const link =
      document.createElement("a");

    link.href = url;

    link.download =
      "AcousticSpace-Detection-Report.txt";

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

    URL.revokeObjectURL(url);
  };


  return (
    <main className="resource-page">

      {/* Header */}
      <section className="resource-hero">

        <span className="resource-eyebrow">
          ANALYSIS DOCUMENTATION
        </span>

        <h1>
          Detection Report
        </h1>

        <p>
          Review the latest audio analysis and generate
          a downloadable detection report.
        </p>

      </section>


      {/* Latest result */}
      <section className="report-main-card">

        <div className="report-card-top">

          <div>

            <span className="card-label">
              LATEST ANALYSIS
            </span>

            <h2>
              Detection Summary
            </h2>

          </div>

          <div className="report-status">
            {status}
          </div>

        </div>


        {/* Metrics */}
        <div className="report-metrics">

          <div className="report-metric">

            <span>
              RESULT
            </span>

            <strong className="result-value">
              {latestResult}
            </strong>

          </div>


          <div className="report-metric">

            <span>
              CONFIDENCE
            </span>

            <strong>
              {confidence}
            </strong>

          </div>


          <div className="report-metric">

            <span>
              DETECTIONS
            </span>

            <strong>
              {history.length}
            </strong>

          </div>

        </div>


        {/* History */}
        <div className="report-history">

          <div className="report-section-title">

            <div>
              <span className="card-label">
                ACTIVITY
              </span>

              <h3>
                Detection History
              </h3>
            </div>

            <span className="history-count">
              {history.length} total
            </span>

          </div>


          {history.length === 0 ? (

            <div className="report-empty">
              No detection history available yet.
            </div>

          ) : (

            <div className="report-history-list">

              {history.map((item) => (

                <div
                  className="report-history-item"
                  key={item.id}
                >

                  <div>

                    <strong>
                      {item.fileName}
                    </strong>

                    <span>
                      {item.status}
                    </span>

                  </div>

                  <div className="history-item-result">

                    <strong>
                      {item.result}
                    </strong>

                    <span>
                      {item.confidence}
                    </span>

                  </div>

                </div>

              ))}

            </div>

          )}

        </div>


        {/* Download */}
        <div className="resource-action">

          <div>

            <strong>
              Download analysis report
            </strong>

            <p>
              Save the current detection summary
              and history for documentation.
            </p>

          </div>

          <button
            type="button"
            className="primary-resource-btn"
            onClick={handleDownloadReport}
          >
            Download Report
          </button>

        </div>

      </section>

    </main>
  );
}

export default ReportDownload;