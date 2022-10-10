import './App.css';
import './style.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">

        <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Rubik:400,700'/>

            <body>
        <div className="login-form">
          <form action="" method="POST">
            <h1>Login</h1>
            <div className="content">
              <div className="input-field">
                <input type="email" placeholder="Email" autocomplete="nope"/>
              </div>
              <div className="input-field">
                <input type="password" placeholder="Password" autocomplete="new-password"/>
              </div>
              <a href="#" className="link">Forgot Your Password?</a>
            </div>
            <div className="action">
              <button>Register</button>
              <button type="submit">Sign in</button>
            </div>
          </form>
        </div>

        </body>


      </header>
    </div>
  );
}

export default App;
