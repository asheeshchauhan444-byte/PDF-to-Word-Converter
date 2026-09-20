from pdf2docx import Converter
from pathlib import Path


def convert_pdf_to_word(pdf_path, output_path):
    pdf_path = str(Path(pdf_path).resolve())
    output_path = str(Path(output_path).resolve())

    if not Path(pdf_path).exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    print("Starting PDF to Word conversion...")
    print("Input :", pdf_path)
    print("Output:", output_path)

    converter = Converter(pdf_path)

    try:
        converter.convert(
            output_path,
            start=0,
            end=None
        )
    finally:
        converter.close()

    if not Path(output_path).exists():
        raise RuntimeError("Word file was not created.")

    print("Conversion completed successfully.")
    return output_path
