# Prenos súboru cez skrytý kanál

Popis varianty:\
Vytvořte klient/server aplikaci, která umožní přenést soubor skrz skrytý kanál, kde data jsou přenášena uvnitř ICMP Echo-Request/Response zpráv. Soubor musí být před přenosem zašifrován, aby nebyl přenášen v textové podobě.

Spuštění aplikace:\
secret -r <file> -s <ip|hostname> [-l]\
-r <file> : specifikace souboru pro přenos\
-s <ip|hostname> : ip adresa/hostname na kterou se má soubor zaslat\
-l : pokud je program spuštěn s tímto parametrem, jedná se o server, který naslouchá příchozím ICMP zprávám a ukládá soubor do stejného adresáře, kde byl spuštěn.

Prostredie
---------

Ubuntu 64bit

