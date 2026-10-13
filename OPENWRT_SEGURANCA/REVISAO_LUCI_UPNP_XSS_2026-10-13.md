# Revisão de segurança LuCI UPnP — GHSA-8v49-6387-7f89

**Data:** 2026-10-13  
**Severidade publicada:** High (CVSS 8.3)  
**Feed LuCI fixada por OpenWrt v25.12.5:** `128a7812f4be233c5dd7f7466f534fd888785caf`  
**Estado XFI:** `SOURCE_PIN_REVIEW_PARTIAL_PENDING_CONTEXT`

## Vulnerabilidade descrita

Um cliente não autenticado na LAN pode enviar uma descrição HTML através de UPnP IGD `AddPortMapping`. O daemon `miniupnpd` armazena a descrição; LuCI obtém o valor e pode renderizá-lo na origem administrativa. O impacto depende de um administrador abrir uma das vistas afetadas e de UPnP estar ativo.

Advisory: https://github.com/openwrt/luci/security/advisories/GHSA-8v49-6387-7f89

## Evidência observada na feed fixada

- [Vista de estado UPnP](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-upnp/htdocs/luci-static/resources/view/status/include/80_upnp.js), blob SHA `3d6b88d065ed8ad6890a2d269bd3703454f206fc`, aplica `'%h'.format(rule.descr)` antes de apresentar a descrição.
- [Vista principal UPnP](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-upnp/htdocs/luci-static/resources/view/upnp/upnp.js), blob SHA `04c870a45e3cfd693a04bd12ebdef2598b9970a3`, também escapa a descrição da tabela de mapas ativos com `'%h'.format(rule.descr)` (linha 68).
- **Ponto pendente:** o mesmo ficheiro tem outra tabela que apresenta `rule.descr` sem `%h` (linha 118). É necessário confirmar a proveniência desse `data[0].rules` e se o valor pode ser controlado pelo cliente UPnP ou se representa apenas regras estáticas de configuração administrativa. Não vou declarar a correção integralmente confirmada enquanto esta diferença não estiver resolvida.
- As notas oficiais da release 25.12.5 dizem que a descrição é agora escapada: https://github.com/openwrt/openwrt/releases e https://openwrt.org/releases/25.12/notes-25.12.5.

## Decisão

O caminho principal de dados de leases/estado está escapado no pin analisado, mas a revisão do código detetou uma utilização adicional de `rule.descr` sem escaping numa tabela de outra origem aparente. Registar como revisão parcial, não como vulnerabilidade confirmada nem como correção integralmente fechada. Próxima ação: traçar a origem de `data[0].rules` e verificar se pode conter uma descrição fornecida por cliente LAN.

## Limites

Não foram enviados pacotes UPnP, executados PoCs, construídas imagens nem alterados routers. A imagem e a configuração efetivas de um router XFI não foram verificadas; Zabbix continua em pausa.
