import json
import os

CHAT_HISTORY_FILE = "memory/chat_history.json"
USER_MEMORY_FILE = "memory/user_memory.json"

MAX_CHAT_HISTORY = 20


# ------------------------------
# Utility
# ------------------------------

def load_json(path, default):

    if not os.path.exists(path):
        return default

    try:

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except:

        return default


def save_json(path, data):

    with open(path, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# ------------------------------
# Chat History
# ------------------------------

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

    if len(chat_history) > MAX_CHAT_HISTORY:

        del chat_history[0]

    save_json(
        CHAT_HISTORY_FILE,
        chat_history
    )


def get_chat_history():

    return chat_history


def clear_chat():

    chat_history.clear()

    save_json(
        CHAT_HISTORY_FILE,
        chat_history
    )


# ------------------------------
# Long Term Memory
# ------------------------------

user_memory = load_json(
    USER_MEMORY_FILE,
    {}
)


def remember(key, value):

    user_memory[key] = value

    save_json(
        USER_MEMORY_FILE,
        user_memory
    )


def recall(key):

    return user_memory.get(key)


def get_all_memory():

    return user_memory


def forget(key):

    if key in user_memory:

        del user_memory[key]

        save_json(
            USER_MEMORY_FILE,
            user_memory
        )

# ------------------------------
# Smart Memory
# ------------------------------

def has_memory(key):
    return key in user_memory


def memory_keys():
    return list(user_memory.keys())       