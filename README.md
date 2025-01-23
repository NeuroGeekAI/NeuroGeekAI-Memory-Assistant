
# NeuroGeekAI-Memory-Assistant
🧠 Système de Support Cognitif Alimenté par l'IA | AI-Powered Cognitive Support System

## 🌍 Description [FR]
Assistant de mémoire contextuelle utilisant l'IA pour le support cognitif et la santé mentale. Intègre Cursor Editor et Claude AI pour une gestion intelligente des conversations et du suivi psychologique.

## 🌐 Description [EN]
Contextual memory assistant using AI for cognitive support and mental health. Integrates Cursor Editor and Claude AI for intelligent conversation management and psychological monitoring.

## 🛠️ Technologies
- Python 3.8+
- Cursor Editor API
- Claude AI Integration
- Privacy-First Data Handling

## 📁 Structure
```
NeuroGeekAI-Memory-Assistant/
├── 🔮 cursor_integration/
├── 🧠 claude_handlers/
├── 📝 memory_management/
├── 🔒 privacy_tools/
└── 📚 docs/
```

## 🔒 Confidentialité / Privacy
- Gestion sécurisée des données
- Conformité RGPD
- Secure data management
- GDPR compliance



## 📚 Guide d'Utilisation / Usage Guide

### 🇫🇷 Installation et Utilisation [FR]

1. **Prérequis**
```bash
Python 3.8+
Cursor Editor
Permissions d'accès aux fichiers
```

2. **Structure des Dossiers**
```bash
votre_dossier/
├── cursor_exports/    # Dossier des exports JSON de Cursor
├── vie_privee/        # Dossier de sauvegarde des conversations
└── save_memory.py     # Script principal
```

3. **Utilisation**
```bash
# Donner les droits d'exécution
chmod +x save_memory.py

# Exécuter le script
./save_memory.py
```

4. **Fonctionnalités**
- Sauvegarde automatique des conversations Cursor
- Nettoyage et formatage du texte
- Horodatage des conversations
- Gestion des doublons
- Format de sortie structuré

### 🇬🇧 Installation and Usage [EN]

1. **Prerequisites**
```bash
Python 3.8+
Cursor Editor
File access permissions
```

2. **Folder Structure**
```bash
your_folder/
├── cursor_exports/    # Cursor JSON exports folder
├── vie_privee/        # Conversations backup folder
└── save_memory.py     # Main script
```

3. **Usage**
```bash
# Grant execution rights
chmod +x save_memory.py

# Run the script
./save_memory.py
```

4. **Features**
- Automatic Cursor conversations backup
- Text cleaning and formatting
- Conversation timestamping
- Duplicate management
- Structured output format

## 📋 Format de Sortie / Output Format

```
🔐 SAUVEGARDE CONVERSATION
📅 DATE: DD/MM/YYYY HH:MM
==================================================
👤 MOI:
[Contenu du message]
--------------------
🤖 ASSISTANT:
[Contenu de la réponse]
--------------------
🔒 FIN SAUVEGARDE
```

## ⚠️ Notes Importantes / Important Notes

- Les fichiers JSON doivent être exportés depuis Cursor
- Le script vérifie les doublons avant la sauvegarde
- Les conversations sont horodatées automatiquement
- Le format de sortie est optimisé pour la lisibilité
- Les espaces superflus sont automatiquement nettoyés




## 📝 Licence
Voir le fichier [LICENSE](LICENSE) pour plus de détails.
See [LICENSE](LICENSE) file for details.
