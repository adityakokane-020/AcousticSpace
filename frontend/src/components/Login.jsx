import { useState } from "react";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (username.trim() !== "" && password.trim() !== "") {
      setError("");
      onLogin();
    } else {
      setError("Please enter username and password");
    }
  };

  return (
    <div className="login-page">
      <div className="login-card">
        <h1>🎵 AcousticSpace</h1>

        <h2>Login</h2>

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Enter Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            type="password"
            placeholder="Enter Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          {error && (
            <p className="login-error">
              {error}
            </p>
          )}

          <button type="submit">
            Login
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;