import requests
import argparse
import re

OFFICIAL_RULES = [
    "https://filters.adtidy.org/android/filters/2_optimized.txt",
    "https://filters.adtidy.org/android/filters/11_optimized.txt",
    "https://filters.adtidy.org/android/filters/17_optimized.txt",
    "https://filters.adtidy.org/android/filters/3_optimized.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&mimetype=plaintext",
    "https://filters.adtidy.org/android/filters/4_optimized.txt",
    "https://filters.adtidy.org/android/filters/18_optimized.txt",
    "https://filters.adtidy.org/android/filters/19_optimized.txt",
    "https://filters.adtidy.org/android/filters/20_optimized.txt",
    "https://filters.adtidy.org/android/filters/21_optimized.txt",
    "https://filters.adtidy.org/android/filters/22_optimized.txt",
    "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt",
    "https://secure.fanboy.co.nz/fanboy-annoyance_ubo.txt",
    "https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AnnoyancesList",
    "https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
    "https://malware-filter.gitlab.io/malware-filter/phishing-filter-ag.txt",
    "https://urlhaus-filter.pages.dev/urlhaus-filter-ag-online.txt",
    "https://filters.adtidy.org/android/filters/224_optimized.txt",
    "https://filters.adtidy.org/android/filters/15_optimized.txt",
    "https://filters.adtidy.org/android/filters/5_optimized.txt",
]

THIRD_PARTY_RULES = [
    "http://rssv.cn/adguard/api.php?type=black",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.plus.txt", # 或者用代理：https://gh-proxy.com/raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.plus.txt
    "https://raw.githubusercontent.com/lingeringsound/10007_auto/master/adb.txt",
    "https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall.txt",
    "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt",
    "https://raw.githubusercontent.com/Noyllopa/NoAppDownload/master/NoAppDownload.txt",
    "https://anti-ad.net/adguard.txt",
    "https://raw.githubusercontent.com/loveqqzj/AdGuard/master/Mobile.txt",
    #"https://raw.githubusercontent.com/qq5460168/dangchu/main/T%E7%99%BD%E5%90%8D%E5%8D%95.txt",
    #"https://raw.githubusercontent.com/user001235/112/main/white.txt",
    #"https://file-git.trli.club/file-hosts/allow/Domains",
    #"https://raw.githubusercontent.com/mphin/AdGuardHomeRules/main/Allowlist.txt",
]

def is_dns_rule(rule):
  """
  检查规则是否为只包含域名的 DNS 过滤规则。

  Args:
    rule: 要检查的规则字符串。

  Returns:
    如果规则是有效的 DNS 规则，则返回 True，否则返回 False。
  """
  # 更严格的域名匹配模式，包括对端口号的可选匹配
  rule = rule.replace('@', '').replace('|', '').replace('*', '')
  pattern = r"^(?!-)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(:[0-9]+)?\^?$"
  return bool(re.match(pattern, rule))

def download_rules(urls, dns_filename, general_filename):
    dns_rules = []
    general_rules = []

    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            rules = response.text.splitlines()

            for rule in rules:
                rule = rule.replace('$important', '')
                if is_dns_rule(rule):
                    dns_rules.append(rule)
                    #print(f"Identified general rule: {rule}")
                else:
                    general_rules.append(rule)
                    #print(f"Identified DNS rule: {rule}")

        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")

    with open(dns_filename, 'w', encoding='utf-8') as f:
        for rule in dns_rules:
            f.write(rule + '\n')

    with open(general_filename, 'w', encoding='utf-8') as f:
        for rule in general_rules:
            f.write(rule + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download AdGuard filter rules.")
    parser.add_argument('--type', choices=['official', 'third_party'], required=True, help='Type of rules to download (official or third_party)')
    args = parser.parse_args()

    if args.type == 'official':
      download_rules(OFFICIAL_RULES, 'AdguardDNSRuler', 'AdguardRuler')
    elif args.type == 'third_party':
      download_rules(THIRD_PARTY_RULES, 'ziyongdnsZ', 'ziyongrulerZ')