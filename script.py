from urllib.parse import unquote
from re import compile

class MacroError(Exception): pass

def read_macro(name:str) -> str:
    with open(f"macro/{name}.md", "r", encoding="UTF-8") as f:
        macro = f.read()
    return macro

def on_page_markdown(markdown:str, **kwargs):
    print(kwargs["config"]["nav"])
    macro = {
        "site_author_url": kwargs["config"]["nav"][3]["GitHub"],
        "site_author": kwargs["config"]["site_author"],
        "site_url": kwargs["config"]["site_url"],
        "url": kwargs["page"].url,
        "url_decode": unquote(kwargs["page"].url),
        }
    macro["state"] = read_macro("state").format(**macro)

    pattern = compile("<python-script>.*</python-script>")
    match = pattern.search(markdown)
    while match:
        try:
            s = match.group()[15:-16].format(**macro)
        except KeyError:
            raise MacroError("未找到这个宏")
        markdown = markdown[:match.start()] + s + markdown[match.end():]
        match = pattern.search(markdown)
    
    return markdown
