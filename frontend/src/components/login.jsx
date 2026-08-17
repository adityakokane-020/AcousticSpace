import { useState } from "react";

function Login({ onClose }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!email || !password) {
      alert("Please enter your email and password.");
      return;
    }

    alert("Login successful!");
    onClose();
  };

  return (
    <div className="login-overlay">
      <div className="login-card">
        <button className="login-close" onClick={onClose}>
          ✕
        </button>

        <div className="login-icon">🔐</div>

        <h2>Welcome Back</h2>

        <p>Login to AcousticSpace</p>

        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email address"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button type="submit" className="login-btn">
            Login
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;