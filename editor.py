from pathlib import Path

import pandas as pd
import streamlit as st

# Load CSVs
csv_folder = Path("csv")
csv_files = list(csv_folder.glob("*.csv"))

dfs = [pd.read_csv(f).assign(_source=f.name) for f in csv_files]
df = pd.concat(dfs, ignore_index=True)

st.set_page_config(page_title="CSV Editor", layout="wide")

st.title("Claraoke CSV Collection Viewer & Editor")

# --- Search + Sorting controls (all in one row) ---
col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])

with col1:
    search_term = st.text_input("Search (case-insensitive):")

with col2:
    col_filter = st.selectbox("Filter column:", ["All"] + list(df.columns))

with col4:
    sort_col = st.selectbox("Sort by:", df.columns, index=0)

with col5:
    sort_order = st.radio("Order:", ["Asc", "Desc"], horizontal=True)

# --- Apply search filter ---
filtered_df = df.copy()
if search_term:
    if col_filter == "All":
        mask = filtered_df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
    else:
        mask = filtered_df[col_filter].astype(str).str.contains(search_term, case=False, na=False)
    filtered_df = filtered_df[mask]

# --- Apply sorting ---
# Map radio selection to True/False
ascending = True if sort_order == "Asc" else False

# Force sort_col to string (satisfies type checker + runtime safety)
sorted_df = filtered_df.sort_values(by=str(sort_col), ascending=ascending)  # pyright: ignore[reportCallIssue]


# --- Editable table ---
edited_df = st.data_editor(
    sorted_df,
    num_rows="dynamic",
    width="stretch",  # stretch to fit the page width
    height=800,  # increase vertical size (in pixels)
)


# --- Save changes back ---
if st.button("Save Changes"):
    for f in csv_files:
        # Original rows for this CSV
        original_df = df[df["_source"] == f.name].drop(columns=["_source"]).copy()
        # Edited rows for this CSV (from table)
        edited_rows = edited_df[edited_df["_source"] == f.name].drop(columns=["_source"])

        # Only update values that changed
        original_df.update(edited_rows)  # pyright: ignore[reportArgumentType]

        # Only write if data actually changed
        if not original_df.equals(df[df["_source"] == f.name].drop(columns=["_source"])):
            # Write full CSV back
            original_df.to_csv(f, index=False, lineterminator="\n")

    st.success("Changes saved!")
