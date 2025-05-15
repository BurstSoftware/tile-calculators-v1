import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Bathroom Tile Cost Calculator - Dickinson's Tile LLC", page_icon="🛁")

# Title and description
st.title("Bathroom Tile Cost Calculator")
st.markdown("""
Transform your bathroom with beautiful tiles! The **Bathroom Tile Cost Calculator** helps you estimate the cost of tiling your bathroom walls, floors, or both. 
Enter details like bathroom dimensions, tile material, and design preferences to get a clear budget overview.
""")

# Base installation cost
BASE_INSTALLATION_COST = 25  # $25 per square foot

# Tile material costs (per square foot)
TILE_MATERIALS = {
    "Ceramic": 5,
    "Porcelain": 7,
    "Glass Mosaic": 15,
    "Natural Stone": 12
}

# Design preferences with additional costs
DESIGN_PREFERENCES = {
    "Standard Layout": 0,
    "Diagonal Pattern": 150,
    "Accent Border": 200,
    "Custom Mosaic Feature": 300
}

# Input section
st.header("Enter Your Bathroom Tiling Details")

# Tiling area selection
st.subheader("Tiling Area")
tiling_area = st.multiselect(
    "Select Areas to Tile",
    ["Floors", "Walls"],
    default=["Floors"]
)

# Bathroom dimensions
st.subheader("Bathroom Dimensions")
length = st.number_input("Length (feet)", min_value=1.0, max_value=50.0, value=8.0, step=0.5)
width = st.number_input("Width (feet)", min_value=1.0, max_value=50.0, value=6.0, step=0.5)
height = st.number_input("Wall Height (feet)", min_value=1.0, max_value=12.0, value=8.0, step=0.5)

# Calculate square footage
floor_area = length * width if "Floors" in tiling_area else 0
wall_area = 2 * (length * height + width * height) if "Walls" in tiling_area else 0  # Four walls
total_area = floor_area + wall_area

# Tile material selection
st.subheader("Tile Material")
tile_material = st.selectbox("Select Tile Material", list(TILE_MATERIALS.keys()))
tile_cost_per_sqft = TILE_MATERIALS[tile_material]

# Design preferences
st.subheader("Design Preferences")
design_preference = st.selectbox("Select Design Preference", list(DESIGN_PREFERENCES.keys()))
design_additional_cost = DESIGN_PREFERENCES[design_preference]

# Calculate costs
material_cost = total_area * tile_cost_per_sqft
installation_cost = total_area * BASE_INSTALLATION_COST
preference_cost = design_additional_cost
total_cost = material_cost + installation_cost + preference_cost

# Display results
st.header("Cost Estimate")
if total_area > 0:
    st.write(f"**Total Tiling Area**: {total_area:.2f} square feet")
    st.write(f"- Floors: {floor_area:.2f} sq ft" if "Floors" in tiling_area else "- Floors: Not selected")
    st.write(f"- Walls: {wall_area:.2f} sq ft" if "Walls" in tiling_area else "- Walls: Not selected")
    st.write(f"**Material Cost** (Tile: {tile_material}): ${material_cost:.2f}")
    st.write(f"**Installation Cost** (@ $25/sqft): ${installation_cost:.2f}")
    st.write(f"**Design Preference Cost** ({design_preference}): ${preference_cost:.2f}")
    st.write(f"### Total Estimated Cost: ${total_cost:.2f}")
else:
    st.warning("Please select at least one tiling area (Floors or Walls) to calculate costs.")

# Note
st.markdown("*Note: This is an approximate estimate. Final costs may vary based on project specifics and consultation with Dickinson's Tile LLC.*")

# Contact information
st.markdown("""
For a detailed quote or to discuss your project, [contact Dickinson's Tile LLC](https://dickinsonstile.com/contact/) today!
""")

# Footer
st.markdown("---")
st.write("© 2025 Dickinson's Tile LLC. All rights reserved.")
