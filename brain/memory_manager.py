from memory.memory import (
    remember,
    recall,
    forget,
    clear_memory,
    get_all_memory,
    memory_summary
)


# ==========================================================
# Save Memory
# ==========================================================

def save_memory(memory):

    if memory is None:

        return False

    category = memory["category"]
    key = memory["key"]
    value = memory["value"]

    remember(
        category,
        key,
        value
    )

    return True


# ==========================================================
# Recall Memory
# ==========================================================

def recall_memory(category, key):

    return recall(
        category,
        key
    )


# ==========================================================
# Forget Memory
# ==========================================================

def forget_memory(category, key):

    value = recall(
        category,
        key
    )

    if value is None:

        return False

    forget(
        category,
        key
    )

    return True


# ==========================================================
# Clear All Memory
# ==========================================================

def clear_all_memory():

    clear_memory()


# ==========================================================
# Show Memory
# ==========================================================

def show_memory():

    return memory_summary()


# ==========================================================
# Memory Exists
# ==========================================================

def memory_exists(category, key):

    value = recall(
        category,
        key
    )

    return value is not None


# ==========================================================
# Get Value
# ==========================================================

def get_memory(category, key):

    return recall(
        category,
        key
    )


# ==========================================================
# Get All Memories
# ==========================================================

def get_memories():

    return get_all_memory()


# ==========================================================
# Auto Save
# ==========================================================

def auto_save(memory):

    if memory is None:

        return False

    if not all(k in memory for k in ["category", "key", "value"]):

        return False

    remember(
        memory["category"],
        memory["key"],
        memory["value"]
    )

    return True


# ==========================================================
# Search Memory
# ==========================================================

def search_memory(keyword):

    keyword = keyword.lower()

    memories = get_all_memory()

    results = []

    for category in memories:

        for key, value in memories[category].items():

            if (
                keyword in key.lower()
                or keyword in str(value).lower()
            ):

                results.append(
                    {
                        "category": category,
                        "key": key,
                        "value": value
                    }
                )

    return results