from app.ai.search_service import search_similar

results = search_similar(
    "dataset/images/1163.jpg"
)

print("=" * 60)
print("SIMILAR PRODUCTS")
print("=" * 60)

for product in results:

    print()

    print("Product Name :", product["product_name"])
    print("Gender       :", product["gender"])
    print("Category     :", product["master_category"])
    print("Type         :", product["article_type"])
    print("Color        :", product["color"])
    print("Similarity   :", f"{product['similarity']}%")