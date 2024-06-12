import openai

markdown = ""
with open("cv.tex", "r") as f:
    markdown += f.read()

# create prompt
prompt = f"""
Take the contents of this xelatex document and write a markdown file with the same information:

```
{markdown}
```

DO NOT include "```" in the markdown file. only the contents of the markdown file should be included.
"""

# Get response
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": prompt}
    ]
)

payload = response.choices[0].message.content

# Write response to file
with open("cv.md", "w") as f:
    f.write(response.choices[0].message.content)