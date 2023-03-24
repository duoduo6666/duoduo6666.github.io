from urllib.parse import unquote
from re import compile

def read_macro(name:str) -> str:
    with open(f"macro/{name}.md", "r", encoding="UTF-8") as f:
        macro = f.read()
    return macro

def on_page_markdown(markdown:str, **kwargs):
    macro = {
        "site_author_url": kwargs["config"]["nav"][-1]["GitHub"],
        "site_author": kwargs["config"]["site_author"],
        "site_url": kwargs["config"]["site_url"],
        "url": kwargs["page"].url,
        "url_decode": unquote(kwargs["page"].url),
        }
    macro["state"] = read_macro("state").format(**macro)

    pattern = compile("<python-script>.*</python-script>")
    match = pattern.search(markdown)
    while match:
        s = match.group()[15:-16].format(**macro)
        markdown = markdown[:match.start()] + s + markdown[match.end():]
        match = pattern.search(markdown)
    
    return markdown
