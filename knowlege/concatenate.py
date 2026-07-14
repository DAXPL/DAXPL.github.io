from pathlib import Path

def merge_markdown_files(source_dir: str, output_file: str):
    source_path = Path(source_dir)
    output_path = Path(output_file)
    
    # Znajdujemy wszystkie pliki .md w folderze i jego podfolderach
    md_files = list(source_path.rglob("*.md"))
    
    if not md_files:
        print("Nie znaleziono żadnych plików .md we wskazanym katalogu.")
        return

    merged_count = 0

    # Używamy kodowania utf-8, co jest krytyczne przy polskich znakach w CV
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for md_file in md_files:
            # Zabezpieczenie: pomijamy plik wyjściowy, jeśli znajduje się w tym samym folderze
            if md_file.name == output_path.name:
                continue
                
            # Tworzymy relatywną ścieżkę (np. projects/projekt1.md), żeby AI miało kontekst
            relative_path = md_file.relative_to(source_path)
            outfile.write(f"\n\n---\n# ŹRÓDŁO: {relative_path}\n---\n\n")
            
            # Odczytujemy zawartość i dopisujemy do pliku zbiorczego
            with open(md_file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
            
            merged_count += 1
                
    print(f"Sukces! Połączono {merged_count} plików .md w plik: {output_path.name}")

if __name__ == "__main__":
    # Katalog źródłowy (kropka oznacza folder, w którym uruchomiono skrypt)
    KATALOG_ZRODLOWY = "." 
    
    # Nazwa pliku, który zostanie wygenerowany i posłuży jako kontekst dla AI
    PLIK_WYNIKOWY = "root_forge_master.md"
    
    merge_markdown_files(KATALOG_ZRODLOWY, PLIK_WYNIKOWY)