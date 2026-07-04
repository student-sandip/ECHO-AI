from ollama import chat

from brain.prompts import SYSTEM_PROMPT
from brain.extractor import extract_memory
from brain.memory_manager import (
    auto_save,
    get_memory,
    show_memory,
    clear_all_memory,
    forget_memory
)

from memory.memory import (
    add_chat,
    get_chat_history
)


# ==========================================================
# ECHO AI
# ==========================================================

def ask_echo(prompt):

    lower = prompt.lower().strip()

    # ======================================================
    # Automatic Memory Save
    # ======================================================

    memory = extract_memory(prompt)

    if memory:

        auto_save(memory)

    # ======================================================
    # Name Recall
    # ======================================================

    if lower in [
        "who am i",
        "what is my name",
        "do you know my name"
    ]:

        name = get_memory(
            "personal",
            "name"
        )

        if name:

            yield f"Your name is {name}."

        else:

            yield "I don't know your name yet."

        return

    # ======================================================
    # Favorite Language
    # ======================================================

    if (
        "favorite language" in lower
        or "favourite language" in lower
    ):

        language = get_memory(
            "preferences",
            "favorite_language"
        )

        if language:

            yield f"Your favorite language is {language}."

        else:

            yield "I don't know your favorite language yet."

        return

    # ======================================================
    # Favorite Color
    # ======================================================

    if (
        "favorite color" in lower
        or "favourite color" in lower
    ):

        color = get_memory(
            "preferences",
            "favorite_color"
        )

        if color:

            yield f"Your favorite color is {color}."

        else:

            yield "I don't know your favorite color yet."

        return

    # ======================================================
    # Show Memory
    # ======================================================

    if lower in [

        "show memory",
        "my memory",
        "show my memory",
        "what do you know about me"

    ]:

        memory = show_memory()

        if memory:

            yield memory

        else:

            yield "I don't know anything about you yet."

        return

    # ======================================================
    # Clear Memory
    # ======================================================

    if lower in [

        "clear memory",
        "reset memory"

    ]:

        clear_all_memory()

        yield "All memories have been cleared."

        return

    # ======================================================
    # Forget Command
    # ======================================================

    if lower.startswith("forget"):

        command = lower.replace(
            "forget",
            ""
        ).strip()

        words = command.split()

        if len(words) >= 2:

            category = words[0]

            key = "_".join(words[1:])

            ok = forget_memory(
                category,
                key
            )

            if ok:

                yield "Done. I forgot it."

            else:

                yield "I couldn't find that memory."

            return

    # ======================================================
    # Conversation
    # ======================================================

    add_chat(
        "user",
        prompt
    )

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }

    ]

    messages.extend(
        get_chat_history()
    )

    stream = chat(

        model="llama3.2",

        messages=messages,

        stream=True

    )

    reply = ""

    for chunk in stream:

        text = chunk["message"]["content"]

        reply += text

        yield text

    add_chat(
        "assistant",
        reply
    )