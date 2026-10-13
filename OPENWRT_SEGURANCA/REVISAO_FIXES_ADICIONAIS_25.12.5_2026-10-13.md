# Revisão complementar dos fixes de segurança — OpenWrt 25.12.5

**Data da revisão:** 2026-10-13  
**Escopo:** correções de segurança adicionais enumeradas nas notas oficiais de OpenWrt 25.12.5, além das cinco CVEs de `odhcpd` já registadas.  
**Estado:** revisão documental de release; não é uma auditoria de imagem binária, nem prova de correção num router XFI.

## Fontes primárias

- [Notas oficiais OpenWrt 25.12.5](https://openwrt.org/releases/25.12/notes-25.12.5)
- [Anúncio oficial de release](https://lists.openwrt.org/pipermail/openwrt-announce/2026-June/000088.html)
- [Releases e tags upstream](https://github.com/openwrt/openwrt/releases)

As notas da release dizem que os itens listados foram corrigidos em 25.12.5. Neste passe, a evidência foi registada ao nível das notas de release; **não foram ainda confirmados os pins individuais de todos os pacotes, os commits de cada advisory em cada tag, nem a presença de cada componente numa imagem específica**.

## Correções adicionais registadas no CSV

| Componente | Identificador | Achado resumido | Condição / relevância operacional | Estado XFI |
|---|---|---|---|---|
| `odhcpd` | GHSA-qvg7-9jf5-wgjc (sem CVE nas notas) | NDP relay aceita Neighbor Solicitation IPv6 com hop limit diferente de 255 | Só relevante se o relay NDP estiver ativado; potencial spoofing de vizinhança/DoS | Nota da release registada; pin pendente |
| `odhcpd` + LuCI | GHSA-hhmc-92hw-535f | XSS persistente via hostname FQDN construído por cliente DHCPv6 | Cliente não autenticado pode injetar linhas no ficheiro de leases; verificar LuCI e versões dos pacotes | Nota da release registada; pins pendentes |
| `uhttpd` | CVE-2026-55612 / GHSA-p55c-rmhc-qfm5 | HTTP request smuggling: estado do comprimento de chunk inválido | Confirmar versão do servidor e exposição dos endpoints HTTP | Nota da release registada; pin pendente |
| `uhttpd` | CVE-2026-55614 / GHSA-mcfg-c4r7-pjpf | HTTP request smuggling: comparação sensível a maiúsculas/minúsculas de Transfer-Encoding | Confirmar versão e exposição HTTP | Nota da release registada; pin pendente |
| `uhttpd` | CVE-2026-55613 / GHSA-wgwp-64hh-f52p | Dessincronização após erro de parsing do corpo POST ubus | Confirmar versão e caminho afetado | Nota da release registada; pin pendente |
| `cgi-io` | GHSA-jw5r-xhf5-2xcq | Bypass de ACL/path traversal com leitura de ficheiros legíveis por root | Requer contexto de cgi-io/LuCI e conta autenticada com permissão wildcard de leitura | Nota da release registada; pin e ACLs pendentes |
| `ead` | CVE-2026-55490 / GHSA-9558-77jp-g3fw | Underflow inteiro com DoS pré-autenticação | Confirmar presença/estado do serviço e versão do pacote | Nota da release registada; pin pendente |
| `umdns` | CVE-2026-55492 / GHSA-jg8f-fhfw-jg46 | Cache mDNS sem limite pode esgotar heap/memória | Atacante no segmento local; confirmar serviço e alcance de rede | Nota da release registada; pin pendente |

## Outros itens da lista oficial que exigem decomposição por pacote/advisory

As notas 25.12.5 também enumeram correções em módulos/aplicações LuCI e dependências centrais. Não devem ser tratados como um único risco homogéneo:

- **LuCI:** `luci-app-tailscale-community` (injeção de comandos; GHSA-xwc5-mx58-rh35), `luci-app-advanced-reboot` (CVE-2026-55897), `luci-app-adblock-fast` (CVE-2026-55159), `luci-app-samba4` (GHSA-vx64-mmp7-h36c), `luci-app-travelmate` (GHSA-p35r-3323-6g7g), `luci-app-upnp` (GHSA-8v49-6387-7f89), `luci-mod-network/luci-mod-status` (GHSA-686p-p8p9-x6fh) e `luci-app-banip` (GHSA-r6hx-4f83-vp8m). A aplicabilidade depende da aplicação instalada e, em vários casos, de contas/ACLs delegadas.
- **Kernel Linux:** a release atualiza para 6.12.94 e inclui correções upstream de 6.12.88–6.12.94, incluindo CVE-2026-43500. É necessário confirmar a versão de kernel do alvo e a composição da imagem.
- **OpenSSL:** atualização para 3.5.7; as notas enumeram CVEs 2026-7383, 2026-9076, 2026-34180–34183, 2026-42764, 2026-42766–42770 e 2026-45445–45447. O pacote e o pin devem ser verificados na tag/build.
- **musl:** backports para CVE-2026-6042 e CVE-2026-40200.
- **Dropbear:** correções upstream de 2026.90/2026.91, incluindo CVE-2019-6111 (relevante ao cliente SCP) e CVE-2026-35385.
- **Outros componentes:** rpcd, ubus, uhttpd, umdns, uclient, fstools e scripts de Wi-Fi receberam atualizações de robustez/hardening; requerem comparação com o changelog completo para determinar alterações específicas e aplicabilidade.

## Método e limitações

1. As notas da release são tratadas como evidência de que o projeto declara as correções na release 25.12.5.
2. O CSV marca os novos registos como `RELEASE_NOTE_RECORDED_PIN_PENDING`: isto não equivale a validar os pins do pacote.
3. Para fechar cada item é necessário consultar o advisory individual, extrair intervalo afetado e commit de correção, inspecionar o Makefile na tag `v25.12.5` e confirmar `PKG_SOURCE_VERSION`/versão do pacote.
4. A aplicação a um router depende do modelo/revisão, alvo, imagem instalada, pacote presente, configuração e superfície de rede.
5. Não foram feitas alterações em routers, testes PoC, mudanças na instância Zabbix ou homologação de hardware. **Zabbix continua em pausa.**

## Próximos passos

1. Decompor primeiro os advisories de `uhttpd`, `cgi-io`, `umdns` e `ead`, inspecionando pins na tag 25.12.5.
2. Depois rever as aplicações LuCI, priorizando componentes que estejam instalados e permissões delegadas.
3. Rever os pins de kernel, OpenSSL, musl e Dropbear e documentar os CVEs agregados sem os confundir com CVEs individuais.
4. Quando existir inventário de hardware, cruzar os resultados com imagem e pacote realmente instalados.



## Validação adicional do pin uhttpd na tag v25.12.5

Foi consultado o Makefile oficial [uhttpd na tag v25.12.5](https://github.com/openwrt/openwrt/blob/v25.12.5/package/network/services/uhttpd/Makefile):

- Blob SHA do Makefile: `915baa07ab9a0cb44f6819d9d09bc2c001ed2eb7`.
- `PKG_SOURCE_DATE=2026-06-16`.
- `PKG_SOURCE_VERSION=7b1bec45826bd78c8afc993435bdc0f1df2fe399`.
- O commit pinado é três commits à frente do commit `1b624f8f814ed568608d756512892416e0431d77` citado como limiar corrigido nas páginas dos advisories; a comparação upstream confirmou relação de ancestralidade e três commits adicionais.
- As notas da release enumeram CVE-2026-55612, CVE-2026-55614 e CVE-2026-55613 como corrigidas. Para estes três registos, o estado passou a `RELEASE_NOTES_AND_PACKAGE_PIN_CONFIRMED`.
- **Limite:** isto confirma a declaração da release e o pin do pacote-fonte na tag, não que um router XFI específico esteja a executar essa imagem/pacote.
- Makefile e commits consultados são evidência upstream; não foi compilada nem testada uma imagem.


## Validação de pins adicionais — 2026-10-13

### umdns — pin confirmado

- Makefile na tag `v25.12.5`: [package/network/services/umdns/Makefile](https://github.com/openwrt/openwrt/blob/v25.12.5/package/network/services/umdns/Makefile).
- Blob SHA: `40ee5ed4922e14b72a90100ac43994f20288574e`.
- `PKG_SOURCE_DATE=2026-06-16`.
- `PKG_SOURCE_VERSION=1b5e7bf1cec775b89f1a6068dc0b9df3593b5986`.
- O commit upstream `5b2c8f4ff94ef7c339586c8a59a684009f1b7194` associa explicitamente este pin à correção GHSA-jg8f-fhfw-jg46: limite da cache e limitação de TTLs hostis.
- Estado documental: `RELEASE_NOTES_AND_PACKAGE_PIN_CONFIRMED`; pacote instalado no router ainda não verificado.

### ead — correção presente no código da tag

- A release 25.12.5 inclui CVE-2026-55490 nas notas oficiais.
- O ficheiro [ead.c na tag v25.12.5](https://github.com/openwrt/openwrt/blob/v25.12.5/package/network/services/ead/src/ead.c) valida o comprimento da mensagem em aritmética sem sinal antes da subtração, evitando o underflow descrito no advisory.
- O advisory continua a apresentar “Patched versions: None”, pelo que o relatório distingue o metadado do advisory da evidência do código/tag.
- Estado documental: `RELEASE_NOTES_AND_TAGGED_SOURCE_CONFIRMED`; aplicabilidade depende de EAD estar presente/ativo e do estado real da imagem.

### cgi-io — identificação a corrigir no CSV

- A página oficial [GHSA-jw5r-xhf5-2xcq](https://github.com/openwrt/openwrt/security/advisories/GHSA-jw5r-xhf5-2xcq) identifica a vulnerabilidade como **CVE-2026-62947** e indica versões afetadas até OpenWrt 25.12.4.
- O registo CSV continua com o identificador GHSA como chave primária e mantém o estado `RELEASE_NOTE_RECORDED_PIN_PENDING`; a atualização automática do campo identificador foi bloqueada pelo controlo de escrita, pelo que a correção de normalização fica explicitamente pendente.
- A release note não substitui a verificação do pin do pacote cgi-io no feed congelado para v25.12.5. Não declarar o pin confirmado até encontrar e inspecionar o Makefile/feed correspondente.

## Limites

As confirmações acima são de notas oficiais e código-fonte/tag. Não foram construídas imagens nem inspecionados routers XFI. Zabbix continua em pausa.
