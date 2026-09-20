import streamlit as st
from pathlib import Path
from pdf_converter import convert_pdf_to_word


st.set_page_config(
    page_title="PDF to Word Converter",
    page_icon="📄",
    layout="centered"
)


st.title("📄 PDF to Word Converter")
st.write(
    "Convert your PDF into an editable Microsoft Word document "
    "while preserving text, images and page layout as closely as possible."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload your PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(f"PDF selected: {uploaded_file.name}")

    temp_dir = Path("uploads")
    output_dir = Path("outputs")

    temp_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    input_path = temp_dir / uploaded_file.name

    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    output_name = Path(uploaded_file.name).stem + "_Editable.docx"
    output_path = output_dir / output_name

    if st.button("🔄 Convert to Word File", use_container_width=True):

        try:
            with st.spinner("Converting PDF to editable Word..."):

                convert_pdf_to_word(
                    str(input_path),
                    str(output_path)
                )

            st.success("✅ Conversion completed!")

            with open(output_path, "rb") as f:
                word_data = f.read()

            st.download_button(
                label="⬇️ Download Editable Word File",
                data=word_data,
                file_name=output_name,
                mime=(
                    "application/vnd.openxmlformats-officedocument."
                    "wordprocessingml.document"
                ),
                use_container_width=True
            )

        except Exception as e:

            st.error("❌ Conversion failed.")
            st.code(str(e))

else:

    st.info("👆 Upload a PDF file to start.")
