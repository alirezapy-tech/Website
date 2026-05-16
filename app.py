import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px

st.set_page_config(
    page_title="AI Luxury Shop",
    page_icon="🛍️",
    layout="wide"
)

# =========================
# Fake Database
# =========================

products = [
    {
        "name": "MacBook Pro M4",
        "price": 2999,
        "category": "Laptop",
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1517336714739-489689fd1ca8"
    },
    {
        "name": "iPhone 16 Pro",
        "price": 1599,
        "category": "Phone",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
    },
    {
        "name": "Gaming RTX Laptop",
        "price": 2499,
        "category": "Gaming",
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853"
    },
    {
        "name": "Luxury Smart Watch",
        "price": 899,
        "category": "Watch",
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    },
]

# =========================
# Session State
# =========================

if "cart" not in st.session_state:
    st.session_state.cart = []

# =========================
# Custom CSS
# =========================

st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }

    .product-card {
        background: #111827;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
        transition: 0.3s;
    }

    .product-card:hover {
        transform: scale(1.03);
    }

    .price {
        color: #22c55e;
        font-size: 24px;
        font-weight: bold;
    }

    .hero {
        padding: 50px;
        border-radius: 25px;
        background: linear-gradient(135deg,#1e3a8a,#7c3aed);
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# Sidebar Menu
# =========================

with st.sidebar:
    selected = option_menu(
        menu_title="AI Luxury Shop",
        options=["Home", "Products", "Cart", "Dashboard", "AI Assistant"],
        icons=["house", "shop", "cart", "graph-up", "robot"],
        default_index=0,
    )

# =========================
# HERO SECTION
# =========================

if selected == "Home":

    st.markdown(
        """
        <div class='hero'>
            <h1>🛍️ AI Luxury Store</h1>
            <h3>Future of Shopping with Streamlit</h3>
            <p>Modern UI • AI Assistant • Smart Dashboard • Premium Products</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.image(
        "https://images.unsplash.com/photo-1556740749-887f6717d7e4",
        use_container_width=True
    )

    st.subheader("🔥 Featured Products")

    cols = st.columns(4)

    for idx, product in enumerate(products):
        with cols[idx % 4]:
            st.image(product["image"])
            st.markdown(f"### {product['name']}")
            st.markdown(f"<div class='price'>$ {product['price']}</div>", unsafe_allow_html=True)
            st.write(f"⭐ {product['rating']}")

# =========================
# PRODUCTS PAGE
# =========================

elif selected == "Products":

    st.title("🛒 Products")

    search = st.text_input("🔍 Search Product")

    categories = ["All"] + list(set([p["category"] for p in products]))

    selected_category = st.selectbox("Category", categories)

    price_range = st.slider("Price Range", 0, 5000, (0, 5000))

    filtered_products = []

    for product in products:
        if search.lower() in product["name"].lower():
            if selected_category == "All" or product["category"] == selected_category:
                if price_range[0] <= product["price"] <= price_range[1]:
                    filtered_products.append(product)

    cols = st.columns(2)

    for idx, product in enumerate(filtered_products):

        with cols[idx % 2]:
            st.markdown("<div class='product-card'>", unsafe_allow_html=True)
            st.image(product["image"])
            st.subheader(product["name"])
            st.write(f"Category: {product['category']}")
            st.write(f"⭐ Rating: {product['rating']}")
            st.markdown(f"<div class='price'>$ {product['price']}</div>", unsafe_allow_html=True)

            if st.button(f"Add To Cart - {product['name']}"):
                st.session_state.cart.append(product)
                st.success("Added to cart")

            st.markdown("</div>", unsafe_allow_html=True)

# =========================
# CART PAGE
# =========================

elif selected == "Cart":

    st.title("🛒 Shopping Cart")

    total = 0

    if len(st.session_state.cart) == 0:
        st.warning("Cart is empty")

    for item in st.session_state.cart:
        col1, col2 = st.columns([1,3])

        with col1:
            st.image(item["image"], width=150)

        with col2:
            st.subheader(item["name"])
            st.write(f"$ {item['price']}")
            total += item["price"]

    st.divider()

    st.markdown(f"# 💰 Total: $ {total}")

    if st.button("✅ Checkout"):
        st.success("Payment Successful 🎉")
        st.balloons()

# =========================
# DASHBOARD PAGE
# =========================

elif selected == "Dashboard":

    st.title("📊 Admin Dashboard")

    sales_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales": [12000, 18000, 15000, 22000, 28000, 35000]
    })

    fig = px.line(
        sales_data,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Sales"
    )

    st.plotly_chart(fig, use_container_width=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Revenue", "$120K", "+12%")

    with col2:
        st.metric("Orders", "2,430", "+8%")

    with col3:
        st.metric("Customers", "1,240", "+20%")

# =========================
# AI ASSISTANT
# =========================

elif selected == "AI Assistant":

    st.title("🤖 AI Shopping Assistant")

    user_input = st.text_input("Ask AI")

    if user_input:

        if "laptop" in user_input.lower():
            st.success("MacBook Pro M4 is the best choice for AI and programming.")

        elif "gaming" in user_input.lower():
            st.success("RTX Gaming Laptop is perfect for gaming and rendering.")

        elif "cheap" in user_input.lower():
            st.success("Luxury Smart Watch is currently the most affordable product.")

        else:
            st.info("AI recommends checking featured products for premium experience.")
