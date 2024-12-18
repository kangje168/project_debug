import os

def generate_combined_txt_from_project(output_txt_file):
    """遍历文件夹并生成一个合并的 .txt 文件"""
    project_path = os.getcwd()

    with open(output_txt_file, 'w', encoding='utf-8') as out_f:
        def process_directory(directory_path, indent=""):
            out_f.write(f"{indent}Folder: {os.path.basename(directory_path)}\n")
            out_f.write(f"{indent}Path: {directory_path}\n")

            for root, dirs, files in os.walk(directory_path):
                # 忽略 .venv 目录及其内容
                dirs[:] = [d for d in dirs if d != ".venv"]
                
                for file in files:
                    # 构建文件路径
                    file_path = os.path.join(root, file)
                    file_extension = os.path.splitext(file)[1].lower()

                    # 仅处理代码文件
                    if file_extension in ['.py', '.java', '.php', '.xml', '.json', '.c', '.h']:
                        try:
                            out_f.write(f"{indent}- {file}\n")
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                out_f.write(content + "\n")
                            out_f.write("\n")  # 空行作为分隔
                        except Exception as e:
                            print(f"Error reading file {file_path}: {e}")

        # 处理项目根目录
        process_directory(project_path)

    print(f"Combined TXT saved as {output_txt_file}")

# 使用示例：输出到 combined_project_structure.txt
if __name__ == "__main__":
    output_txt_file = "combined_project_structure.txt"
    generate_combined_txt_from_project(output_txt_file)
