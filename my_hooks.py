from urllib.parse import unquote

site_author_url = "https://github.com/duoduo6666/"

def on_page_markdown(markdown:str, **kwargs):
    site_author =  kwargs["config"]["site_author"]
    site_url = kwargs["config"]["site_url"]
    url = kwargs["page"].url
    url_decode = unquote(kwargs["page"].url)
    state = f"""<div style="font-size:10px; line-height:1px">
<p>本文作者： <a href="{site_author_url}">{site_author}</a>, 文章链接： <a href="{site_url}{url}">{site_url}{url_decode}</a></p>
<p>本文为博主原创文章，采用<strong><a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a></strong>协议发布。</p>
</div>"""
    return markdown.format(state=state)