import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Tile Demo Cost Calculator - Dickinson's Tile LLC", page_icon="🛠️")

# Title and description
st.title("Tile Demo Cost Calculator")
st.markdown("""
Need to remove old tiles before starting fresh? The **Tile Demo Cost Calculator** helps you estimate the cost of tile demolition. 
Input the area size, tile type, and project specifics to get a clear idea of demolition expenses.
""")

# Base demolition cost
BASE_DEMOLITION_COST = 5  # $5 per square foot

# Tile type difficulty multipliers (affects demolition cost)
TILE_TYPES = {
    "Ceramic": 1.0,  # Standard difficulty
    "Porcelain": 1.1,  # Slightly harder
    "Natural Stone": 1.3,  # More difficult
    "Glass Mosaic": 1.2  # Intricate removal
}

# Project specifics with additional costs
PROJECT_SPECIFICS = {
    "Standard Removal": 0,
    "Adhesive Removal": 100,
    "Subfloor Repair": 200,
    "Hazardous Material Handling (e.g., Asbestos)": 500
}

# Input section
st.header("Enter Your Demolition Details")

# Area size
st.subheader("Area Size")
length = st.number_input("Length (feet)", min_value=1.0, max_value=100.0, value=10.0, step=0.5)
width = st.number_input("Width (feet)", min_value=1.0, max_value=100.0, value=10.0, step=0.5)

# Calculate square footage
total_area = length * width

# Tile type selection
st.subheader("Tile Type")
tile_type = st.selectbox("Select Tile Type", list(TILE_TYPES.keys()))
tile_difficulty_multiplier = TILE_TYPES[tile_type]

# Project specifics
st.subheader("Project Specifics")
project_specific = st.selectbox("Select Project Specific", list(PROJECT_SPECIFICS.keys()))
specific_additional_cost = PROJECT_SPECIFICS[project_specific]

# Calculate costs
base_demolition_cost = total_area * BASE_DEMOLITION_COST
adjusted_demolition_cost = base_demolition_cost * tile_difficulty_multiplier
specific_cost = specific_additional_cost
total_cost = adjusted_demolition_cost + specific_cost

# Display results
st.header("Cost Estimate")
if total_area > 0:
    st.write(f"**Demolition Area**: {total_area:.2f} square feet")
    st.write(f"**Base Demolition Cost** (@ $5/sqft): ${base_demolition_cost:.2f}")
    st.write(f"**Adjusted Demolition Cost** (Tile: {tile_type}, {tile_difficulty_multiplier}x multiplier): ${adjusted_demolition_cost:.2f}")
    st.write(f"**Project Specific Cost** ({project_specific}): ${specific_cost:.2f}")
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
