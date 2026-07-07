import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import UploadBox from "../components/UploadBox";
import Footer from "../components/Footer";

function Home() {
  return (
    <>
      <Navbar title="VisionMatch AI" />

      <Hero
        heading="Find Similar Products Using AI"
        description="Upload an image and discover visually similar products using Artificial Intelligence."
      />

      <UploadBox />

      <Footer />
    </>
  );
}

export default Home;