
# filterallinone

```
    更新时间: 2025-06-26 20:42:12 （北京时间） 

ziyongdns: 264333 lines
ziyongruler: 38205 lines
```

一个github能用的脚本或者工作流,用于合并Adguard的过滤规则,思路如下:合并自定义的Adguard官方规则,并将其存储在AdguardDNSRuler和Adguardruler,合并列表自定义第三方规则,并将其合并在ziyongdnsZ和ziyongrulerZ,如果AdguardDNSRuler和ziyongdnsZ中有相同规则,则删除ziyongdnsZ中的相同规则,并将规则存储到ziyongdnsZ1中,同理处理Adguardruler和ziyongrulerZ的规则,井存储到ziyongrulerZ1,最后对ziyongdnsZ1和ziyongrulerZ1进行优化,查看ziyongdnsZ1的规则中是否有包含关系的规则,如果有,则删除被包含的规则,并存储到ziyongdns中,同理处理ziyongrulerZ1,然后处理后存储到ziyongruler
    