import os
def generate_docs_for_folder(folder_name):
    docs_folder = 'docs'
    folder_path = os.path.join(docs_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Listar archivos .py en la carpeta especificada
    folder_files = [f for f in os.listdir(folder_name) if f.endswith('.py') and not f.startswith('__')]

    # Crear el contenido del archivo .md
    content_lines = [f"# {folder_name.capitalize()} Documentation
"]
    for file in folder_files:
        module_name = file.replace('.py', '')
        content_lines.append(f"::: {folder_name}.{module_name}
")

    # Guardar el archivo .md en la carpeta de documentación
    md_file_path = os.path.join(docs_folder, f"{folder_name}.md")
    with open(md_file_path, 'w') as md_file:
        md_file.write('\n'.join(content_lines))

if __name__ == "__main__":
    folders_to_process = ['modules', 'utils']
    for folder in folders_to_process:
        if os.path.exists(folder):
            generate_docs_for_folder(folder)
