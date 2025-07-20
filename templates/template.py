# Demo 

import os

TEMPLATES_DIR = "templates"

def get_template(template_name: str) -> tuple:
    """Şablon içeriğini ve değişkenleri döndürür."""
    for ext in ['.html', '.txt']:
        file_path = os.path.join(TEMPLATES_DIR, f"{template_name}{ext}")
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            variables = list(set(re.findall(r"\{(.*?)\}", content)))
            return content, variables
    return None, []
