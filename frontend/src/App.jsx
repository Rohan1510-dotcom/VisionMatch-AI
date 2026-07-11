import "./App.css";

import Navbar from "./components/Navbar";
import UploadBox from "./components/UploadBox";
import Footer from "./components/Footer";

function App() {
  return (
    <div className="app">

      <Navbar />

      <main className="hero">

        <div className="hero-content">

          <h1>VisionMatch AI</h1>

          <p>
            Upload a fashion product image and instantly discover visually
            similar products using AI-powered image search.
          </p>

          <UploadBox />

        </div>

      </main>

      <Footer />

    </div>
  );
}

export default App;