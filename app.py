
import streamlit as st
from pathlib import Path
from pdf_converter import convert_pdf_to_word

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

st.set_page_config(
    page_title="PDF to Word Converter",
    page_icon="📄",
    layout="centered"
)

st.title("📄 PDF to Word Converter")

st.write(
    "Convert your PDF into a Word document "
    "while preserving the visual appearance "
    "of every page."
)

st.divider()

uploaded_file = st.file_uploader(
    "📤 Upload your PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(
        f"PDF selected: {uploaded_file.name}"
    )

    st.write(
        "Ready to convert your PDF."
    )

    convert_button = st.button(
        "🔄 Convert to Word File",
        type="primary"
    )

    if convert_button:

        try:

            with st.spinner(
                "Converting PDF to Word..."
            ):

                input_path = (
                    UPLOAD_DIR /
                    uploaded_file.name
                )

                with open(
                    input_path,
                    "wb"
                ) as file:

                    file.write(
                        uploaded_file.getbuffer()
                    )

                output_name = (
                    Path(
                        uploaded_file.name
                    ).stem
                    + ".docx"
                )

                output_path = (
                    OUTPUT_DIR /
                    output_name
                )

                convert_pdf_to_word(
                    input_path,
                    output_path,
                    dpi=200
                )

            st.success(
                "✅ Conversion completed successfully!"
            )

            with open(
                output_path,
                "rb"
            ) as file:

                word_data = file.read()

            st.download_button(
                label="📥 Download Word File",
                data=word_data,
                file_name=output_name,
                mime=(
                    "application/vnd.openxmlformats-"
                    "officedocument.wordprocessingml.document"
                )
            )

        except Exception as error:

            st.error(
                "❌ Conversion failed."
            )

            st.code(
                str(error)
            )

else:

    st.info(
        "Please upload a PDF file to begin."
    )

st.divider()

st.caption(
    "PDF to Word Converter | "
    "Python + PyMuPDF + python-docx"
)
