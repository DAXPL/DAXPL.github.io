---
title: "Zero-Trust AI: Bezpieczeństwo wrażliwych danych i lokalne LLM (OCETA Lounge 2026)"
date: 2026-06-18
summary: "Wykład na OCETA Lounge poświęcony architekturze Zero-Trust AI – przetwarzaniu wrażliwych danych telemetrycznych i biometrycznych wyłącznie lokalnie przy użyciu Ollama i otwartych modeli LLM."
tags: ["Konferencja", "AI", "Ollama", "Security", "LLM", "Prelekcja", "Zero-Trust"]
categories: ["Wpisy & Relacje", "Prelekcje & Wystąpienia"]
---

Podczas spotkania **OCETA Lounge 2026** wygłosiłem prezentację zatytułowaną **"Zero-Trust AI: Securing Sensitive Data Through Local-Only Processing"**.

Wystąpienie skupiało się na skrzyżowaniu dwóch dynamicznie rozwijających się dziedzin: pozyskiwania wysoce intymnych danych telemetrycznych i biometrycznych w systemach XR oraz wykorzystywania lokalnych modeli sztucznej inteligencji w paradygmacie *Zero-Trust*.

---

## Główne Zagadnienia

### 1. Wrażliwość danych immersyjnych i biometrycznych
Współczesne zestawy XR oraz powiązane z nimi sensory biometryczne (tętno, aktywność elektrodermalna, ruchy gałek ocznych, mimika) rejestrują najbardziej prywatne sygnały ludzkiego organizmu. Wysyłanie tych strumieni danych do chmurowych API niesie ze sobą ogromne ryzyko naruszenia prywatności użytkownika.

### 2. Architektura Zero-Trust w ekosystemie AI
Zasada „nigdy nie ufaj, zawsze weryfikuj” w kontekście sztucznej inteligencji oznacza, że żadne nieprzetworzone dane personalne ani surowa telemetria nie powinny opuszczać granic urządzenia użytkownika.

Zaprezentowałem architekturę opartą o:
* Uruchamianie zoptymalizowanych, otwartych modeli językowych i wizyjnych w całości lokalnie za pomocą narzędzi takich jak **Ollama**.
* Wykorzystanie lokalnych interfejsów API do analizy nastroju, kontekstu rozgrywki i wspomagania użytkownika bez dostępu do Internetu.
* Połączenie modeli lokalnych ze środowiskami wirtualnymi (Unity) poprzez bezpieczne lokalne gniazda sieciowe.

### 3. Wnioski dla twórców aplikacji
Twórcy oprogramowania nie muszą wybierać między inteligencją aplikacji a prywatnością użytkownika. Dzisiejsza moc obliczeniowa lokalnych układów graficznych i procesorów NPU pozwala na wdrażanie zaawansowanych funkcji AI przy jednoczesnym zagwarantowaniu, że dane użytkownika pozostają wyłącznie w jego rękach.

