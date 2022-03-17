# Informačný systém - Konference: správa událostí, prezentací a účastníků
[Odkaz](https://kralovicvalkoiis.herokuapp.com)
## Popis varianty:
Úkolem zadání je vytvořit informační systém pro tvorbu událostí a správu účastníků konferencí obsahující prezentace vybraných přednášejících. Každá konference má nějaké označení, pomocí kterého ji její návštěvníci budou moci vhodně odlišit a další vhodné atributy (popis, žánr/oblast zájmu, místo, apod.). Konference se koná v nějaký časový interval, účast stojí nějakou cenu a má nějakou kapacitu návštěvníků. Dále obsahuje libovolný počet místností, v kterých vystoupí dle stanoveného rozpisu přednášející přijatých prezentací. Každá prezentace je charakterizována popisem (název, přednášející, popis, případně tagy, fotka/logo/poster apod...) a má přesně vymezený čas a místnost na konferenci. Uživatelé budou moci informační systém použít jak pro vkládání a správu konferencí, místností, tak pro podávání a schvalování prezentací a rezervaci/nákup vstupenek na konference - a to následujícím způsobem:
### administrátor\

- spravuje uživatele

- má rovněž práva všech následujících rolí

### registrovaný uživatel

- zakládá konference - stane se pořadatelem konference

- spravuje místnosti a obsah konference

- schvaluje přednášející na konference, vytváří časový rozpis přednášek v místnostech (časové kolize ošetřete)

- spravuje rezervace návštěvníků, po úhradě vstupného potvrdí rezervaci a případně vydá vstupenky (pokud je hrazeno na místě)

- registruje své příspěvky na konference (zasílá návrh prezentace - postačí ve formě textu) - stane se přednášejícím na konferenci

- vidí uživatelsky přívětivý rozpis svých přednášek
(pořadatel se může přihlásit na svoji konferenci jako přednášející)

- rezervuje 1 až N vstupenek (zvolte vhodné omezení - např. maximální množství, úhrada v daném intervalu - kontroluje a případně ruší pořadatel) - stane se návštěvníkem konference

- sleduje stav jeho rezervací (provedení úhrady)

- vidí uživatelsky přívětivý rozpis přednášek konference, může si vytvářet osobní rozvrh

### neregistrovaný

- vidí dostupné konference a jejich obsah

- má možnost vhodně vidět, které konference jsou vyprodané (v případě souběžně prováděných rezervací více uživateli a překročení limitu míst je pomalejší uživatel vhodně upozorněn, že jeho registrace nebyla provedena)

- může provést rezervaci 1 až N vstupenek bez registrace: vyžadujte vhodné údaje (má možnost dokončit registraci a stát se návštěvníkem konference)

Prostredie
---------

Ubuntu 64bit

