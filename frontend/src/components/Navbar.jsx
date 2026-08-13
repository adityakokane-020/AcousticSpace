function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">
        🎵 <span>AcousticSpace</span>
      </div>

      <ul className="nav-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#upload">Upload</a></li>
        <li><a href="#result">Results</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;