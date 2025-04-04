import streamlit as st
import pandas as pd
from io import BytesIO
import time

# Set page configuration
st.set_page_config(
    page_title="CSV Column Cleaner",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom styling with black and green color palette
st.markdown("""
<style>
    /* Primary theme color (green) */
    .stApp {
        background-color: black;
    }
    .stButton button {
        background-color: #80c241;
        color: black;
        border: none;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        transition: all 0.3s;
    }
    .stButton button:hover {
        background-color: #68a234;
        color: black;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .stTitle, .stHeader {
        color: #80c241 !important;
    }
    /* Text colors */
    p, span, div, label, .stMarkdown {
        color: white !important;
    }
    h1, h2, h3 {
        color: #80c241 !important;
    }
    /* File uploader */
    .stFileUploader {
        border-color: #80c241 !important;
        border-radius: 5px;
        padding: 1rem;
    }
    /* DataFrame styling */
    .dataframe {
        color: white !important;
    }
    /* Container styling */
    .main-container {
        background-color: rgba(20, 20, 20, 0.7);
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    /* Progress bar */
    .stProgress > div > div {
        background-color: #80c241;
    }
    /* Checkbox */
    .stCheckbox label {
        color: white !important;
    }
    .stCheckbox label:hover {
        color: #80c241 !important;
    }
    /* Multiselect */
    .stMultiSelect {
        background-color: #1e1e1e;
    }
    /* Expander */
    .streamlit-expanderHeader {
        color: #80c241 !important;
        font-weight: bold;
    }
    /* Divider */
    hr {
        border-color: #3c3c3c;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }
    /* Remove unnecessary padding and borders */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    /* Clean up the subtitle spacing */
    .subtitle {
        margin-bottom: 1.5rem;
        margin-top: 0;
        font-size: 1.2rem;
        font-weight: normal;
    }
    /* Fix any unexpected containers */
    div.stMarkdown {
        background-color: transparent !important;
        border: none !important;
    }
    /* Footer styling */
    footer {
        visibility: hidden;
    }
    .footer-text {
        text-align: center;
        color: #666 !important;
        padding: 1rem 0;
        font-size: 0.8rem;
    }
    /* Navy blue download button */
    .navy-download-button button {
        background-color: navy !important;
        color: white !important;
        border: none;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        transition: all 0.3s;
    }
    .navy-download-button button:hover {
        background-color: #000080 !important;
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# App header - removed logo section
st.title("🧹 Yonah's Column Cleaner")

# Subtitle with clean styling
st.markdown("<p class='subtitle'>Simplify your csv file by keeping only the columns you need</p>", unsafe_allow_html=True)

# Default columns to keep - this can be customized
DEFAULT_COLUMNS = ['Last Name', 'First Name', 'Job Title', 'Direct Phone Number', 'Email Address', 
                   'LinkedIn Contact Profile URL', 'Company Name', 'Website', 'Company Zip Code', 
                   'Company Country', 'Full Address']

# Initialize session state for storing dataframe and settings
if 'dataframe' not in st.session_state:
    st.session_state.dataframe = None
if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False
if 'columns_selected' not in st.session_state:
    st.session_state.columns_selected = DEFAULT_COLUMNS
if 'all_columns' not in st.session_state:
    st.session_state.all_columns = []
if 'download_ready' not in st.session_state:
    st.session_state.download_ready = False

# File upload section
with st.container():
    st.subheader("Step 1: Upload your file")
    upload_help = "Supported format: CSV (.csv)"
    uploaded_file = st.file_uploader(f"Choose a CSV file to clean", 
                                  type=["csv"],
                                  help=upload_help)

# Process the uploaded file
if uploaded_file is not None:
    try:
        with st.spinner("Processing your file..."):
            # Show a progress bar to indicate loading
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)  # Simulate processing time
                progress_bar.progress(i + 1)
            
            # Read the CSV file
            df = pd.read_csv(uploaded_file)
            
            # Store dataframe in session state
            st.session_state.dataframe = df
            st.session_state.all_columns = df.columns.tolist()
            st.session_state.file_uploaded = True
            
            # Filter to keep only available columns from our defaults
            st.session_state.columns_selected = [col for col in DEFAULT_COLUMNS if col in df.columns]
            
            # Success message with file info
            st.success(f"✅ File '{uploaded_file.name}' loaded successfully!")
            st.markdown(f"**File details:** {len(df)} rows, {len(df.columns)} columns")
        
    except Exception as e:
        st.error(f"❌ Error processing file: {str(e)}")
        st.session_state.file_uploaded = False

# Column selection section (only show if file is uploaded)
if st.session_state.file_uploaded and st.session_state.dataframe is not None:
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    with st.container():
        st.subheader("Step 2: Select columns to keep")
        
        # Two-column layout for column selection
        selection_col1, selection_col2 = st.columns([1, 1])
        
        with selection_col1:
            # Quick column selection shortcuts
            st.markdown("#### Quick Selection")
            
            quick_col1, quick_col2 = st.columns(2)
            with quick_col1:
                if st.button("Select All", use_container_width=True):
                    st.session_state.columns_selected = st.session_state.all_columns
            
            with quick_col2:
                if st.button("Select Bare Minimum", use_container_width=True):
                    # Select the default columns that exist in the current file
                    bare_minimum_columns = [col for col in DEFAULT_COLUMNS if col in st.session_state.all_columns]
                    
                    # Check if any matching columns were found
                    if len(bare_minimum_columns) > 0:
                        st.session_state.columns_selected = bare_minimum_columns
                    else:
                        # Show a popup-like message when no columns match
                        st.error("⚠️ Ignore this button - No matching columns found in your CSV file!")
                        st.info("Your CSV file doesn't contain any of the expected column names. Please use 'Select All' or manually select columns instead.")
        
        with selection_col2:
            # Custom column selection
            st.markdown("#### Column Selection")
            st.session_state.columns_selected = st.multiselect(
                "Choose specific columns to keep:",
                options=st.session_state.all_columns,
                default=st.session_state.columns_selected,
                help="Select the columns you want to keep in your cleaned file"
            )
    
    # Preview section
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    with st.container():
        st.subheader("Step 3: Preview and download")
        
        if len(st.session_state.columns_selected) > 0:
            try:
                # Create cleaned dataframe
                cleaned_df = st.session_state.dataframe[st.session_state.columns_selected]
                
                # Show preview with column info
                st.markdown(f"**Preview:** Showing {len(st.session_state.columns_selected)} columns out of {len(st.session_state.all_columns)} total")
                st.dataframe(cleaned_df.head(5), use_container_width=True)
                
                # Display stats about data cleaning
                reduction = (1 - len(st.session_state.columns_selected) / len(st.session_state.all_columns)) * 100
                st.success(f"🎉 File size reduced by approximately {reduction:.1f}% by removing {len(st.session_state.all_columns) - len(st.session_state.columns_selected)} columns!")
                
                # Download section
                st.markdown("#### Download your cleaned file")
                
                # Add extension based on original file if possible
                original_name = uploaded_file.name
                # Split name and extension to insert "cleaned" before extension
                file_name_parts = original_name.rsplit('.', 1)
                if len(file_name_parts) == 2:
                    base_name, extension = file_name_parts
                    output_filename = f"{base_name}_cleaned.{extension}"
                else:
                    output_filename = f"{original_name}_cleaned.csv"
                
                # Generate CSV data
                csv_data = cleaned_df.to_csv(index=False)
                
                download_col1, download_col2, download_col3 = st.columns([2, 1, 2])
                with download_col2:
                    st.download_button(
                        label="💾 Download Cleaned File",
                        data=csv_data,
                        file_name=output_filename,
                        mime="text/csv",
                        help="Download your cleaned CSV file with only the selected columns",
                        use_container_width=True
                        key="navy-download-button"
                    )
                
            except Exception as e:
                st.error(f"❌ Error generating preview: {str(e)}")
        else:
            st.warning("⚠️ Please select at least one column to keep")

# Footer
st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown("<p class='footer-text'>Made by YonahAndTheWhale | © 2023</p>", unsafe_allow_html=True)
