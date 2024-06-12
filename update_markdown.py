import openai

# create prompt
prompt = "Take the contents of this xelatex document and write a markdown file with the same information:\n```"

with open("cv.tex", "r") as f:
    prompt += f.read()

prompt += "\n```"

# Get response
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": prompt}
    ]
)

# Write response to file
with open("cv.md", "w") as f:
    f.write(response.choices[0].message.content)