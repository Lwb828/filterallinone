import os
import datetime
import pytz

def  merge_whitelist(dns_file="ziyongdns", whitelist_file="whitelist.txt"):

    try:
        with open(whitelist_file, 'r', encoding='utf-8') as f:
            whitelist = [line.strip() for line in f if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        print(f"错误：找不到白名单文件 {whitelist_file}")
        return
    except Exception as e:
        print(f"读取白名单文件时发生错误: {e}")
        return

    try:
        with open(dns_file, 'r', encoding='utf-8') as f:
            ziyongdns_rules = [line.strip() for line in f if line.strip()] #读取并去除空行
    except FileNotFoundError:
        print(f"错误：找不到 ziyongdns 文件 {dns_file}")
        return
    except Exception as e:
        print(f"读取 ziyongdns 文件时发生错误: {e}")
        return

    updated_ziyongdns = ziyongdns_rules[:] # 创建一个副本，避免直接修改原列表

    for white_rule in whitelist:
        if "$" in white_rule:
            if white_rule not in updated_ziyongdns:  # 避免重复添加
                 updated_ziyongdns.append(white_rule)
            
        else:
            domain = white_rule.replace('@', '').replace('|', '').replace('*', '').replace('\^', '')
            if domain:
                hasDel = False
                for i in reversed(range(len(updated_ziyongdns))): #倒序遍历，避免删除元素后索引错位
                    if domain in updated_ziyongdns[i] and updated_ziyongdns[i].startswith('||'):
                        hasDel = True
                        del updated_ziyongdns[i]       
                if (!hasDel):
                    updated_ziyongdns.append(white_rule)         

    try:
        with open(dns_file, 'w', encoding='utf-8') as f:
            for rule in updated_ziyongdns:
                f.write(rule + '\n')

        print(f"成功更新了 ziyongdns 文件: {dns_file}")
    except Exception as e:
        print(f"写入 ziyongdns 文件时发生错误: {e}")

if __name__ == "__main__":
    merge_whitelist()