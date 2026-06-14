import os
import re

def fix_csdn_image_links(input_file, output_file):
    """
    修复 Markdown 文件中的图片链接，使其适合 CSDN 发布
    
    Args:
        input_file: 输入 Markdown 文件路径
        output_file: 输出 Markdown 文件路径
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复 CSDN 破坏的图片格式：! `url` 转换为 ![图片](url)
    # 匹配模式：! `url`
    pattern = r'! `(https?://[^`]+)`'
    replacement = r'![图片](\1)'
    content = re.sub(pattern, replacement, content)
    
    # 确保所有图片链接格式正确
    # 匹配完整的图片格式 ![alt](url)
    image_pattern = r'!\[([^\]]*)\]\((https?://[^)]+)\)'
    images = re.findall(image_pattern, content)
    
    print(f"找到 {len(images)} 张图片:")
    for alt, url in images:
        print(f"  - {alt}: {url}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n修复完成！已保存到: {output_file}")

def batch_fix_csdn_files(directory):
    """
    批量修复目录中所有 Markdown 文件
    
    Args:
        directory: 目录路径
    """
    for filename in os.listdir(directory):
        if filename.endswith('.md') and 'CSDN' in filename:
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, filename.replace('.md', '_fixed.md'))
            print(f"\n处理文件: {filename}")
            fix_csdn_image_links(input_path, output_path)

def generate_csdn_ready_version(input_file, output_file):
    """
    生成适合 CSDN 发布的版本，移除 Jekyll 配置并修复图片
    
    Args:
        input_file: 输入 Markdown 文件路径
        output_file: 输出 Markdown 文件路径
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 移除 Jekyll front matter (--- 开头的部分)
    if lines[0].strip() == '---':
        end_idx = 0
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                end_idx = i + 1
                break
        lines = lines[end_idx:]
    
    content = ''.join(lines)
    
    # 确保图片格式正确
    pattern = r'!\[([^\]]*)\]\((https?://[^)]+)\)'
    images = re.findall(pattern, content)
    
    print(f"找到 {len(images)} 张图片")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"CSDN 版本已生成: {output_file}")

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 60)
    print("CSDN 图片链接修复工具")
    print("=" * 60)
    print("\n选项:")
    print("1. 修复单个文件")
    print("2. 批量修复目录中所有 CSDN 文件")
    print("3. 生成 CSDN 发布版本")
    print("4. 退出")
    
    choice = input("\n请输入选项 (1-4): ")
    
    if choice == '1':
        input_file = input("请输入输入文件路径: ")
        output_file = input("请输入输出文件路径: ")
        fix_csdn_image_links(input_file, output_file)
    elif choice == '2':
        batch_fix_csdn_files(current_dir)
    elif choice == '3':
        input_file = input("请输入输入文件路径: ")
        output_file = input("请输入输出文件路径: ")
        generate_csdn_ready_version(input_file, output_file)
    elif choice == '4':
        print("退出程序")
    else:
        print("无效选项")