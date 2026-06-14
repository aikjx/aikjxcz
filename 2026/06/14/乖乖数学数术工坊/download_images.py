import os
import re
import requests

def extract_image_urls(html_file):
    """从 HTML 文件中提取所有图片链接"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>'
    urls = re.findall(pattern, content)
    
    print(f"找到 {len(urls)} 张图片链接:")
    for i, url in enumerate(urls, 1):
        print(f"  {i}. {url}")
    
    return urls

def download_images(urls, save_dir):
    """下载图片到指定目录"""
    os.makedirs(save_dir, exist_ok=True)
    
    for i, url in enumerate(urls, 1):
        try:
            print(f"\n正在下载图片 {i}/{len(urls)}...")
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            filename = f"image_{i}.jpg"
            filepath = os.path.join(save_dir, filename)
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"  ✓ 已保存: {filename}")
        
        except Exception as e:
            print(f"  ✗ 下载失败: {str(e)}")

if __name__ == '__main__':
    html_file = r"d:\a10\aikjx\code\my_lib\aikjxcz\2026\06\14\乖乖数学数术工坊\html\数术工坊 · 第四卷 橡皮泥江湖（拓扑学）【完整定稿】.html"
    save_dir = r"d:\a10\aikjx\code\my_lib\aikjxcz\2026\06\14\乖乖数学数术工坊\img\第四卷_橡皮泥江湖"
    
    print("=" * 60)
    print("图片下载工具")
    print("=" * 60)
    
    urls = extract_image_urls(html_file)
    
    if not urls:
        print("未找到图片链接")
        exit()
    
    print("\n--- 开始下载 ---")
    download_images(urls, save_dir)
    print("\n--- 下载完成 ---")