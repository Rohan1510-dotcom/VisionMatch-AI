function ProductCard({ product }) {

    return (

        <div className="product-card">

            <img

                src={product.image_url}

                alt={product.product_name}

                className="product-image"

            />

            <div className="product-content">

                <h3>{product.product_name}</h3>

                <span className="similarity-badge">

                    ⭐ {product.similarity}% Match

                </span>

                <div className="product-details">

                    <p>

                        <strong>Gender:</strong> {product.gender}

                    </p>

                    <p>

                        <strong>Category:</strong> {product.master_category}

                    </p>

                    <p>

                        <strong>Sub Category:</strong> {product.sub_category}

                    </p>

                    <p>

                        <strong>Article Type:</strong> {product.article_type}

                    </p>

                    <p>

                        <strong>Color:</strong> {product.color}

                    </p>

                    <p>

                        <strong>Season:</strong> {product.season}

                    </p>

                    <p>

                        <strong>Usage:</strong> {product.usage}

                    </p>

                </div>

            </div>

        </div>

    );

}

export default ProductCard;