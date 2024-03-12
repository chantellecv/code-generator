import streamlit as st
import gzip
import shutil

# Function to read a file
def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

# Function to write to a file
def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    return f"Content written to {file_path}"

# Function to compress a file
def compress_file(input_file_path, output_file_path):
    with open(input_file_path, "rb") as f_in:
        with gzip.open(output_file_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    return f"File compressed as {output_file_path}"

# Function to decompress a gzip file
def decompress_file(input_file_path, output_file_path):
    with gzip.open(input_file_path, "rb") as f_in:
        with open(output_file_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    return f"File decompressed as {output_file_path}"

# Streamlit UI
st.title("File Operations App")

# Sidebar options
operation = st.sidebar.selectbox("Choose an operation:", ["Read", "Write", "Compress", "Decompress"])

if operation == "Read":
    uploaded_file = st.file_uploader("Choose a file to read", type=['txt', 'gz'])
    if uploaded_file is not None:
        file_content = read_file(uploaded_file)
        st.write(file_content)
elif operation == "Write":
    content_to_write = st.text_area("Enter content to write to file:")
    file_name_to_write = st.text_input("Enter the name of the new file (with extension):")
    if st.button("Write to File"):
        write_message = write_file(file_name_to_write, content_to_write)
        st.success(write_message)
elif operation == "Compress":
    file_to_compress = st.file_uploader("Choose a file to compress", type=['txt'])
    output_file_name = st.text_input("Enter the name of the compressed file (with .gz extension):")
    if st.button("Compress File"):
        compress_message = compress_file(file_to_compress, output_file_name)
        st.success(compress_message)
elif operation == "Decompress":
    file_to_decompress = st.file_uploader("Choose a .gz file to decompress", type=['gz'])
    decompressed_file_name = st.text_input("Enter the name for the decompressed file:")
    if st.button("Decompress File"):
        decompress_message = decompress_file(file_to_decompress, decompressed_file_name)
        st.success(decompress_message)