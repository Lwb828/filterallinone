import os
import datetime
import pytz

def generate_readme(dns_file="ziyongdns", ruler_file="ziyongruler", readme_file="README.md"):
    """
    生成 README.md 文件，包含指定 DNS 和 Ruler 文件的行数。

    Args:
        dns_file: DNS 文件名 (默认为 "ziyongdnsZ")。
        ruler_file: Ruler 文件名 (默认为 "ziyongrulerZ")。
        readme_file: README 文件名 (默认为 "README.md")。
    """

    try:
        with open(dns_file, 'r') as f:
            dns_line_count = sum(1 for _ in f)
    except FileNotFoundError:
        dns_line_count = "File not found"

    try:
        with open(ruler_file, 'r') as f:
            ruler_line_count = sum(1 for _ in f)
    except FileNotFoundError:
        ruler_line_count = "File not found"

    # 获取北京时间
    beijing_timezone = pytz.timezone('Asia/Shanghai')
    beijing_time = datetime.datetime.now(beijing_timezone).strftime("%Y-%m-%d %H:%M:%S")    

    readme_content = f"""
# filterallinone

```
    更新时间: {beijing_time} （北京时间） 

{dns_file}: {dns_line_count} lines
{ruler_file}: {ruler_line_count} lines
```

一个github能用的脚本或者工作流,用于合并Adguard的过滤规则,思路如下:合并自定义的Adguard官方规则,并将其存储在AdguardDNSRuler和Adguardruler,合并列表自定义第三方规则,并将其合并在ziyongdnsZ和ziyongrulerZ,如果AdguardDNSRuler和ziyongdnsZ中有相同规则,则删除ziyongdnsZ中的相同规则,并将规则存储到ziyongdnsZ1中,同理处理Adguardruler和ziyongrulerZ的规则,井存储到ziyongrulerZ1,最后对ziyongdnsZ1和ziyongrulerZ1进行优化,查看ziyongdnsZ1的规则中是否有包含关系的规则,如果有,则删除被包含的规则,并存储到ziyongdns中,同理处理ziyongrulerZ1,然后处理后存储到ziyongruler
    """

    with open(readme_file, 'w') as f:
        f.write(readme_content)

    print(f"README file '{readme_file}' generated successfully.")

if __name__ == "__main__":
    generate_readme()