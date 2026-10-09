import os
from PIL import Image
import sys

def process_images(source_dir, target_dir, max_width=800, quality=75):
    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):
        relative_path = os.path.relpath(root, source_dir)
        if relative_path == '.':
            target_subdir = target_dir
        else:
            target_subdir = os.path.join(target_dir, relative_path)
        if not os.path.exists(target_subdir):
            os.makedirs(target_subdir)

        for file in files:
            if file.lower().endswith(supported_extensions):
                source_path = os.path.join(root, file)
                base_filename = os.path.splitext(file)[0]
                target_filename = f"{base_filename}.webp"
                target_path = os.path.join(target_subdir, target_filename)

                try:
                    with Image.open(source_path) as img:
                        if img.mode == 'P' or img.mode == 'LA':
                            img = img.convert('RGBA')
                        elif img.mode == 'CMYK':
                            img = img.convert('RGB')
                        elif img.mode == 'RGBA' and not target_path.lower().endswith('.png'):
                             pass
                        elif img.mode != 'RGB' and img.mode != 'RGBA':
                             img = img.convert('RGB')

                        if img.width > max_width:
                            ratio = max_width / float(img.width)
                            new_height = int(float(img.height) * ratio)
                            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

                        img.save(target_path, 'WEBP', quality=quality)
                        print(f"SKOMPRESOWANO: {source_path} -> {target_path}")

                except Exception as e:
                    print(f"BŁĄD: Nie można przetworzyć {source_path}. Błąd: {e}")

# --- Uruchomienie skryptu ---
if __name__ == "__main__":
    #source_folder = input("Podaj ścieżkę do folderu z obrazami: ")
    source_folder = "img/"
    if not os.path.isdir(source_folder):
        print(f"Folder '{source_folder}' nie istnieje.")
        sys.exit(1)
        
    source_folder = source_folder.rstrip('/\\')
    target_folder = f"{source_folder}-compressed"
    
    print(f"Folder źródłowy: {source_folder}")
    print(f"Folder docelowy:  {target_folder}")
    
    process_images(source_folder, target_folder)

    print(f"Obrazy zostały skompresowane i zapisane w '{target_folder}'.")