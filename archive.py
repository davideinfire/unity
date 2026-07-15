def list_entries(entries):

    print()

    for entry in entries:

        print(entry.date)

        print(f"Mood: {entry.mood}")

        print(entry.text)

        print()

        print("-" * 25)
