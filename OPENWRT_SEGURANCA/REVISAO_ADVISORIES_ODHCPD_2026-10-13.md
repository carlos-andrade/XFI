# Revisão semântica de advisories odhcpd — 2026-10-13

**Repositório:** XFI  
**Escopo:** cinco advisories citados no anúncio OpenWrt 25.12.5.  
**Estado:** leitura das páginas individuais e registo dos intervalos/commits descritos pelos próprios advisories; **não é homologação de firmware nem prova de correção numa imagem binária específica**.

## Resultado executivo

A revisão identificou commits de correção nas cinco páginas. Em várias páginas, porém, o cabeçalho estruturado ainda mostra **“Patched versions: None”**, enquanto o rodapé lista commits de correção. Por isso, este registo separa explicitamente **commit de correção**, **commit de ramo OpenWrt 25.12** e **tag de release publicada**. A página oficial da release v25.12.5 lista explicitamente as cinco CVEs revistas — CVE-2026-53921, CVE-2026-53918, CVE-2026-53920, CVE-2026-53922 e CVE-2026-55606 — como corrigidas. Assim, o anúncio oficial da release confirma a inclusão da quinta correção, embora a correspondência ao pacote instalado num router específico continue a exigir validação.

| CVE | Severidade publicada | Escopo afetado indicado pela fonte | Correção upstream / ramo 25.12 indicada pela fonte | Estado XFI |
|---|---|---|---|---|
| CVE-2026-53921 | Critical | `<= master (e432dd6)`; versões anteriores que contêm os caminhos de serialização vulneráveis | upstream `d329a15`, `0320032`, `03dacc2`; 25.12 `d168c27`, `6634b7a`, `2a42d34` | Release 25.12.5 lista explicitamente a CVE como corrigida |
| CVE-2026-53918 | High | Pins de OpenWrt 18.06 a 25.12 e master que contêm `a2ffc59`; LEDE 17.01/pré-`a2ffc` não é esperado como afetado por este UAF específico | upstream `26b1220`; 25.12 `5b28383` | Release 25.12.5 lista explicitamente a CVE como corrigida |
| CVE-2026-53920 | High | Releases OpenWrt 17.01.0 a 25.12.3 segundo o mapeamento da fonte | upstream `f2275ef`; 25.12 `719fc3a` | Release 25.12.5 lista explicitamente a CVE como corrigida |
| CVE-2026-53922 | Moderate | `<= cfddd56`; releases que contêm o ramo vulnerável de `build_ia`; master e 25.12.x identificados | upstream `c6792ba`, `d329a15`; 25.12 `d08dbcc`, `d168c27` | Release 25.12.5 lista explicitamente a CVE como corrigida |
| CVE-2026-55606 | Moderate | `<= master (e432dd6)`; advisory descreve targets OpenWrt little-endian | upstream `ed38cff`; 25.12 `6907f28` | Release oficial v25.12.5 lista explicitamente a CVE como corrigida |

## Fontes primárias consultadas

1. [CVE-2026-53921 — DHCPv6 IA reply stack buffer overflow](https://github.com/openwrt/odhcpd/security/advisories/GHSA-7fwx-hhrg-3496) — severidade Critical; lista os três commits upstream e os três commits do ramo 25.12.
2. [CVE-2026-53918 — DHCPv6 IA use-after-free](https://github.com/openwrt/odhcpd/security/advisories/GHSA-44ff-jcwh-wgc2) — severidade High; mapeia os pins dos ramos OpenWrt e lista os commits de correção.
3. [CVE-2026-53920 — DHCPv6 IA stack memory disclosure](https://github.com/openwrt/odhcpd/security/advisories/GHSA-p769-5v73-pc4f) — severidade High; indica releases afetadas até 25.12.3 e commits de correção, mas refere que não identificou tag fixa.
4. [CVE-2026-53922 — DHCPv6 IA pre-auth denial of service](https://github.com/openwrt/odhcpd/security/advisories/GHSA-7hcw-g2jh-pqv5) — severidade Moderate; descreve os commits de correção upstream e do ramo 25.12.
5. [CVE-2026-55606 — DUID length endianness mismatch](https://github.com/openwrt/odhcpd/security/advisories/GHSA-x8x4-7gvf-gp45) — severidade Moderate; descreve os commits de correção upstream e do ramo 25.12.
6. [Notas oficiais das releases OpenWrt](https://github.com/openwrt/openwrt/releases) — a entrada v25.12.5 lista as cinco CVEs desta revisão entre as correções de odhcpd. O anúncio por email serve como fonte complementar da release.

## Interpretação técnica e limites

- Os advisories tratam vulnerabilidades no componente **odhcpd**, principalmente em caminhos DHCPv6. A aplicabilidade operacional depende de o pacote existir na imagem, da versão/commit do pacote, da configuração do serviço e da interface alcançável.
- “Commit de correção no ramo 25.12” não é, isoladamente, prova de que uma imagem específica instalada contém a correção.
- A release v25.12.5 lista explicitamente as cinco CVEs revistas, incluindo CVE-2026-55606. Isto confirma a correção declarada pela release; não prova, por si só, que uma imagem instalada num router XFI contenha esse pacote corrigido.
- Os campos “Patched versions: None” no topo de várias páginas parecem coexistir com referências a commits fixos no rodapé. O registo conserva essa discrepância em vez de a ocultar.
- Não foi feita correspondência a routers XFI: não há inventário confirmado com modelo, revisão de hardware, imagem, versão de firmware, pacote odhcpd e configuração efetiva.
- Não foi executado qualquer PoC contra router de produção, nem é necessário fazê-lo para este trabalho documental.
- Não se deve concluir que todos os routers OpenWrt estão vulneráveis, nem que um firmware está corrigido, sem a correspondência entre advisory, pacote, tag de release, imagem e configuração real.

## Próximas ações

1. Confirmar, nas tags de release oficiais, se cada commit de correção está incluído na versão de OpenWrt considerada para implantação.
2. Verificar o `PKG_SOURCE_VERSION` do pacote `odhcpd` nas tags relevantes e registar evidência por release.
3. Repetir o mesmo método para outros fixes citados nas notas da release 25.12.5, sem assumir que o índice de advisories é completo.
4. Só após definir modelos/revisões de hardware, cruzar a evidência com a imagem suportada e a configuração DHCPv6 do equipamento.
5. Manter Zabbix em pausa; esta revisão não exige nem autoriza alterações na instância Zabbix.

## Registo de qualidade

A revisão é baseada nas páginas públicas consultadas em 2026-10-13. As versões afetadas e commits acima refletem o texto das fontes upstream; o estado de inclusão em tags de release permanece explicitamente pendente. A verificação de URLs 30/30 é uma evidência separada de acessibilidade HTTP e não valida estes metadados semânticos.
