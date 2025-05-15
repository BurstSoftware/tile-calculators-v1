import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Custom Shower Cost Calculator - Dickinson's Tile LLC", page_icon="🛁")

# Title and description
st.title("Custom Shower Cost Calculator")
st.markdown("""
Want a unique, luxurious shower? The **Custom Shower Cost Calculator** lets you customize every detail, from premium tiles to advanced features like built-in benches or niches. Enter your preferences to see how your vision fits your budget.
""")

# Base installation cost
BASE_INSTALLATION_COST = 25  # $25 per square foot

# Premium tile type costs (per square foot)
PREMIUM_TILE_TYPES = {
    "Handcrafted Glass Mosaic": 25,
    "Marble": 20,
    "Porcelain Slab": 15,
    "Designer Ceramic": 10
}

# Advanced features with costs
ADVANCED_FEATURES = {
    "Built-in Bench (Custom)": 500,
    "Shower Niche (Large)": 250,
    "Frameless Glass Enclosure": 1200,
    "Luxury Rain Showerhead": 600,
    "Heated Floor System": 800,
    "Custom Accent Wall": 400
}

# Input section
st.header("Enter Your Custom Shower Details")

# Shower dimensions
st.subheader("Shower Size")
length = st.number_input("Length (feet)", min_value=1.0, max_value=20.0, value=6.0, step=0.5)
width = st.number_input("Width (feet)", min_value=1.0, max_value=20.0, value=4.0, step=0.5)
height = st.number_input("Height (feet)", min_value=1.0, max_value=12.0, value=8.0, step=0.5)

# Calculate square footage (floor + walls)
floor_area = length * width
wall_area = 2 * (length * height + width * height)  # Two longer walls + two shorter walls
total_area = floor_area + wall_area

# Tile type selection
st.subheader("Premium Tile Type")
tile_type = st.selectbox("Select Tile Type", list(PREMIUM_TILE_TYPES.keys()))
tile_cost_per_sqft = PREMIUM_TILE_TYPES[tile_type]

# Advanced features
st.subheader("Advanced Features")
selected_features = []
for feature, cost in ADVANCED_FEATURES.items():
    if st.checkbox(feature, key=feature):
        selected_features.append((feature, cost))

# Calculate costs
material_cost = total_area * tile_cost_per_sqft
installation_cost = total_area * BASE_INSTALLATION_COST
feature_cost = sum(cost for _, cost in selected_features)
total_cost = material_cost + installation_cost + feature_cost

# Display results
st.header("Cost Estimate")
st.write(f"**Shower Area**: {total_area:.2f} square feet")
st.write(f"**Material Cost** (Tile: {tile_type}): ${material_cost:.2f}")
st.write(f"**Installation Cost** (@ $25/sqft): ${installation_cost:.2f}")
st.write(f"**Advanced Features Cost**: ${feature_cost:.2f}")
st.write(f"### Total Estimated Cost: ${total_cost:.2f}")

# Note
st.markdown("*Note: This is an approximate estimate. Final costs may vary based on project specifics and consultation with Dickinson's Tile LLC.*")

# Contact information
st.markdown("""
For a detailed quote or to discuss your project, [contact Dickinson's Tile LLC](https://dickinsonstile.com/contact/) today!
""")

# Footer
st.markdown("---")
st.write("© 2025 Dickinson's Tile LLC. All rights reserved.")
