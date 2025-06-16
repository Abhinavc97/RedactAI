def get_prompt(text):
    return f"""
You are a security-focused AI assistant.

Your task is to redact sensitive personal identification information **inline** in the provided text.

Redact the original text by replacing sensitive content **in-place**, without deleting surrounding context.
Please make sure to redact any names,phone numbers, email ids, date of birth,address and any medical information that are not in the public domain. 

After the redacted version, add an explanation section separated by:
`---EXPLANATION---`

Explain **why** you redacted each part and what category it belongs to.

Return only:
1. The redacted version of the original input text
2. An explanation of what was redacted and why

Here is the input:

{text}
"""