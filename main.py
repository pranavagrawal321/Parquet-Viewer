import streamlit as st
import pandas as pd


def main():
    st.title("Parquet Viewer")

    # Upload Parquet file
    st.sidebar.header("Upload Parquet File")
    uploaded_file = st.sidebar.file_uploader("Upload", type=["parquet"])

    if uploaded_file is not None:
        # Read Parquet file
        try:
            df = pd.read_parquet(uploaded_file)
            st.write("### Parquet File Contents:")
            st.write(df)

            # Display summary statistics
            st.write("### Summary Statistics:")
            st.write(df.describe())

            # Optionally display specific columns
            column_selection = st.sidebar.multiselect(
                "Select Columns to Display", df.columns.tolist()
            )
            if column_selection:
                st.write("### Selected Columns:")
                st.write(df[column_selection])

        except Exception as e:
            st.error(f"Error reading file: {e}")


if __name__ == "__main__":
    main()
