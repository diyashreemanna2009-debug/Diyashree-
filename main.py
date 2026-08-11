import streamlit as st

st.title("Interactive Streamlit App")

#Taking user input
name=st.text_input("Enter your name:")

#Displaying a message when a button is clicked
if st.button ("Submit"):
    st.write(f"Hello,{name}: Welcome to Streamlit,")
      

import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
# CRITICAL: st.set_page_config must be the absolute first Streamlit command called.
st.set_page_config(
    page_title="Interactive Data Dashboard",
    page_icon=" ",
    layout="wide"
)

# 2. Mock Data Generation Function
@st.cache_data
def load_data():
    dates = pd.date_range(start="2026-01-01", periods=100)
    data = pd.DataFrame({
        "Date": dates,
        "Sales": np.random.randint(200, 1000, size=100),
        "Users": np.random.randint(50, 500, size=100),
        "Region": np.random.choice(["North", "South", "East", "West"], size=100)
    })
    return data

df = load_data()

# 3. Sidebar Navigation & Interactive Controls
st.sidebar.title("Configuration Panel")
st.sidebar.markdown("Use the widgets below to filter the dashboard content dynamically.")

# Widget 1: Text Input
user_name = st.sidebar.text_input("Enter your name:", placeholder="Guest User")

# Widget 2: Select Box
metric_choice = st.sidebar.selectbox("Select Visual Metric:", ["Sales", "Users"])

# Widget 3: Multi-Select Box
selected_regions = st.sidebar.multiselect(
    "Filter by Region:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

# Widget 4: Slider
# FIXED: Corrected parameter names (min_value, max_value) and fixed variable name references.
min_val = int(df[metric_choice].min())
max_val = int(df[metric_choice].max())
value_range = st.sidebar.slider(
    f"Filter {metric_choice} Range:",
    min_value=min_val,
    max_value=max_val,
    value=(min_val, max_val)
)

# 4. Data Filtering Logic
filtered_df = df[
    (df["Region"].isin(selected_regions)) &
    (df[metric_choice] >= value_range[0]) &
    (df[metric_choice] <= value_range[1])
]

# 5. Main Content Area Layout
greeting = f"Hello, {user_name}! Welcome to Streamlit." if user_name else "Interactive Streamlit App"
st.title(greeting)
st.markdown("This web app updates automatically in real-time as you modify the sidebar parameters.")

# Integrated your initial submit button workflow smoothly here
st.subheader("Quick Welcome Form")
name = st.text_input("Enter a name for a custom greeting:")
if st.button("Submit"):
    st.write(f"Hello, {name}: Welcome to Streamlit!")

st.markdown("---")

# Layout Columns for Metrics
col1, col2, col3 = st.columns(3)

if not filtered_df.empty:
    with col1:
        st.metric(label=f"Total {metric_choice}", value=f"{filtered_df[metric_choice].sum():,}")
    with col2:
        st.metric(label=f"Average {metric_choice}", value=f"{int(filtered_df[metric_choice].mean()):,}")
    with col3:
        st.metric(label="Data Points Found", value=len(filtered_df))
else:
    st.warning("No data matches current filter criteria.")

st.markdown("---")

# Chart and Data Table Display
if not filtered_df.empty:
    st.subheader(f"Historical Trend: {metric_choice}")
    chart_data = filtered_df.set_index("Date")[[metric_choice]]
    st.line_chart(chart_data)
    
    # Interactive Toggle Element
    if st.checkbox("Show Raw Data Table"):
        st.subheader("Filtered Dataset View")
        st.dataframe(filtered_df, use_container_width=True)

# Interactive Action Button
if st.button("Celebrate Data Insights!"):
    st.balloons()
