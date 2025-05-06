import requests
import json
from googlesearch import search
from github import Github

# Config - Replace with your keys
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
REPO_NAME = "YOUR_GITHUB_USERNAME/NovaLink"
PRODUCTS_FILE = "products.json"

# Google search for trending products
def find_trending_products():
    query = "top dropshipping products 2025"
    results = []
    for url in search(query, num_results=5):
        results.append(url)
    return results

# Update GitHub repo with new product data
def update_catalog(products):
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    with open(PRODUCTS_FILE, "r") as f:
        current_products = json.load(f)
    current_products.extend(products[:1])  # Add one new product
    repo.update_file(
        PRODUCTS_FILE,
        "Update product catalog",
        json.dumps(current_products, indent=2),
        repo.get_contents(PRODUCTS_FILE).sha
    )

# Generate promotional post
def create_promo_post(product):
    return f"🔥 Hot Deal! Get your {product['name']} for only ${product['price']}! Shop now: https://github.com/{REPO_NAME} #Dropshipping #Deals #NovaLink"

# Main execution
if __name__ == "__main__":
    print("Agent running...")
    trending_urls = find_trending_products()
    print("Found trends:", trending_urls)
    # Simulate new product (replace with real parsing if needed)
    new_products = [
        {
            "id": 6,
            "name": "Trendy Item",
            "price": 11.99,
            "cost": 3.00,
            "aliexpress_link": "https://www.aliexpress.com/store/dropshipping",
            "image": "trend.jpg"
        }
    ]
    update_catalog(new_products)
    with open(PRODUCTS_FILE, "r") as f:
        products = json.load(f)
    for product in products:
        post = create_promo_post(product)
        print("Post to X/Reddit:", post)
