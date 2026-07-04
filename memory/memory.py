import json
import os

# ==========================================================
# ECHO Memory System
# Version : 0.4
# Author  : Sandip
# ==========================================================

BASE_DIR = os.path.dirname(__file__)

CHAT_HISTORY_FILE = os.path.join(BASE_DIR, "chat_history.json")
USER_MEMORY_FILE = os.path.join(BASE_DIR, "user_memory.json")

MAX_CHAT_HISTORY = 20


# ==========================================================
# JSON Utilities
# ==========================================================

def load_json(file_path, default):

    if not os.path.exists(file_path):

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(default, file, indent=4)

        return default

    try:

        with open(file_path, "r", encoding="utf-8") as file:

            return json.load(file)

    except:

        return default


def save_json(file_path, data):

    with open(file_path, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# ==========================================================
# Chat History
# ==========================================================

chat_history = load_json(
    CHAT_HISTORY_FILE,
    []
)


def add_chat(role, content):

    chat_history.append(
        {
            "role": role,
            "content": content
        }
    )

    while len(chat_history) > MAX_CHAT_HISTORY:

        chat_history.pop(0)

    save_json(
        CHAT_HISTORY_FILE,
        chat_history
    )


def get_chat_history():

    return chat_history


def clear_chat():

    global chat_history

    chat_history = []

    save_json(
        CHAT_HISTORY_FILE,
        chat_history
    )


# ==========================================================
# Long Term Memory
# ==========================================================

user_memory = load_json(
    USER_MEMORY_FILE,
    {
        "personal": {},
        "preferences": {},
        "projects": {},
        "other": {}
    }
)


def remember(category, key, value):

    category = category.lower()

    if category not in user_memory:

        user_memory[category] = {}

    user_memory[category][key] = value

    save_json(
        USER_MEMORY_FILE,
        user_memory
    )


def recall(category, key):

    category = category.lower()

    if category not in user_memory:

        return None

    return user_memory[category].get(key)


def forget(category, key):

    category = category.lower()

    if category in user_memory:

        if key in user_memory[category]:

            del user_memory[category][key]

            save_json(
                USER_MEMORY_FILE,
                user_memory
            )


def clear_memory():

    global user_memory

    user_memory = {
        "personal": {},
        "preferences": {},
        "projects": {},
        "other": {}
    }

    save_json(
        USER_MEMORY_FILE,
        user_memory
    )


def get_all_memory():

    return user_memory


# ==========================================================
# Helper Functions
# ==========================================================

def has_memory(category, key):

    category = category.lower()

    if category not in user_memory:

        return False

    return key in user_memory[category]


def memory_summary():

    text = ""

    for category in user_memory:

        if len(user_memory[category]) == 0:
            continue

        text += f"\n[{category.upper()}]\n"

        for key, value in user_memory[category].items():

            text += f"{key} : {value}\n"

    return text.strip()