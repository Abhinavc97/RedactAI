from openai import OpenAI
from prompts import get_prompt

client = OpenAI()

def redact_text(text):
    prompt = get_prompt(text)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    content = response.choices[0].message.content
    if "---EXPLANATION---" in content:
        redacted, explanation = content.split("---EXPLANATION---", 1)
        return redacted.strip(), explanation.strip()
    else:
        return content.strip(), "No explanation provided."