import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS STYLING
# --------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}

.hero {
    padding: 30px;
    background: linear-gradient(90deg, #4F46E5, #7C3AED);
    color: white;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 25px;
}

.product-card {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    min-height: 260px;
}

.product-name {
    font-size: 20px;
    font-weight: bold;
    color: #222;
}

.product-price {
    color: #16A34A;
    font-size: 22px;
    font-weight: bold;
    margin-top: 10px;
}

.category-tag {
    background-color: #EEF2FF;
    color: #4F46E5;
    padding: 5px 10px;
    border-radius: 20px;
    display: inline-block;
    margin-top: 8px;
    font-size: 12px;
}

.featured {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SAMPLE PRODUCT DATA
# --------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "description": "Premium noise-cancelling headphones with 30-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 4999,
        "description": "Track fitness, heart rate, and notifications on the go.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 2499,
        "description": "Comfortable and lightweight shoes for daily workouts.",
        "category": "Fashion"
    },
    {
        "name": "Backpack",
        "price": 1499,
        "description": "Durable travel backpack with multiple storage compartments.",
        "category": "Accessories"
    },
    {
        "name": "Coffee Maker",
        "price": 3499,
        "description": "Automatic coffee machine for fresh coffee every morning.",
        "category": "Home"
    },
    {
        "name": "Gaming Mouse",
        "price": 1999,
        "description": "High-precision RGB gaming mouse with programmable buttons.",
        "category": "Electronics"
    }
]

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

# Shopping Cart Summary (Demo)
st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart")

cart_items = 3
cart_total = 7497

st.sidebar.write(f"Items: **{cart_items}**")
st.sidebar.write(f"Total: **₹{cart_total:,}**")

st.sidebar.button("Proceed to Checkout")

# --------------------------------------------------
# HOMEPAGE
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ Welcome to MiniStore</h1>
    <h3>Your One-Stop Shop for Everyday Essentials</h3>
    <p>Discover quality products at unbeatable prices.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# WELCOME SECTION
# --------------------------------------------------
st.title("MiniStore Online Shopping")

st.write("""
Welcome to MiniStore, your trusted destination for electronics,
fashion, home essentials, and accessories. Browse our featured
products and enjoy a seamless shopping experience.
""")

# --------------------------------------------------
# FILTER PRODUCTS
# --------------------------------------------------
if selected_category != "All":
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]
else:
    filtered_products = products

# --------------------------------------------------
# FEATURED PRODUCTS SECTION
# --------------------------------------------------
st.markdown(
    '<div class="featured">⭐ Featured Products</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# PRODUCT GRID USING COLUMNS
# --------------------------------------------------
cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:

        st.markdown(
            f"""
            <div class="product-card">
                <div class="product-name">
                    {product['name']}
                </div>

                <div class="category-tag">
                    {product['category']}
                </div>

                <p style="margin-top:12px;">
                    {product['description']}
                </p>

                <div class="product-price">
                    ₹{product['price']:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Demo Add to Cart Button
        st.button(
            f"Add to Cart",
            key=product["name"]
        )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")

st.markdown("""
<center>
<p>© 2026 MiniStore | Built with Streamlit</p>
</center>
""", unsafe_allow_html=True)