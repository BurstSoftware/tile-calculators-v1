import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Walkway Tile Cost Calculator - Dickinson's Tile LLC", page_icon="🌳")

# Title and description
st.title("Walkway Tile Cost Calculator")
st.markdown("""
Enhance your outdoor space with a durable and stylish tiled walkway! The **Walkway Tile Cost Calculator** lets you input key details like walkway dimensions, tile material, and installation preferences to generate an accurate cost estimate for your project.
""")

# Base installation cost
BASE_INSTALLATION_COST = 25  # $25 per square foot

# Tile material costs (per square foot)
TILE_MATERIALS = {
    "Porcelain Paver": 8,
    "Natural Stone": 12,
    "Concrete Paver": 5,
    "Ceramic": 6
}

# Installation preferences with additional costs
INSTALLATION_PREFERENCES = {
    "Standard Installation": 0,
    "Patterned Layout": 200,
    "Gravel Base Preparation": 150,
    "Sealed Finish": 100
}

# Input section
st.header("Enter Your Walkway Details")

# Walkway dimensions
st.subheader("Walkway Dimensions")
length = st.number_input("Length (feet)", min_value=1.0, max_value=200.0, value=20.0, step=0.5)
width = st.number_input("Width (feet)", min_value=1.0, max_value=20.0, value=4.0, step=0.5)

# Calculate square footage
total_area = length * width

# Tile material selection
st.subheader("Tile Material")
tile_material = st.selectbox("Select Tile Material", list(TILE_MATERIALS.keys()))
tile_cost_per_sqft = TILE_MATERIALS[tile_material]

# Installation preferences
st.subheader("Installation Preferences")
installation_preference = st.selectbox("Select Installation Preference", list(INSTALLATION_PREFERENCES.keys()))
installation_additional_cost = INSTALLATION_PREFERENCES[installation_preference]

# Calculate costs
material_cost = total_area * tile_cost_per_sqft
installation_cost = total_area * BASE_INSTALLATION_COST
preference_cost = installation_additional_cost
total_cost = material_cost + installation_cost + preference_cost

# Display results
st.header("Cost Estimate")
if total_area > 0:
    st.write(f"**Walkway Area**: {total_area:.2f} square feet")
    st.write(f"**Material Cost** (Tile: {tile_material}): ${material_cost:.2f}")
    st.write(f"**Installation Cost** (@ $25/sqft): ${installation_cost:.2f}")
    st.write(f"**Installation Preference Cost** ({installation_preference}): ${preference_cost:.2f}")
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
