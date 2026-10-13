# Validação LuCI — luci-app-tailscale-community

**Data:** 2026-10-13  
**Advisory:** [GHSA-xwc5-mx58-rh35](https://github.com/openwrt/luci/security/advisories/GHSA-xwc5-mx58-rh35)  
**Severidade publicada:** Critical, CVSS 9.9  
**Componente:** `luci-app-tailscale-community`  
**Estado XFI:** `RELEASE_NOTES_AND_FEED_PIN_CONFIRMED`

## Risco e condição de aplicabilidade

O advisory descreve injeção de comandos como root na chamada `tailscale.do_login`, causada pela composição de um comando shell com dados controlados pelo utilizador. O cenário depende da aplicação instalada, do Tailscale estar em estado de logout/NeedsLogin e de existir uma conta LuCI delegada com permissão `luci-app-tailscale-community`; não é uma afirmação de execução anónima em qualquer router.

## Cadeia de evidência na tag OpenWrt v25.12.5

1. O ficheiro [`feeds.conf.default` da tag v25.12.5](https://github.com/openwrt/openwrt/blob/v25.12.5/feeds.conf.default) fixa o feed `luci` no commit `128a7812f4be233c5dd7f7466f534fd888785caf`.
2. O ficheiro [`tailscale.uc` nesse commit do feed](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-tailscale-community/root/usr/share/rpcd/ucode/tailscale.uc) tem blob SHA `2a30bdbfbadc285133c25b3d50dd6ae4b5317bf4`.
3. No método `do_login`, a linha 207 usa `popen('/bin/sh -c ' + shell_quote(login_cmd + ' &'), 'r')`, aplicando o quoting à expressão completa passada ao shell exterior. Isto difere do padrão vulnerável descrito no advisory, que colocava o comando dentro de aspas duplas exteriores e permitia expansão de shell em valores controlados.
4. As notas oficiais de [OpenWrt 25.12.5](https://openwrt.org/releases/25.12/notes-25.12.5) enumeram esta vulnerabilidade como corrigida; o advisory identifica o fix do ramo 25.12 como `756692b`.

## Conclusão

A revisão confirma que a árvore do feed LuCI fixada por `v25.12.5` contém a alteração de quoting que corrige o vetor descrito. Estado documental: `RELEASE_NOTES_AND_FEED_PIN_CONFIRMED`.

**Limites:** não confirma se a aplicação está instalada, a versão/binário de uma imagem específica, se há backports/customizações locais ou a existência de contas ACL delegadas num router XFI. Não foi executado PoC nem alterado qualquer equipamento. Zabbix permanece em pausa.

## Fontes primárias

- https://github.com/openwrt/openwrt/blob/v25.12.5/feeds.conf.default
- https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-tailscale-community/root/usr/share/rpcd/ucode/tailscale.uc
- https://github.com/openwrt/luci/security/advisories/GHSA-xwc5-mx58-rh35
- https://openwrt.org/releases/25.12/notes-25.12.5
