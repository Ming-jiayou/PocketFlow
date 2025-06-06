<<<<<<< HEAD
# Batch-Übersetzungsvorgang

Dieses Projekt demonstriert eine Batch-Verarbeitungsimplementierung, die es künstlichen Intelligenzen ermöglicht, Dokumente zeitgleich in mehrere Sprachen zu übersetzen. Es ist darauf ausgelegt, die Übersetzung von Markdown-Dateien effizient zu verarbeiten, während das Format beibehalten wird.

## Funktionen

- Übersetzt Inhalt in Markdown-Format parallel in mehrere Sprachen
- Speichert die übersetzten Dateien in dem angegebenen Ausgabeverzeichnis

## Erste Schritte

1. Installieren Sie die erforderlichen Pakete:
```bash
pip install -r requirements.txt
```

2. Setzen Sie Ihren API-Schlüssel:
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

3. Führen Sie den Übersetzungsvorgang aus:
```bash
python main.py
```
=======
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – 100-Zeilen minimalistisches LLM-Framework" width="600"/>
</div>

<!-- [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) -->

[English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) | [中文](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_CHINESE.md) | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | Deutsch | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)

![Lizenz: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow ist ein [100-zeiliges](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) minimalistisches LLM-Framework

- **Leichtgewichtig**: Nur 100 Zeilen. Kein Ballast, keine Abhängigkeiten, keine Anbieterbindung.
  
- **Ausdrucksstark**: Alles, was Sie lieben—([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agenten](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html), und mehr.

- **[Agenten-basiertes Programmieren](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**: Lassen Sie KI-Agenten (z.B. Cursor AI) Agenten bauen—10-fache Produktivitätssteigerung!

Erste Schritte mit Pocket Flow:
- Zur Installation, ```pip install pocketflow```oder kopieren Sie einfach den [Quellcode](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) (nur 100 Zeilen).
- Um mehr zu erfahren, schauen Sie in die [Dokumentation](https://the-pocket.github.io/PocketFlow/). Um die Motivation zu verstehen, lesen Sie die [Geschichte](https://zacharyhuang.substack.com/p/i-built-an-llm-framework-in-just).
- Haben Sie Fragen? Schauen Sie sich diesen [KI-Assistenten](https://chatgpt.com/g/g-677464af36588191b9eba4901946557b-pocket-flow-assistant) an, oder [erstellen Sie ein Issue!](https://github.com/The-Pocket/PocketFlow/issues/new)
- 🎉 Treten Sie unserem [Discord](https://discord.gg/hUHHE9Sa6T) bei, um sich mit anderen Entwicklern zu vernetzen, die mit Pocket Flow arbeiten!
- 🎉 Pocket Flow ist ursprünglich in Python geschrieben, aber wir haben jetzt auch Versionen für [Typescript](https://github.com/The-Pocket/PocketFlow-Typescript), [Java](https://github.com/The-Pocket/PocketFlow-Java), [C++](https://github.com/The-Pocket/PocketFlow-CPP) und [Go](https://github.com/The-Pocket/PocketFlow-Go)!
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342

## Funktionsweise

<<<<<<< HEAD
Die Implementierung nutzt einen `TranslateTextNode`, der Batches von Übersetzungsanfragen verarbeitet:
=======
Aktuelle LLM-Frameworks sind aufgebläht... Sie brauchen nur 100 Zeilen für ein LLM-Framework!
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342

```mermaid
flowchart LR
    batch[TranslateTextNode]
```

Der `TranslateTextNode`:
1. Bereitet Batches für Übersetzungen in mehrere Sprachen vor
2. Führt die Übersetzungen parallel unter Verwendung des Modells durch
3. Speichert den übersetzten Inhalt in individuelle Dateien
4. Behält die ursprüngliche Markdown-Struktur bei

<<<<<<< HEAD
Dieses Vorgehen zeigt, wie PocketFlow effizient mehrere verwandte Aufgaben parallel verarbeiten kann.
=======
  |                | **Abstraktion**          | **App-spezifische Wrapper**                                      | **Anbieter-spezifische Wrapper**                                    | **Zeilen**       | **Größe**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | Agent, Chain               | Viele <br><sup><sub>(z.B. QA, Zusammenfassung)</sub></sup>              | Viele <br><sup><sub>(z.B. OpenAI, Pinecone, etc.)</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | Agent, Chain            | Viele <br><sup><sub>(z.B. FileReadTool, SerperDevTool)</sub></sup>         | Viele <br><sup><sub>(z.B. OpenAI, Anthropic, Pinecone, etc.)</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | Agent                      | Einige <br><sup><sub>(z.B. CodeAgent, VisitWebTool)</sub></sup>         | Einige <br><sup><sub>(z.B. DuckDuckGo, Hugging Face, etc.)</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | Agent, Graph           | Einige <br><sup><sub>(z.B. Semantic Search)</sub></sup>                     | Einige <br><sup><sub>(z.B. PostgresStore, SqliteSaver, etc.) </sub></sup>        | 37K           | +51MB                      |
| AutoGen    | Agent                | Einige <br><sup><sub>(z.B. Tool Agent, Chat Agent)</sub></sup>              | Viele <sup><sub>[Optional]<br> (z.B. OpenAI, Pinecone, etc.)</sub></sup>        | 7K <br><sup><sub>(nur Kern)</sub></sup>    | +26MB <br><sup><sub>(nur Kern)</sub></sup>          |
| **PocketFlow** | **Graph**                    | **Keine**                                                 | **Keine**                                                  | **100**       | **+56KB**                  |
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342

## Beispiel-Ausgabe

Wenn Sie den Übersetzungsvorgang ausführen, sehen Sie eine Ausgabe, die diesem ähnelt:

```
Übersetzt chinesischer Text
Übersetzt spanischer Text
Übersetzt japanischer Text
Übersetzt deutscher Text
Übersetzt russischer Text
Übersetzt portugiesischer Text
Übersetzt französischer Text
Übersetzt koreanischer Text
Übersetzung gespeichert in translations/README_CHINESE.md
Übersetzung gespeichert in translations/README_SPANISH.md
Übersetzung gespeichert in translations/README_JAPANESE.md
Übersetzung gespeichert in translations/README_GERMAN.md
Übersetzung gespeichert in translations/README_RUSSIAN.md
Übersetzung gespeichert in translations/README_PORTUGUESE.md
Übersetzung gespeichert in translations/README_FRENCH.md
Übersetzung gespeichert in translations/README_KOREAN.md

<<<<<<< HEAD
=== Übersetzung abgeschlossen ===
Übersetzungen gespeichert in: translations
============================
```

## Dateien
=======
Von dort aus ist es einfach, beliebte Designmuster wie ([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agenten](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html), etc. zu implementieren.
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ Hier sind grundlegende Tutorials:

<div align="center">
  
|  Name  | Schwierigkeit    |  Beschreibung  |  
| :-------------:  | :-------------: | :--------------------- |  
| [Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <br> *Anfänger*   | Ein einfacher Chatbot mit Gesprächsverlauf |
| [Strukturierte Ausgabe](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <br> *Anfänger* | Extraktion strukturierter Daten aus Lebensläufen durch Prompting |
| [Workflow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <br> *Anfänger*   | Ein Schreib-Workflow, der gliedert, Inhalte schreibt und Formatierungen anwendet |
| [Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <br> *Anfänger*   | Ein Recherche-Agent, der im Web suchen und Fragen beantworten kann |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <br> *Anfänger*   | Ein einfacher Abrufsaugmentierter Generierungsprozess |
| [Batch](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <br> *Anfänger* | Ein Batch-Prozessor, der Markdown-Inhalte in mehrere Sprachen übersetzt |
| [Streaming](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <br> *Anfänger*   | Eine Echtzeit-LLM-Streaming-Demo mit Benutzer-Unterbrechungsfunktion |
| [Chat-Leitplanke](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <br> *Anfänger*  | Ein Reiseberater-Chatbot, der nur reisebezogene Anfragen verarbeitet |
| [Map-Reduce](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ★☆☆ <br> *Einsteiger* | Ein Lebenslauf-Qualifikationsprozessor, der das Map-Reduce-Muster für Batch-Auswertungen verwendet |
| [Multi-Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <br> *Einsteiger* | Ein Tabu-Wortspiel für asynchrone Kommunikation zwischen zwei Agenten |
| [Supervisor](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <br> *Einsteiger* | Forschungsagent wird unzuverlässig... Bauen wir einen Überwachungsprozess auf|
| [Parallel](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) | ★☆☆ <br> *Einsteiger*   | Eine parallele Ausführungsdemo, die 3-fache Beschleunigung zeigt |
| [Paralleler Flow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <br> *Einsteiger*   | Eine parallele Bildverarbeitungsdemo, die 8-fache Beschleunigung mit mehreren Filtern zeigt |
| [Mehrheitswahl](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ★☆☆ <br> *Einsteiger* | Verbesserte Schlussfolgerungsgenauigkeit durch Aggregation mehrerer Lösungsversuche |
| [Denken](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) | ★☆☆ <br> *Einsteiger*   | Lösen komplexer Schlussfolgerungsprobleme durch Chain-of-Thought |
| [Gedächtnis](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) | ★☆☆ <br> *Einsteiger* | Ein Chatbot mit Kurz- und Langzeitgedächtnis |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) | ★☆☆ <br> *Einsteiger* | Konvertierung natürlicher Sprache in SQL-Abfragen mit Auto-Debug-Schleife |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) | ★☆☆ <br> *Einsteiger* |  Agent mit Model Context Protocol für numerische Operationen |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) | ★☆☆ <br> *Einsteiger* | Agent mit Agent-to-Agent-Protokoll für Inter-Agenten-Kommunikation |
| [Web HITL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-web-hitl) | ★☆☆ <br> *Einsteiger* | Ein minimaler Webdienst für eine menschliche Überprüfungsschleife mit SSE-Updates |
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342

- [`main.py`](./main.py): Implementierung des Batch-Übersetzungs-Knotens
- [`utils.py`](./utils.py): Einfache Wrapper für den Aufruf des Anthropics-Modells
- [`requirements.txt`](./requirements.txt): Projektabhängigkeiten

<<<<<<< HEAD
Die Übersetzungen werden im Verzeichnis `translations` gespeichert, wobei jede Datei nach der ZielSprache benannt ist.
=======
👀 Möchten Sie andere Tutorials für Anfänger sehen? [Erstellen Sie ein Issue!](https://github.com/The-Pocket/PocketFlow/issues/new)

## Wie verwendet man Pocket Flow?

🚀 Durch **Agenten-basiertes Programmieren**—das schnellste LLM-App-Entwicklungsparadigma, bei dem *Menschen entwerfen* und *Agenten programmieren*!

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ Hier sind Beispiele für komplexere LLM-Apps:

<div align="center">
  
|  App-Name     |  Schwierigkeit    | Themen  | Menschlicher Entwurf | Agent-Code |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [Cursor mit Cursor bauen](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>Wir werden bald die Singularität erreichen ...</sup></sub> | ★★★ <br> *Fortgeschritten*   | [Agent](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Design-Dokument](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [Codebase-Wissensgenerator](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>Das Leben ist zu kurz, um ratlos fremden Code anzustarren</sup></sub> |  ★★☆ <br> *Mittel* | [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [Design-Dokument](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [Frage KI Paul Graham](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>Frage KI Paul Graham, falls du nicht reinkommst</sup></sub> | ★★☆ <br> *Mittel*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [Design-Dokument](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [Youtube-Zusammenfasser](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub> Erklärt YouTube-Videos so, als wärst du 5 </sup></sub> | ★☆☆ <br> *Einsteiger*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [Design-Dokument](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [Cold-Opener-Generator](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub> Sofortige Eisbrecher, die kalte Leads heiß machen </sup></sub> | ★☆☆ <br> *Einsteiger*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [Web-Suche](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [Design-Dokument](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)

</div>

- Möchten Sie **Agenten-basiertes Programmieren** lernen?

  - Schauen Sie sich [meinen YouTube-Kanal](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1) für Video-Tutorials an, wie einige der oben genannten Apps erstellt wurden!

  - Möchten Sie Ihre eigene LLM-App erstellen? Lesen Sie diesen [Beitrag](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)! Beginnen Sie mit [dieser Vorlage](https://github.com/The-Pocket/PocketFlow-Template-Python)!
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342
