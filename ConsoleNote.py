import argparse
import Note
import NotesManager

parser = argparse.ArgumentParser(description='Notes application')
parser.add_argument('command', choices=['list', 'create', 'update', 'delete'], help='Command to execute')
parser.add_argument('--id', type=int, help='Note ID')
parser.add_argument('--title', help='Note title')
parser.add_argument('--body', help='Note body')

args = parser.parse_args()

notes_manager = NotesManager.NotesManager('notes.json')
notes_manager.load_notes()

if args.command == 'list':
    for note in notes_manager.notes:
        print(f'{note.id} - {note.title}')
elif args.command == 'create':
    note = notes_manager.add_note(args.title, args.body)
    print(f'Note created with ID {note.id}')
elif args.command == 'update':
    notes_manager.update_note_by_id(args.id, title=args.title, body=args.body)
    print(f'Note with ID {args.id} updated')
elif args.command == 'delete':
    notes_manager.delete_note_by_id(args.id)
    print(f'Note with ID {args.id} deleted')

notes_manager.save_notes()