from journal import Journal

from demo_entries import ENTRIES

from timeline import ordered

from archive import list_entries

from writer import report

journal = Journal()

for entry in ENTRIES:

    journal.add(entry)

entries = ordered(

    journal.all()

)

list_entries(entries)

report(entries)
