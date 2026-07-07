import { useState } from "react";
import { uploadImage } from "../services/api";

function UploadBox() {
  // State variables
  const [selectedImage, setSelectedImage] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);
  const [selectedFileName, setSelectedFileName] = useState("");
  const [selectedFileSize, setSelectedFileSize] = useState("");

  // Process selected file
  function processFile(file) {
    if (!file) return;

    const imageUrl = URL.createObjectURL(file);

    setSelectedImage(imageUrl);
    setSelectedFile(file);
    setSelectedFileName(file.name);
    setSelectedFileSize((file.size / 1024).toFixed(2));
  }

  // File picker
  function handleImage(event) {
    processFile(event.target.files[0]);
  }

  // Drag over
  function handleDragOver(event) {
    event.preventDefault();
  }

  // Drop image
  function handleDrop(event) {
    event.preventDefault();

    processFile(event.dataTransfer.files[0]);
  }

  // Remove image
  function removeImage() {
    setSelectedImage(null);
    setSelectedFile(null);
    setSelectedFileName("");
    setSelectedFileSize("");
  }

  // Upload image to FastAPI
  async function handleSearch() {
    if (!selectedFile) {
      alert("Please select an image first.");
      return;
    }

    try {
      const result = await uploadImage(selectedFile);

      console.log(result);

      alert(result.message);
    } catch (error) {
      console.error(error);

      alert("Upload failed!");
    }
  }

  return (
    <div className="upload-box">
      {/* Upload Area */}
      <div
        className="upload-area"
        onDragOver={handleDragOver}
        onDrop={handleDrop}
      >
        <h2>📷</h2>

        <h3>Drag & Drop Image Here</h3>

        <p>or click below to choose an image</p>

        <input
          type="file"
          accept="image/*"
          onChange={handleImage}
        />

        <small>Supported Formats: JPG • PNG • JPEG</small>
      </div>

      {/* Preview Card */}
      {selectedImage && (
        <div className="preview-card">
          <h3>🖼 Image Preview</h3>

          <img
            src={selectedImage}
            alt="Preview"
            className="preview-image"
          />

          <p className="file-name">
            📄 {selectedFileName}
          </p>

          <p className="file-size">
            📦 {selectedFileSize} KB
          </p>

          <div className="button-group">
            <button
              className="remove-btn"
              onClick={removeImage}
            >
              Remove
            </button>

            <button onClick={handleSearch}>
              Search Similar Products
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default UploadBox;