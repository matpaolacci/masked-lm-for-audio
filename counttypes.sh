#!/bin/bash

# Controlla che sia stata fornita una directory come argomento
if [ "$#" -ne 2 ]; then
  echo "Uso: $0 <source> <dest>"
  exit 1
fi

# Directory di partenza
SOURCE_DIR="$1"
DEST_DIR="$2"

# Controlla che la directory esista
if [ ! -d "$SOURCE_DIR" ]; then
  echo "Errore: La directory $SOURCE_DIR non esiste."
  exit 1
fi

# Controlla che la directory esista
if [ ! -d "$DEST_DIR" ]; then
  echo "Errore: La directory $DEST_DIR non esiste."
  exit 1
fi

# Genera il report
echo "Genero il dataset..."

# Trova tutte le cartelle midi nelle sottodirectory e conta i tipi di file
find "$SOURCE_DIR" -type d -name midi | while read -r MIDI_DIR; do
  echo "Analisi della directory: $MIDI_DIR"
  
  find "$MIDI_DIR" -type f | while read -r FILE; do
    # Ottiene il tipo di file usando il comando `file` e lo estrae
    FILE_TYPE=$(file -b --mime-type "$FILE")
    echo "$FILE_TYPE"
  done | sort | uniq -c | sort -nr

  echo "----------------------------------------------------------"
done

exit 0