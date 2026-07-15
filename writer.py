from mood import summary


def report(entries):

    print()

    print(
        f"Entries stored: {len(entries)}"
    )

    moods = summary(entries)

    common = max(

        moods,

        key=moods.get

    )

    print(
        f"Most common mood: {common}"
    )
