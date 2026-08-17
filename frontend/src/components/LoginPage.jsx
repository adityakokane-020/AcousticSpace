function LoginPage({ onBack, onLogin }) {
  const handleSubmit = (event) => {
    event.preventDefault();

    onLogin();
  };

  return (
    <div className="login-page">

      <div className="login-background"></div>

      <div className="login-container">

        {/* Back */}
        <button
          type="button"
          className="back-home-btn"
          onClick={onBack}
        >
          ← Back to Home
        </button>

        {/* Brand */}
        <div className="login-brand">

          <div className="login-brand-icon">
            🎵
          </div>

          <h1>
            AcousticSpace
          </h1>

          <p>
            AI-powered deepfake audio detection
          </p>

        </div>

        {/* Login Card */}
        <div className="login-card">

          <div className="login-heading">

            <span className="login-label">
              SECURE ACCESS
            </span>

            <h2>
              Welcome back
            </h2>

            <p>
              Sign in to continue to your AcousticSpace dashboard.
            </p>

          </div>

          <form onSubmit={handleSubmit}>

            <div className="form-group">

              <label htmlFor="email">
                Email address
              </label>

              <input
                id="email"
                type="email"
                placeholder="you@example.com"
                required
              />

            </div>

            <div className="form-group">

              <label htmlFor="password">
                Password
              </label>

              <input
                id="password"
                type="password"
                placeholder="Enter your password"
                required
              />

            </div>

            <div className="login-options">

              <label className="remember-me">
                <input type="checkbox" />
                <span>Remember me</span>
              </label>

              <button
                type="button"
                className="forgot-password"
              >
                Forgot password?
              </button>

            </div>

            <button
              type="submit"
              className="login-submit"
            >
              Sign In
              <span>→</span>
            </button>

          </form>

          <div className="login-divider">
            <span>ACOUSTICSPACE</span>
          </div>

          <p className="login-demo-note">
            Demo authentication interface
          </p>

        </div>

      </div>

    </div>
  );
}

export default LoginPage;