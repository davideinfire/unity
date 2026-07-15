from collections import Counter


def summary(entries):

    stats = Counter(

        entry.mood

        for entry in entries

    )

    return stats
