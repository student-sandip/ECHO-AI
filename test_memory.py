from memory.memory import *

remember("personal", "name", "Sandip")
remember("preferences", "favorite_language", "Java")
remember("projects", "current_project", "ECHO AI")

print(recall("personal", "name"))
print(recall("preferences", "favorite_language"))

print()

print(memory_summary())