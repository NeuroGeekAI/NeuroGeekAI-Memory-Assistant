#!/usr/bin/env python3
import json
from pathlib import Path
import datetime

def create_readable_summary():
    # Dossier source
    input_dir = Path("cursor_exports")
    
    # Créer fichier résumé
    with open("chat_summary.txt", "w", encoding="utf-8") as summary:
        summary.write("📚 RÉSUMÉ DES CONVERSATIONS CURSOR 📚\n")
        summary.write("=====================================\n\n")
        
        # Lire tous les .json
        json_files = sorted(input_dir.glob("*.json"))
        
        for json_path in json_files:
            try:
                with open(json_path, encoding="utf-8") as f:
                    chat = json.load(f)
                
                # Extraire infos
                date = datetime.datetime.fromtimestamp(chat["createdAt"]/1000)
                name = chat.get("name", "Sans titre")
                
                # Écrire dans le résumé
                summary.write(f"📅 {date.strftime('%d/%m/%Y %H:%M')}\n")
                summary.write(f"📝 {name}\n")
                
                # Extraire début conversation
                if "conversation" in chat:
                    first_msg = chat["conversation"][0]["text"]
                    summary.write(f"💬 Début: {first_msg[:100]}...\n")
                
                summary.write("-----------------------------------\n\n")
                
            except Exception as e:
                continue

        summary.write("\n✨ Fin du résumé ✨")

if __name__ == "__main__":
    print("📝 Création du résumé...")
    create_readable_summary()
    print("✅ Résumé créé dans chat_summary.txt")