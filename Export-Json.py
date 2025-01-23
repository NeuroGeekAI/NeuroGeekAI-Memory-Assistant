#!/usr/bin/env python3
import sqlite3
import json
import datetime
from pathlib import Path
import sys

def get_chat_data_from_db(db_path):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM cursorDiskKV")
        return cursor.fetchall()
    finally:
        if conn:
            conn.close()

def ts_to_str(ts, readable=False):
    ts = ts / 1000
    if readable:
        timestamp = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    else:
        timestamp = datetime.datetime.fromtimestamp(ts).strftime("%Y%m%d-%H%M%S")
    return timestamp

def find_cursor_files():
    # Chemins Windows à vérifier
    paths_to_check = [
        Path.home() / "AppData" / "Roaming" / "Cursor" / "User" / "globalStorage" / "state.vscdb",
        Path.home() / "AppData" / "Local" / "Cursor" / "User" / "globalStorage" / "state.vscdb",
    ]
    
    for path in paths_to_check:
        if path.exists():
            print(f"💡 DB Cursor trouvée : {path}")
            return path
    return None

def handle_chat_data(chat_data, output_dir):
    files_processed = 0
    files_skipped = 0
    
    for row in chat_data:
        try:
            chat = json.loads(row[0])
            if not isinstance(chat, dict):
                continue
                
            name = chat.get("name", "Sans titre")
            ts = ts_to_str(chat.get("createdAt", datetime.datetime.now().timestamp() * 1000))
            
            md_filename = Path(output_dir) / f"{ts}.md"
            json_filename = Path(output_dir) / f"{ts}.json"
            
            # Skip si fichiers existent déjà
            if md_filename.exists() or json_filename.exists():
                files_skipped += 1
                continue

            # Vérification du contenu avant sauvegarde
            if not chat.get("conversation") and not chat.get("text"):
                print(f"⚠️ Conversation vide ignorée : {name}")
                continue

            # Sauvegarde fichiers
            with open(md_filename, "w", encoding="utf-8") as f:
                f.write(f"# {name}\n")
                for block in chat.get("conversation", []):
                    f.write("\n\n---\n")
                    f.write(block.get("text", ""))

            with open(json_filename, "w", encoding="utf-8") as f:
                json.dump(chat, f, indent=2, ensure_ascii=False)

            print(f"✅ Sauvegarde : {name}")
            files_processed += 1
            
        except Exception as e:
            print(f"❌ Erreur : {str(e)}")
            continue

    return files_processed, files_skipped

def main():
    # Cherche d'abord la DB Cursor
    db_file_path = find_cursor_files()
    output_dir = Path("cursor_exports")
    output_dir.mkdir(exist_ok=True)
    
    total_processed = 0
    total_skipped = 0

    print("\n🔍 Recherche des conversations...")
    
    if db_file_path:
        print("📂 Lecture de la base Cursor...")
        chats = get_chat_data_from_db(db_file_path)
        processed, skipped = handle_chat_data(chats, output_dir)
        total_processed += processed
        total_skipped += skipped
    else:
        print("⚠️ Base Cursor non trouvée")

    # Vérifie aussi les exports manuels
    export_dir = Path("cursor_exports")
    if export_dir.exists():
        print("\n📂 Vérification des exports manuels...")
        json_files = list(export_dir.glob("*.json"))
        if json_files:
            for json_file in json_files:
                try:
                    with open(json_file, "r", encoding="utf-8") as f:
                        chat = json.load(f)
                    if chat.get("conversation") or chat.get("text"):
                        print(f"✅ Export trouvé : {json_file.name}")
                        total_processed += 1
                except Exception as e:
                    print(f"❌ Erreur lecture {json_file.name}: {str(e)}")

    print(f"\n✨ Terminé !")
    print(f"📁 Nouveaux fichiers : {total_processed}")
    print(f"⏩ Fichiers ignorés : {total_skipped}")

if __name__ == "__main__":
    main()