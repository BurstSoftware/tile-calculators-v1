import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Tile Flooring Cost Calculator - Dickinson's Tile LLC", page_icon="🪚")

# Title and description
st.title("Tile Flooring Cost Calculator")
st.markdown("""
Ready to transform your floors? Use our **Tile Flooring Cost Calculator** to estimate the cost of your flooring project. 
Input room dimensions, tile material, and installation preferences to get an accurate estimate for your space.
""")

# Base installation cost
BASE_INSTALLATION_COST = 25  # $25 per square foot

# Tile material costs (per square foot)
TILE_MATERIALS = {
    "Ceramic": 5,
    "Porcelain": 7,
    "Natural Stone": 12,
    "Luxury Vinyl Tile": 4
}

# Installation preferences with additional costs
INSTALLATION_PREFERENCES = {
    "Standard Installation": 0,
    "Diagonal Pattern": 100,
    "Herringbone Pattern": 200,
    "Underfloor Heating": 500
}

# Input section
st.header("Enter Your Flooring Details")

# Room dimensions
st.subheader("Room Size")
length = st.number_input("Length (feet)", min_value=1.0, max_value=100.0, value=12.0, step=0.5)
width = st.number_input("Width (feet)", min_value=1.0, max_value=100.0, value=10.0, step=0.5)

# Calculate square footage
total_area = length * width

# Tile material selection
st.subheader("Tile Material")
tile_material = st.selectbox("Select Tile Material", list(TILE_MATERIALS.keys()))
tile_cost_per_sqft = TILE_MATERIALS[tile_material]

# Installation preferences
st.subheader("Installation Preferences")
installation_preference = st.selectbox("Select Installation Type", list(INSTALLATION_PREFERENCES.keys()))
installation_additional_cost = INSTALLATION_PREFERENCES |installation_preference]

# Calculate costs
material_cost = total_area * tile_cost_per_sqft
installation_cost = total_area * BASE_INSTALLATION_COST
preference_cost = installation_additional_cost
total_cost = material_cost + installation_cost + preference_cost

# Display results
st.header("Cost Estimate")
st.write(f"**Floor Area**: {total_area:.2f} square feet")
st.write(f"**Material Cost** (Tile: {tile_material}): ${material_cost:.2f}")
st.write(f"**Installation Cost** (@ $25/sqft): ${installation_cost:.2f}")
st.write(f"**Installation Preference Cost** ({installation_preference}): ${preference_cost:.2f}")
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
