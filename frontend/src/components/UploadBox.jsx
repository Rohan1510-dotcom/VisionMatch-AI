import { useState } from "react";

function UploadBox() {

    const [selectedFile, setSelectedFile] = useState(null);
    const [selectedImage, setSelectedImage] = useState(null);
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);

    function handleImage(event) {

        const file = event.target.files[0];

        if (file) {

            setSelectedFile(file);
            setSelectedImage(URL.createObjectURL(file));
            setResults([]);

        }

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

            const data = await response.json();

            setResults(data.results);

        }

        catch (error) {

            console.error(error);

            alert("Search Failed!");

        }

        setLoading(false);

    }

    return (

        <div className="upload-box">

            <h3>📷 Drag & Drop Image Here</h3>

            <p>or choose an image from your computer</p>

            <input
                type="file"
                accept="image/*"
                onChange={handleImage}
            />

            {

                selectedImage &&

                <img
                    src={selectedImage}
                    alt="Preview"
                    className="preview-image"
                />

            }

            <br />

            <button
                onClick={searchProducts}
            >

                Search Similar Products

            </button>

            {

                loading &&

                <h3>Searching...</h3>

            }

            {

                results.length > 0 &&

                <div className="results">

                    <h2>Similar Products</h2>

                    {

                        results.map((product, index) => (

                            <div
                                key={index}
                                className="product-card"
                            >

                                <h3>{product.product_name}</h3>

                                <p>
                                    <b>Gender:</b> {product.gender}
                                </p>

                                <p>
                                    <b>Category:</b> {product.master_category}
                                </p>

                                <p>
                                    <b>Type:</b> {product.article_type}
                                </p>

                                <p>
                                    <b>Color:</b> {product.color}
                                </p>

                                <p>
                                    <b>Season:</b> {product.season}
                                </p>

                                <p>
                                    <b>Usage:</b> {product.usage}
                                </p>

                                <p>
                                    <b>Similarity:</b> {product.similarity}%
                                </p>

                            </div>

                        ))

                    }

                </div>

            }

        </div>

    );

}

export default UploadBox;