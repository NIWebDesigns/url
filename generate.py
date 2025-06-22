import os
import json

# Load the short links
with open("links.json", "r") as f:
    links = json.load(f)

# Create the output folder if it doesn't exist
os.makedirs("links", exist_ok=True)

# Template for redirect pages
template = """<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="0; url={url}" />
  </head>
  <body>
    <p>Redirecting to <a href="{url}">{url}</a></p>
  </body>
</html>
"""

# Generate a folder and index.html for each short link
for slug, target_url in links.items():
    path = os.path.join("links", slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(template.format(url=target_url))

print("✅ Pages generated in 'links/' folder.")
