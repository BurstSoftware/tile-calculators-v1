import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Kitchen Backsplash Cost Calculator - Dickinson's Tile LLC", page_icon="🍽️")

# Title and description
st.title("Kitchen Backsplash Cost Calculator")
st.markdown("""
Elevate your kitchen with a stunning backsplash! Our **Kitchen Backsplash Cost Calculator** lets you input details such as backsplash area, tile type, and installation complexity to estimate costs for your perfect kitchen accent.
""")

# Base installation cost
BASE_INSTALLATION_COST = 25  # $25 per square foot

# Tile type costs (per square foot)
TILE_TYPES = {
    "Ceramic": 5,
    "Porcelain": 7,
    "Glass Mosaic": 15,
    "Subway Tile": 6
}

# Installation complexity with additional costs
INSTALLATION_COMPLEXITY = {
    "Standard Installation": 0,
    "Intricate Pattern": 150,
    "Custom Cut Tiles": 200,
    "Accent Trim": 100
}

# Input section
st.header("Enter Your Backsplash Details")

# Backsplash area
st.subheader("Backsplash Area")
length = st.number_input("Length (feet)", min_value=1.0, max_value=50.0, value=10.0, step=0.5)
height = st.number_input("Height (feet)", min_value=1.0, max_value=10.0, value=1.5, step=0.1)

# Calculate square footage
total_area = length * height

# Tile type selection
st.subheader("Tile Type")
tile_type = st.selectbox("Select Tile Type", list(TILE_TYPES.keys()))
tile_cost_per_sqft = TILE_TYPES[tile_type]

# Installation complexity
st.subheader("Installation Complexity")
installation_complexity = st.selectbox("Select Installation Complexity", list(INSTALLATION_COMPLEXITY.keys()))
installation_additional_cost = INSTALLATION_COMPLEXITY[installation_complexity]

# Calculate costs
material_cost = total_area * tile_cost_per_sqft
installation_cost = total_area * BASE_INSTALLATION_COST
complexity_cost = installation_additional_cost
total_cost = material_cost + installation_cost + complexity_cost

# Display results
st.header("Cost Estimate")
if total_area > 0:
    st.write(f"**Backsplash Area**: {total_area:.2f} square feet")
    st.write(f"**Material Cost** (Tile: {tile_type}): ${material_cost:.2f}")
    st.write(f"**Installation Cost** (@ $25/sqft): ${installation_cost:.2f}")
    st.write(f"**Installation Complexity Cost** ({installation_complexity}): ${complexity_cost:.2f}")
    st.write(f"### Total Estimated Cost: ${total_cost:.2f}")
else:
    st.warning("Please enter valid dimensions to calculate costs.")

# Note
st.markdown("*Note: This is an approximate estimate. Final costs may vary based on project specifics and consultation with Dickinson's Tile LLC.*")

# Contact information
st.markdown("""
For a detailed quote or to discuss your project, [contact Dickinson's Tile LLC](https://dickinsonstile.com/contact/) today!
""")

# Footer
st.markdown("---")
st.write("© 2025 Dickinson's Tile LLC. All rights reserved.")
