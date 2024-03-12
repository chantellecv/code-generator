import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the app
st.title('Basic Data Analysis App')

# Allow file upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)
    
    # Display dataset structure
    if st.checkbox('Show dataset structure'):
        st.write(df.head())
    
    # Calculate summary statistics
    if st.checkbox('Show summary statistics'):
        st.write(df.describe())
    
    # Data Visualizations
    if st.checkbox('Visualize data'):
        st.subheader('Data Visualization')
        # Plot options
        plot_type = st.selectbox("Choose plot type", ['Histogram', 'Boxplot', 'Correlation Heatmap'])
        
        if plot_type == 'Histogram':
            column_to_plot = st.selectbox("Choose column to plot", df.columns)
            bins = st.slider("Number of bins", min_value=10, max_value=100, value=30)
            plt.hist(df[column_to_plot], bins=bins)
            plt.title(f'Histogram of {column_to_plot}')
            plt.ylabel('Frequency')
            plt.xlabel(column_to_plot)
            st.pyplot(plt)
        
        elif plot_type == 'Boxplot':
            column_to_plot = st.selectbox("Choose column for Boxplot", df.columns)
            sns.boxplot(y=df[column_to_plot])
            plt.title(f'Boxplot of {column_to_plot}')
            st.pyplot(plt)
        
        elif plot_type == 'Correlation Heatmap':
            corr = df.corr()
            sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
            plt.title('Correlation Heatmap')
            st.pyplot(plt)

# Note: Make sure to adjust plt.figure() sizes (not shown here) as needed for better layout in the app.