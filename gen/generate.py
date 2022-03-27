import os
from os import path
from typing import Dict

def create_dir(p):
    if not path.exists(p):
        os.mkdir(p)

OutputPath = "../www.contextuallight.com"
SnippetPath = "meta"
ContentPath = "content"

create_dir(OutputPath)

BasicPage  = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital@0;1&display=block" rel="stylesheet">
    <meta name="author" content="Chris Osborne">
    <meta name="description" content="Solar physics, and other musings.">
    <link rel="stylesheet" href="main.css">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="icon" href="favicon.svg" type="image/svg+xml">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5">
    <meta name="msapplication-TileColor" content="#da532c">
    <meta name="theme-color" content="#ffffff">
    <title>{Title}</title>
    <script src="https://kit.fontawesome.com/d3ebb79b80.js" crossorigin="anonymous"></script>
</head>
<body>
<div class="not-footer">

{Header}

{Body}

</div>
{Footer}
</body>
</html>
"""

TitleExceptions = {
    "Main": "Contextual Light"
}

def load_single_file(p: str) -> str:
    with open(p, "r") as f:
        return f.read()

def nameify(s: str) -> str:
    return path.splitext(s)[0].replace("_", " ").capitalize()

def html_nameify(s: str) -> str:
    return s.lower().replace(" ", "_") + ".html"

def page_title(name: str) -> str:
    try:
        return TitleExceptions[name]
    except KeyError:
        return name + ": Contextual Light"

def load_file_chunks_from(dir: str) -> Dict[str, str]:
    snippets = {nameify(s): path.join(dir, s) for s in os.listdir(dir)}
    result = {s: load_single_file(p) for s, p in snippets.items()}
    return result

def render_basic_page(content: str, snippets: Dict[str, str], **kwargs) -> str:
    return BasicPage.format(Body=content, **snippets, **kwargs)

def output_to(p: str, content: str):
    with open(path.join(OutputPath, p), "w") as f:
        f.write(content)

if __name__ == "__main__":
    snippets = load_file_chunks_from(SnippetPath)
    content_chunks = load_file_chunks_from(ContentPath)

    for name, content in content_chunks.items():
        page = render_basic_page(content, snippets, Title=page_title(name))
        output_to(html_nameify(name), page)
