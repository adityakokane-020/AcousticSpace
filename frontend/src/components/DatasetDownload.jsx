function DatasetDownload() {
  const handleDownload = () => {
    const datasetInfo = `
ACOUSTICSPACE
Audio Deepfake Detection Dataset
================================

Dataset Overview

AcousticSpace uses real and AI-generated audio samples
for deepfake audio detection and classification.

Categories:
- Real Audio
- AI-Generated Audio

Purpose:
Training and evaluation of audio deepfake detection models.

Project:
AcousticSpace
AI-Powered Deepfake Audio Detection
`;

    const blob = new Blob([datasetInfo], {
      type: "text/plain;charset=utf-8",
    });

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    link.download = "AcousticSpace-Dataset-Information.txt";

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
          DATA RESOURCES
        </span>

        <h1>
          Audio Dataset
        </h1>

        <p>
          Explore the data used to develop and evaluate
          the AcousticSpace deepfake audio detection system.
        </p>

      </section>


      {/* Main card */}
      <section className="dataset-main-card">

        <div className="dataset-card-header">

          <div className="dataset-icon">
            D
          </div>

          <div>
            <span className="card-label">
              DATASET
            </span>

            <h2>
              Audio Deepfake Dataset
            </h2>

            <p>
              Dataset structure for real and AI-generated
              audio classification.
            </p>
          </div>

        </div>


        {/* Dataset categories */}
        <div className="dataset-categories">

          <div className="dataset-category">

            <div className="category-icon real">
              R
            </div>

            <div>
              <strong>
                Real Audio
              </strong>

              <span>
                Authentic human recordings
              </span>
            </div>

          </div>


          <div className="dataset-category">

            <div className="category-icon synthetic">
              AI
            </div>

            <div>
              <strong>
                AI-Generated Audio
              </strong>

              <span>
                Synthetic or manipulated recordings
              </span>
            </div>

          </div>

        </div>


        {/* Information */}
        <div className="dataset-info-grid">

          <div>
            <span>
              DATA TYPE
            </span>

            <strong>
              Audio
            </strong>
          </div>

          <div>
            <span>
              CLASSIFICATION
            </span>

            <strong>
              Binary
            </strong>
          </div>

          <div>
            <span>
              CLASSES
            </span>

            <strong>
              Real / AI
            </strong>
          </div>

          <div>
            <span>
              APPLICATION
            </span>

            <strong>
              Deepfake Detection
            </strong>
          </div>

        </div>


        {/* Download */}
        <div className="resource-action">

          <div>
            <strong>
              Dataset information
            </strong>

            <p>
              Download the available dataset documentation.
            </p>
          </div>

          <button
            type="button"
            className="primary-resource-btn"
            onClick={handleDownload}
          >
            Download
          </button>

        </div>

      </section>


      {/* Note */}
      <section className="resource-note">

        <strong>
          About this resource
        </strong>

        <p>
          The dataset supports the development and evaluation
          of AcousticSpace's audio classification pipeline.
        </p>

      </section>

    </main>
  );
}

export default DatasetDownload;