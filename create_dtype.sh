#!/bin/bash

fichier_entree=$1

fichier_sortie=$2

lignes_attribut=$(grep '@ATTRIBUTE' "$fichier_entree")

echo "{" > "$fichier_sortie"

echo "$lignes_attribut" | awk '
  BEGIN { first = 1 }
  {
    if (first) {
      first = 0
    } else {
      printf(",\n")
    }
    gsub(/@ATTRIBUTE /, "", $0)
    split($0, a, " ")
    printf("  '\''%s'\'': '\''%s'\''", a[1], a[2])
  }
  END { printf("\n}\n") }
' >> "$fichier_sortie"

# Afficher un message de confirmation
echo "Liste JSON générée et enregistrée dans $fichier_sortie"
