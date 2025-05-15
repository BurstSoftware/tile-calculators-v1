import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Room Tile Cost Calculator - Dickinson's Tile LLC", page_icon="🏠")

# Title and description
st.title("Room Tile Cost Calculator")
st.markdown("""
Revamp any room with new tile flooring! The **Room Tile Cost Calculator** allows you to estimate costs for tiling any space, from living rooms to offices. 
Provide room dimensions, tile preferences, and additional options to see your project’s potential cost.
""")

# Base installation cost
BASE_INSTALLATION_COST = 25  # $25 per square foot

# Tile material costs (per square foot)
TILE_MATERIALS = {
    "Ceramic": 5,
    "Porcelain": 7,
    "Natural Stone": 12,
    "Wood-Look Tile": 8
}

# Additional options with costs
ADDITIONAL_OPTIONS = {
    "Standard Installation": 0,
    "Diagonal Pattern": 150,
    "Border Trim": 200,
    "Underfloor Heating": 600
}

# Input section
st.header("Enter Your Room Tiling Details")

# Room dimensions
st.subheader("Room Dimensions")
length = st.number_input("Length (feet)", min_value=1.0, max_value=100.0, value=15.0, step=0.5)
width = st.number_input("Width (feet)", min_value=1.0, max_value=100.0, value=12.0, step=0.5)

# Calculate square footage
total_area = length * width

# Tile material selection
st.subheader("Tile Preferences")
tile_material = st.selectbox("Select Tile Material", list(TILE_MATERIALS.keys()))
tile_cost_per_sqft = TILE_MATERIALS[tile_material]

# Additional options
st.subheader("Additional Options")
additional_option = st.selectbox("Select Additional Option", list(ADDITIONAL_OPTIONS.keys()))
option_additional_cost = ADDITIONAL_OPTIONS[additional_option]

# Calculate costs
material_cost = total_area * tile_cost_per_sqft
installation_cost = total_area * BASE_INSTALLATION_COST
option_cost = option_additional_cost
total_cost = material_cost + installation_cost + option_cost

# Display results
st.header("Cost Estimate")
if total_area > 0:
    st.write(f"**Room Area**: {total_area:.2f} square feet")
    st.write(f"**Material Cost** (Tile: {tile_material}): ${material_cost:.2f}")
    st.write(f"**Installation Cost** (@ $25/sqft): ${installation_cost:.2f}")
    st.write(f"**Additional Option Cost** ({additional_option}): ${option_cost:.2f}")
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
