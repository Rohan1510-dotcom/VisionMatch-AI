import { useState } from "react";
import ProductCard from "./ProductCard";

function UploadBox() {

    const [selectedFile, setSelectedFile] = useState(null);

    const [previewImage, setPreviewImage] = useState(null);

    const [results, setResults] = useState([]);

    const [loading, setLoading] = useState(false);

    function handleImage(event) {

        const file = event.target.files[0];

        if (!file) return;

        setSelectedFile(file);

        setPreviewImage(URL.createObjectURL(file));

        setResults([]);

    }

    async function searchProducts() {

        if (!selectedFile) {

            alert("Please select an image first.");

            return;

        }

        setLoading(true);

        const formData = new FormData();

        formData.append("file", selectedFile);

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/search",
                {
                    method: "POST",
                    body: formData,
                }
            );

            if (!response.ok) {

                throw new Error("Search request failed.");

            }

            const data = await response.json();

            setResults(data.results);

        }

        catch (error) {

            console.error(error);

            alert("Unable to search products.");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <div className="upload-container">

            <div className="upload-card">

                <h2>Upload Product Image</h2>

                <p>

                    Choose an image of a fashion product and let AI find similar
                    items from the catalogue.

                </p>

                <input

                    type="file"

                    accept="image/*"

                    onChange={handleImage}

                />

                {

                    previewImage &&

                    <div className="preview-container">

                        <img

                            src={previewImage}

                            alt="Preview"

                            className="preview-image"

                        />

                    </div>

                }

                <button

                    className="search-btn"

                    onClick={searchProducts}

                >

                    Search Similar Products

                </button>

            </div>

            {

                loading &&

                <div className="loading">

                    <h2>🔍 Searching through 44,000+ products...</h2>

                    

                </div>

            }

            {

                results.length > 0 &&

                <>

                    <h2 className="results-title">

                        Top Similar Products

                    </h2>

                    <div className="results-grid">

                        {

                            results.map((product, index) => (

                                <ProductCard

                                    key={index}

                                    product={product}

                                />

                            ))

                        }

                    </div>

                </>

            }

        </div>

    );

}

export default UploadBox;