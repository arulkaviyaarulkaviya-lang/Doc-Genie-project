import gradio as gr
from analyzer import DocGenieAnalyzer

def generate_doc(code):

    signature = DocGenieAnalyzer.extract_function_signature(code)

    docstring = DocGenieAnalyzer.generate_google_docstring(signature)

    result = code.replace(":", ":\n    " + docstring)

    return result


interface = gr.Interface(
    fn=generate_doc,
    inputs=gr.Textbox(lines=15, label="Enter Python Code"),
    outputs=gr.Code(label="Generated Code"),
    title="Doc-Genie",
    description="Automatic Python Docstring Generator"
)

interface.launch()