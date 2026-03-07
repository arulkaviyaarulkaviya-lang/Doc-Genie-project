import ast

class DocGenieAnalyzer:

    @staticmethod
    def extract_function_signature(code):
        tree = ast.parse(code)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):

                params = []
                for arg in node.args.args:
                    params.append({
                        "name": arg.arg,
                        "type": "Any"
                    })

                return {
                    "name": node.name,
                    "params": params,
                    "return_type": "Any"
                }

    @staticmethod
    def generate_google_docstring(signature):

        doc = f'"""{signature["name"]} function.\n\n'

        doc += "Args:\n"

        for p in signature["params"]:
            doc += f'    {p["name"]} ({p["type"]}): description\n'

        doc += "\nReturns:\n"
        doc += f'    {signature["return_type"]}: result\n'

        doc += '"""'

        return doc