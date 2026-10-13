# Validação Travelmate — GHSA-p35r-3323-6g7g

**Data:** 2026-10-13  
**Severidade publicada:** High (CVSS 7.5)  
**Feed packages da tag OpenWrt v25.12.5:** `5caa62e0bc9f7fb9b0c12a23267bceb7724214dd`  
**Feed LuCI da tag OpenWrt v25.12.5:** `128a7812f4be233c5dd7f7466f534fd888785caf`

## Risco descrito

O advisory descreve que uma sessão autenticada com ACL de escrita da aplicação LuCI Travelmate pode escrever opções UCI `script` e `script_args`. A versão vulnerável do serviço root executava um caminho controlado pelo UCI sem impor no backend a mesma allowlist que a interface gráfica apresentava. Em condições específicas de uplink ativo e ramo de auto-login de captive portal, isto permitia execução de comandos como root.

## Evidência da correção na feed pinada

- [Makefile Travelmate no feed packages pinado](https://github.com/openwrt/packages/blob/5caa62e0bc9f7fb9b0c12a23267bceb7724214dd/net/travelmate/Makefile), blob SHA `71ca99568bc5377365350ad28d7b6feca0ee95ff`, declara `PKG_VERSION=2.4.6` e `PKG_RELEASE=2`.
- [travelmate-functions.sh no mesmo feed](https://github.com/openwrt/packages/blob/5caa62e0bc9f7fb9b0c12a23267bceb7724214dd/net/travelmate/files/travelmate-functions.sh), blob SHA `b72e891632c7cbd0cf6f179f7b4c296eb700f157`, canonicaliza o caminho com `readlink -f`, impõe um `case` que aceita apenas `/etc/travelmate/*.login` e rejeita os restantes caminhos antes de executar. A execução requer ainda que o alvo seja ficheiro e executável.
- A ACL LuCI continua a permitir escrita de UCI para a configuração `travelmate`, pelo que a mitigação relevante tem de existir no serviço/backend, não apenas no formulário web. O código pinado contém essa validação server-side.

## Conclusão

A revisão confirma que o pacote Travelmate selecionado pelo feed packages fixado em OpenWrt `v25.12.5` inclui validação server-side do caminho do script, impedindo que o valor UCI seja diretamente `/bin/sh` como no cenário do advisory. Estado documental: `RELEASE_NOTES_AND_PACKAGE_PIN_CONFIRMED`.

**Limites:** não confirma que um router XFI execute esse pacote, que a aplicação esteja instalada, nem a configuração real de uplinks/ACLs. Não foram executados PoCs, builds ou testes físicos. Zabbix continua em pausa.

## Fontes primárias

- https://github.com/openwrt/openwrt/blob/v25.12.5/feeds.conf.default
- https://github.com/openwrt/packages/blob/5caa62e0bc9f7fb9b0c12a23267bceb7724214dd/net/travelmate/Makefile
- https://github.com/openwrt/packages/blob/5caa62e0bc9f7fb9b0c12a23267bceb7724214dd/net/travelmate/files/travelmate-functions.sh
- https://github.com/openwrt/luci/security/advisories/GHSA-p35r-3323-6g7g
- https://openwrt.org/releases/25.12/notes-25.12.5
