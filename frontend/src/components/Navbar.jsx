function Navbar({
  onHome,
  onDataset,
  onReport,
  onLogout,
}) {
  return (
    <nav className="navbar">

      <button
        type="button"
        className="navbar-logo"
        onClick={onHome}
      >
        <span>🎵</span>
        <strong>AcousticSpace</strong>
      </button>

      <div className="nav-links">

        <button
          type="button"
          onClick={onHome}
        >
          Home
        </button>

        <a href="#upload">
          Upload
        </a>

        <a href="#result">
          Results
        </a>

        <a href="#history">
          History
        </a>

        <button
          type="button"
          onClick={onDataset}
        >
          Dataset
        </button>

        <button
          type="button"
          onClick={onReport}
        >
          Reports
        </button>

        <button
          type="button"
          className="logout-btn"
          onClick={onLogout}
        >
          Logout
        </button>

      </div>

    </nav>
  );
}

export default Navbar;