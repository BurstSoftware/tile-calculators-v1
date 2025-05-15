import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Shower Cost Calculator - Dickinson's Tile LLC", page_icon="🛁")

# Title and description
st.title("Shower Cost Calculator")
st.markdown("""
Dreaming of a new shower? Our **Shower Cost Calculator** helps you estimate the cost of a standard shower installation. 
Input details like shower size, tile type, and additional features to get a clear picture of your project budget.
""")

# Base installation cost
BASE_INSTALLATION_COST = 25  # $25 per square foot

# Tile type costs (per square foot)
TILE_TYPES = {
    "Ceramic": 5,
    "Porcelain": 7,
    "Glass": 15,
    "Natural Stone": 12
}

# Additional features with costs
ADDITIONAL_FEATURES = {
    "Shower Bench": 300,
    "Niche/Recess": 150,
    "Glass Door": 800,
    "Upgraded Fixtures": 400
}

# Input section
st.header("Enter Your Shower Details")

# Shower dimensions
st.subheader("Shower Size")
length = st.number_input("Length (feet)", min_value=1.0, max_value=20.0, value=5.0, step=0.5)
width = st.number_input("Width (feet)", min_value=1.0, max_value=20.0, value=3.0, step=0.5)
height = st.number_input("Height (feet)", min_value=1.0, max_value=10.0, value=7.0, step=0.5)

# Calculate square footage (floor + walls)
floor_area = length * width
wall_area = 2 * (length * height + width * height)  # Two longer walls + two shorter walls
total_area = floor_area + wall_area

# Tile type selection
st.subheader("Tile Type")
tile_type = st.selectbox("Select Tile Type", list(TILE_TYPES.keys()))
tile_cost_per_sqft = TILE_TYPES[tile_type]

# Additional features
st.subheader("Additional Features")
selected_features = []
for feature, cost in ADDITIONAL_FEATURES.items():
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
st.write(f"**Additional Features Cost**: ${feature_cost:.2f}")
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
