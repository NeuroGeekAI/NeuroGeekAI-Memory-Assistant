#!/usr/bin/env python3
import json
from pathlib import Path
import datetime
import re

def clean_text(text):
    # Nettoyer plus agressivement les espaces
    # Remplacer multiples lignes vides par une seule
    text = re.sub(r'\n\s*\n', '\n', text)
    # Enlever espaces début/fin de chaque ligne
    lines = [line.strip() for line in text.split('\n')]
    # Rejoindre les lignes avec un seul saut de ligne
    text = '\n'.join(line for line in lines if line)
    return text

def save_full_conversation(json_file, output_dir):
    try:
        # Lire le JSON
        with open(json_file, encoding="utf-8") as f:
            chat = json.load(f)
        
        # Créer nom fichier avec timestamp
        date = datetime.datetime.fromtimestamp(chat["createdAt"]/1000)
        name = chat.get("name", "Sans titre")
        safe_name = "".join(x for x in name if x.isalnum() or x in (' ','-','_'))
        output_file = output_dir / f"vie_privee_{date.strftime('%Y%m%d_%H%M')}_{safe_name}.txt"
        
        # Vérifier si fichier existe déjà
        if output_file.exists():
            return False, "Déjà sauvegardé"
        
        # Sauvegarder toute la conversation
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("🔐 SAUVEGARDE CONVERSATION\n")
            f.write(f"📅 DATE: {date.strftime('%d/%m/%Y %H:%M')}\n")
            f.write("="*50 + "\n")
            
            for msg in chat["conversation"]:
                role = "👤 MOI" if msg.get("role") == "human" else "🤖 ASSISTANT"
                text = clean_text(msg.get('text', ''))
                if text:  # Ne pas écrire si texte vide
                    f.write(f"{role}:\n")
                    f.write(f"{text}\n")
                    f.write("-"*20 + "\n")
            
            f.write("🔒 FIN SAUVEGARDE\n")
        
        return True, "Sauvegardé"
        
    except Exception as e:
        print(f"❌ Erreur avec {json_file}: {e}")
        return False, "Erreur"

def main():
    input_dir = Path("cursor_exports")
    output_dir = Path("vie_privee")
    output_dir.mkdir(exist_ok=True)
    
    # Vérifier s'il y a des fichiers à traiter
    json_files = list(input_dir.glob("*.json"))
    if not json_files:
        print("❌ Aucun fichier JSON trouvé dans cursor_exports")
        print("💡 Créez une nouvelle session Cursor pour exporter les conversations récentes")
        return
    
    new_files = 0
    skipped = 0
    
    for json_file in json_files:
        print(f"🔍 Traitement de {json_file.name}...")
        result, info = save_full_conversation(json_file, output_dir)
        if result:
            new_files += 1
            print(f"✅ {info}")
        else:
            skipped += 1
            print(f"⏭️ {info}")
    
    print("\n🔒 SAUVEGARDE TERMINÉE")
    print(f"📝 Nouveaux fichiers: {new_files}")
    print(f"⏭️ Fichiers ignorés: {skipped}")
    print(f"📂 Dossier: {output_dir}")
    
    if new_files == 0:
        print("\n💡 CONSEIL: Créez une nouvelle session Cursor pour sauvegarder les conversations récentes")

if __name__ == "__main__":
    main()