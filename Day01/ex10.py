input_notes = input("Enter notes (note1,note2,...): ")
notes = input_notes.split(",")
addition = 0
int_notes = []

for note in notes:
    int_notes.append(int(note))

for note in int_notes:
   addition += note

moyenne = addition / len(notes)
print(moyenne)
