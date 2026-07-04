import json
import re

from ollama import chat

from brain.prompts import MEMORY_EXTRACTION_PROMPT


# ==========================================================
# Clean JSON
# ==========================================================

def clean_json(text):

    text = text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )

    if match:

        return match.group()

    return ""


# ==========================================================
# Validate Memory
# ==========================================================

def validate_memory(data):

    if not isinstance(data, dict):

        return False

    if not data.get("save"):

        return False

    required = [
        "category",
        "key",
        "value"
    ]

    for item in required:

        if item not in data:

            return False

    return True


# ==========================================================
# Extract Memory
# ==========================================================

def extract_memory(user_message):

    prompt = f"""

{MEMORY_EXTRACTION_PROMPT}

User:

{user_message}

JSON:

"""

    try:

        response = chat(

            model="llama3.2",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        text = response["message"]["content"]

        text = clean_json(text)

        if text == "":

            return None

        data = json.loads(text)

        if validate_memory(data):

            return data

        return None

    except Exception:

        return None


# ==========================================================
# Utility
# ==========================================================

def should_save(memory):

    return memory is not None


def category(memory):

    return memory["category"]


def key(memory):

    return memory["key"]


def value(memory):

    return memory["value"]