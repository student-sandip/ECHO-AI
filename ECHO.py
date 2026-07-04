from brain.ai import ask_echo
import time


# ==========================================================
# ECHO AI Assistant
# Version : 0.4
# Author  : Sandip
# ==========================================================


# ----------------------------------------------------------
# Startup Banner
# ----------------------------------------------------------

def startup():

    print("=" * 60)
    print("                 🤖 ECHO AI Assistant")
    print("=" * 60)

    loading_steps = [
        "Loading Brain............. ✅",
        "Loading AI Engine......... ✅",
        "Loading Memory............ ✅",
        "Initializing Chat......... ✅",
        "System Ready.............. ✅"
    ]

    for step in loading_steps:
        print(step)
        time.sleep(0.25)

    print("\nWelcome back, Sandip! 👋")
    print("Type 'exit' anytime to close ECHO.\n")


# ----------------------------------------------------------
# Thinking Animation
# ----------------------------------------------------------

def thinking():

    print("\n🧠 ECHO is thinking...", flush=True)


# ----------------------------------------------------------
# Stream Output
# ----------------------------------------------------------

def print_stream(stream):

    for chunk in stream:

        print(chunk, end="", flush=True)

    print()


# ----------------------------------------------------------
# Main Chat Loop
# ----------------------------------------------------------

def chat():

    while True:

        try:

            user = input("👤 You : ").strip()

            if not user:
                continue

            if user.lower() in [
                "exit",
                "quit",
                "bye"
            ]:

                print("\n🤖 ECHO : Goodbye Sandip! Have a wonderful day! 👋")
                break

            thinking()

            print("\n🤖 ECHO : ", end="", flush=True)

            stream = ask_echo(user)

            print_stream(stream)

            print()

        except KeyboardInterrupt:

            print("\n\n👋 ECHO stopped by user.")
            break

        except Exception as e:

            print(f"\n❌ Error : {e}")


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------

def main():

    startup()

    chat()


# ----------------------------------------------------------
# Entry Point
# ----------------------------------------------------------

if __name__ == "__main__":

    main()