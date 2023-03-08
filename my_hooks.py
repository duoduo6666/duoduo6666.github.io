from urllib.parse import unquote

def on_page_markdown(markdown:str, **kwargs):
    print(kwargs)
    k = {
        "site_author_url": "https://github.com/duoduo6666/",
        "site_author": kwargs["config"]["site_author"],
        "site_url": kwargs["config"]["site_url"],
        "url": kwargs["page"].url,
        "url_decode": unquote(kwargs["page"].url)
        }
    return markdown.format(**k)