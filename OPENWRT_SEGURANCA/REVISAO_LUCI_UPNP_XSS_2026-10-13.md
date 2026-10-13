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


## Resultado da análise de proveniência — 2026-10-13

**O caminho de dados está agora identificado; o estado passa de contexto pendente para possível correção incompleta no código fixado.**

1. O backend `luci.upnp` da mesma feed fixa lê o ficheiro de leases `upnp_lease_file` e extrai `record[5]` para `lease.description` (linhas 24–38; blob SHA `f72b57b7ba84188b9b78854bf7ad0711394a0045`).
2. O backend associa essa descrição às regras ativas através de endereço/portas e devolve `{ rules }` via ubus (linhas 89–111). Logo, `rule.descr` não é necessariamente texto estático: pode vir da descrição de um mapeamento UPnP criada por cliente da LAN.
3. Na vista principal, a tabela criada em `render()` passa `rule.descr` sem escaping na linha 118 para `cbi_update_table()`. O componente `L.ui.Table.update()` passa a string como filho de `E('td', ...)`; a função `E` atribui uma string não-Node a `innerHTML`. Portanto, este caminho inicial pode interpretar HTML controlado pelo cliente.
4. A atualização periódica na mesma vista usa `'%h'.format(rule.descr)` (linha 68), mas isso não elimina a exposição no render inicial. A correção observada parece incompleta para este caminho.

### Estado e ação

- Estado atualizado para **`FIX_INCOMPLETE_SOURCE_PATH_REMAINS`**: o pin de código analisado mantém um caminho de renderização sem escaping para a descrição UPnP.
- Tratar como possível vulnerabilidade persistente na vista LuCI principal, apesar da afirmação de correção nas notas da release. Antes de declarar um alvo vulnerável, confirmar se a versão binária instalada corresponde ao pin e se UPnP está ativo.
- A mitigação de código a propor é aplicar `'%h'.format(rule.descr)` também à linha 118 (ou passar um nó de texto seguro), e testar ambos os caminhos: render inicial e atualização periódica. Nenhuma alteração foi feita no upstream nem em routers XFI.
- Fontes do caminho: [backend ucode](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-upnp/root/usr/share/rpcd/ucode/luci.upnp), [vista UPnP](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-upnp/htdocs/luci-static/resources/view/upnp/upnp.js), [implementação de cbi_update_table](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/modules/luci-base/htdocs/luci-static/resources/cbi.js), [implementação da tabela](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/modules/luci-base/htdocs/luci-static/resources/ui.js), [primitiva DOM E](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/modules/luci-base/htdocs/luci-static/resources/luci.js).
