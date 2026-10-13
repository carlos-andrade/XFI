# Roadmap — OpenWrt Security XFI

**Atualização:** 2026-10-13  
**Percentual preliminar:** 32% — estimativa de planeamento documental; não representa segurança validada nem implantação. Reconciliar com a norma central de status do XFI/GOVERNANCA.  
**Estado:** fundação documental, shortlist técnica/comercial e especificação inicial preparadas; sem hardware inventariado ou testes físicos. **Zabbix em pausa por decisão de 2026-10-13; não avançar nessa frente até nova instrução.**

| Fase | Entregável | Critério de saída | Estado |
|---|---|---|---|
| 1. Fundação | Governança, arquitetura, baseline, fontes e teste | Documentação persistida e revista | DOCUMENTADO |
| 2. Inventário | Modelo de ficha de router e requisitos de cliente | Templates criados; falta preencher com hardware real | EM PREPARAÇÃO |
| 3. Ingestão inicial | Verificador agendado de URLs do catálogo | Workflow passa em execução real e relatório é revisto | **EXECUTADO COM SUCESSO — 20/20 URLs acessíveis** |
| 4. Ingestão ampliada | Releases, advisories, commits e páginas de hardware | Dados normalizados, rastreáveis e revistos | **EXECUTADO COM SUCESSO — 30/30 URLs acessíveis; registo inicial de releases/advisories criado** |
| 5. Perfis | Perfis por classe de cliente e matriz de fluxos | Requisitos e variáveis sem segredos | DOCUMENTADO PRELIMINARMENTE |
| 6. Seleção de hardware | Fabricantes, modelos, critérios, preços públicos e plano de homologação | Shortlist técnica/comercial criada; fontes revistas; critérios testáveis definidos | DOCUMENTADO, NÃO HOMOLOGADO |
| 7. Monitorização Zabbix | Templates, métricas, alertas, inventário, proxies e canal seguro | Todos os routers monitorizados; recolha e alertas testados por modelo | **EM PAUSA — especificação documentada; não implementada** |
| 8. Controlo operacional via Zabbix | Ações autorizadas e runner restrito com auditoria/rollback | Ações críticas protegidas por aprovação, preflight e rollback | **EM PAUSA — não iniciar** |
| 9. Configuração reproduzível | Templates UCI/scripts por versão/hardware | Preflight, validação, diff e rollback | PLANEADO |
| 10. Laboratório | Ambiente isolado e testes automatizados | Matriz IPv4/IPv6, firewall, DNS, Wi-Fi, acesso e desempenho aprovada | PLANEADO |
| 11. Homologação | Fichas de hardware/perfil e evidências | Revisão por pares e risco residual aprovado | PLANEADO |
| 12. Operação, piloto e escala | Telemetria, alertas, inventário, mudanças, incidentes e rollout | Runbooks, rollback, revisão periódica e responsabilidades aprovados | PLANEADO |

## Evidência da primeira execução do verificador

- **Data/hora UTC:** 2026-10-13 10:20:45 (execução GitHub Actions).
- **Workflow:** [XFI — Verificar fontes oficiais OpenWrt](https://github.com/carlos-andrade/XFI/actions/runs/38382664530).
- **Resultado:** sucesso.
- **URLs únicas detetadas:** 20.
- **Acessíveis:** 20.
- **Erros HTTP:** 0.
- **Erros de rede:** 0.
- **Artefacto do relatório:** [openwrt-source-check-report](https://github.com/carlos-andrade/XFI/actions/runs/38382664530/artifacts/11804441572) (retenção de 30 dias, conforme workflow).
- **Interpretação:** o teste confirma acessibilidade HTTP no momento da execução, não valida conteúdo, segurança, atualidade nem adequação técnica das páginas.
- **Aviso não bloqueante:** o runner reportou aviso de depreciação de Node.js 20 em actions usadas pelo workflow; rever as versões dessas actions antes de futura incompatibilidade do runner.

## Evolução da ingestão ampliada — 2026-10-13

- Catálogo expandido com índices de advisories, releases, downloads oficiais, repositório upstream, commits e issues do projeto OpenWrt.
- Verificador atualizado para extrair metadados da tabela do catálogo, deduplicar URLs, aplicar allowlist explícita e produzir relatório JSON por fonte.
- Esquema e limitações documentados em [INGESTAO_FONTES.md](INGESTAO_FONTES.md).
- README atualizado para distinguir o sucesso da versão inicial da validação ainda pendente da versão ampliada.
- **Estado de validação:** a primeira versão comprovou 20/20 URLs acessíveis. A nova execução deve ser confirmada antes de marcar a fase ampliada como validada. O conteúdo técnico ainda requer revisão humana.

## Evidência da execução do catálogo ampliado

- **Workflow:** [execução ampliada do verificador](https://github.com/carlos-andrade/XFI/actions/runs/38384643976).
- **Commit verificado:** `19470db2e473a7d517d0d41fcceac285c503cc8d`.
- **Resultado do job:** sucesso técnico; relatório gerado e artefacto publicado.
- **URLs únicas:** 26.
- **Acessíveis:** 25.
- **Erros HTTP:** 1.
- **Erros de rede:** 0.
- **Artefacto:** [openwrt-source-check-report](https://github.com/carlos-andrade/XFI/actions/runs/38384643976/artifacts/11804753837).
- **Interpretação:** a URL que falhou foi o histórico de commits do GitHub, com HTTP 429 (`Too Many Requests`), consistente com limitação de taxa e não necessariamente com link quebrado.
- **Correção aplicada:** a fonte de commits foi migrada para o repositório Git oficial `git.openwrt.org`; o verificador passou a classificar HTTP 429 separadamente como `rate_limited` e a imprimir as URLs com falha no resumo.
- **Validação após correção:** [execução de 26 URLs](https://github.com/carlos-andrade/XFI/actions/runs/38384970277) com 26/26 acessíveis; a execução mais recente após acrescentar quatro URLs específicas de release/segurança confirmou 30/30 acessíveis, 0 erros HTTP, 0 rate limits e 0 erros de rede.

## Evidência da execução após correção do rate limit

- **Workflow:** [execução validada](https://github.com/carlos-andrade/XFI/actions/runs/38384970277).
- **Commit:** `5ce7e161cf778a412dad0df0343e738a4816f0ce`.
- **URLs únicas:** 26.
- **Acessíveis:** 26.
- **Erros HTTP:** 0.
- **Rate limits:** 0.
- **Erros de rede:** 0.
- **Falhas listadas no resumo:** nenhuma.
- **Artefacto:** [openwrt-source-check-report](https://github.com/carlos-andrade/XFI/actions/runs/38384970277/artifacts/11804872300).
- **Limite:** esta verificação valida acessibilidade no instante da execução, não o conteúdo, segurança ou aplicabilidade técnica.

## Revisão documental de releases e advisories

- Criado [REVISAO_FONTES_OFICIAIS_2026-10-13.md](REVISAO_FONTES_OFICIAIS_2026-10-13.md) com análise inicial de releases estáveis, estado da série antiga e separação entre advisories e notas de release.
- Fontes oficiais consultadas: [OpenWrt homepage](https://openwrt.org/), [Release Builds](https://openwrt.org/releases/start), [advisories](https://openwrt.org/advisory/start), [OpenWrt 25.12.5](https://openwrt.org/releases/25.12/notes-25.12.5) e [histórico](https://openwrt.org/about/history).
- Decisão: monitorizar advisories, anúncios de release e changelogs em paralelo; o índice de advisories não é fonte única.
- A análise é documental e datada; verificar release e suporte de novo antes de comprar, instalar ou homologar.

## Evidência da validação final do catálogo ampliado

- **Workflow:** [execução com 30 URLs](https://github.com/carlos-andrade/XFI/actions/runs/38385191297).
- **Commit verificado:** `96660eea0da69fb23bb82742bc38859b1acf7d3d`.
- **URLs únicas:** 30.
- **Acessíveis:** 30.
- **Erros HTTP / rate limits / erros de rede:** 0 / 0 / 0.
- **Artefacto:** [relatório JSON](https://github.com/carlos-andrade/XFI/actions/runs/38385191297/artifacts/11804862674).
- **Resultado:** a lista de fontes é acessível no instante da verificação; conteúdo e aplicabilidade continuam sujeitos a revisão humana.

## Próximas ações — fora da frente Zabbix

1. **Validar os metadados de advisories e releases** e confirmar versões afetadas/corrigidas nas fontes upstream, sem inferir dados ausentes.
2. **Continuar a diligência de hardware:** verificar SKU e revisão exata, disponibilidade e preço final, garantia, imagem OpenWrt suportada e método de recuperação.
3. **Preparar o inventário inicial** de routers e requisitos por perfil de cliente, sem inventar dados de equipamentos ainda não adquiridos.
4. **Ampliar o registo semântico** de advisories/releases e ligar os registos a modelos e firmware apenas quando houver evidência explícita.
5. **Detalhar perfis de segurança e matriz de fluxos** para os diferentes perfis de cliente.
6. Retomar laboratório, homologação e deployment apenas depois de haver hardware identificado e evidências técnicas adequadas.

### Frente explicitamente em pausa

A implementação do Zabbix — incluindo levantamento da instância, atualização, templates, configuração de hosts, alertas, proxies e automação operacional — fica suspensa até nova instrução do responsável. A documentação existente mantém-se como referência; não realizar alterações na infraestrutura Zabbix enquanto a pausa estiver ativa.

## Limitação de estado
O percentual é apenas progresso documental e de planeamento. Nenhuma unidade física foi instalada, testada ou homologada. O Zabbix ainda não foi configurado para esta frota.

## Revisão semântica dos advisories odhcpd — atualização 2026-10-13

- **Ficheiro:** [REVISAO_ADVISORIES_ODHCPD_2026-10-13.md](REVISAO_ADVISORIES_ODHCPD_2026-10-13.md).
- **Registo normalizado atualizado:** [REGISTO_ADVISORIES_RELEASES.csv](REGISTO_ADVISORIES_RELEASES.csv).
- **Resultado:** as cinco páginas individuais foram consultadas; os commits de correção upstream e os commits do ramo 25.12 foram registados.
- **Qualificação importante:** várias páginas apresentam “Patched versions: None” no cabeçalho, embora listem commits de correção no rodapé. O estado de inclusão dos commits em tags de release específicas permanece pendente e está marcado explicitamente no CSV.
- **Não inferir:** não declarar 25.12.5 ou qualquer outra versão corrigida sem verificar tags/builds e pins do pacote odhcpd. A aplicabilidade a routers XFI continua indeterminada sem modelo/revisão, imagem, versão e configuração reais.
- **Próximo passo técnico:** cruzar os commits com tags oficiais de release e `PKG_SOURCE_VERSION` de odhcpd; só depois relacionar advisories a uma versão de firmware. Zabbix continua em pausa.

### Resultado adicional — cruzamento com notas oficiais de 25.12.5

- As notas oficiais da release 25.12.5 listam explicitamente quatro das cinco CVEs revistas: **CVE-2026-53921, CVE-2026-53918, CVE-2026-53920 e CVE-2026-53922**.
- **CVE-2026-55606** não aparece na lista de correções de odhcpd consultada; embora o advisory indique um commit de correção no ramo 25.12 (`6907f28`), a inclusão na tag 25.12.5 não está confirmada neste momento.
- CSV e relatório foram corrigidos para refletir essa distinção. Não inferir que 25.12.5 resolve a quinta CVE sem verificar a tag e o pin do pacote.

### Correção da conclusão anterior — validação da tag v25.12.5

A conclusão anterior de que CVE-2026-55606 não constava nas notas de v25.12.5 estava incorreta. A revisão direta da entrada **v25.12.5** na página oficial de releases lista explicitamente as cinco CVEs desta revisão, incluindo CVE-2026-55606, como corrigidas.

- Fonte da release: https://github.com/openwrt/openwrt/releases
- Makefile do pacote na tag v25.12.5: https://github.com/openwrt/openwrt/blob/v25.12.5/package/network/services/odhcpd/Makefile
- `PKG_SOURCE_DATE`: `2026-06-29`
- `PKG_SOURCE_VERSION`: `5d7be43f8b9dec0eb47e245cfab81108bb131273`
- Blob SHA do Makefile consultado: `9353be754fefee82f08dff522258d9131c56f3ce`
- **Estado:** as cinco CVEs estão declaradas como corrigidas nas notas oficiais de v25.12.5, e o pin do pacote nessa tag foi identificado. Continua necessário confirmar o modelo/revisão de router, a imagem exata e o pacote efetivamente instalado antes de declarar um equipamento XFI corrigido.


## Revisão complementar de fixes — OpenWrt 25.12.5 (2026-10-13)

- **Fonte primária:** [notas oficiais 25.12.5](https://openwrt.org/releases/25.12/notes-25.12.5).
- **Relatório:** [REVISAO_FIXES_ADICIONAIS_25.12.5_2026-10-13.md](REVISAO_FIXES_ADICIONAIS_25.12.5_2026-10-13.md).
- **Registo normalizado:** oito entradas adicionais foram acrescentadas a `REGISTO_ADVISORIES_RELEASES.csv`: NDP relay/odhcpd, XSS DHCPv6/LuCI, três problemas uhttpd, cgi-io, ead e umdns.
- **Estado de cada entrada:** `RELEASE_NOTE_RECORDED_PIN_PENDING`. A release declara as correções, mas os pins individuais e os intervalos afetados ainda precisam de ser confirmados nos advisories e Makefiles da tag.
- **Outros componentes a decompor:** aplicações LuCI, kernel Linux, OpenSSL, musl, Dropbear e componentes de rede listados no relatório.
- **Limites:** nenhuma imagem binária ou router foi testado; não há conclusão de vulnerabilidade/correção para hardware XFI sem inventário e versão instalada. Zabbix continua em pausa.
- **Próximo passo:** verificar advisories e pins de uhttpd, cgi-io, umdns e ead; depois LuCI e bibliotecas centrais.


### Validação do pin uhttpd — atualização 2026-10-13

- Makefile da tag v25.12.5: `package/network/services/uhttpd/Makefile`; blob SHA `915baa07ab9a0cb44f6819d9d09bc2c001ed2eb7`.
- Pin: `PKG_SOURCE_DATE=2026-06-16`, `PKG_SOURCE_VERSION=7b1bec45826bd78c8afc993435bdc0f1df2fe399`.
- Comparação upstream: o pin está três commits à frente do commit-limiar `1b624f8f814ed568608d756512892416e0431d77`; as notas de 25.12.5 listam as três CVEs uhttpd revistas como corrigidas.
- Os registos CVE-2026-55612, CVE-2026-55614 e CVE-2026-55613 passaram a `RELEASE_NOTES_AND_PACKAGE_PIN_CONFIRMED`.
- **Limite:** o pin é da fonte usada pela tag; não comprova que qualquer router XFI execute a imagem/pacote correspondente.
- Relatório e CSV atualizados; sem compilação, teste de imagem ou alteração de router. Zabbix permanece em pausa.


## Atualização — fecho do pin cgi-io (2026-10-13)

- **Fechado ao nível documental/source pin:** a tag `v25.12.5` fixa o feed packages no commit `5caa62e0bc9f7fb9b0c12a23267bceb7724214dd`; o Makefile de `cgi-io` nesse feed fixa o código-fonte `7314451cb99692c0862a70c3307ee08bd2fbd9c0` (`PKG_SOURCE_DATE=2026-06-28`).
- O `main.c` desse pin canonicaliza o caminho antes da verificação ACL; o baseline afetado `658b14b` fazia a autorização e abertura sobre o caminho não canonicalizado.
- O CSV foi normalizado para **CVE-2026-62947 / GHSA-jw5r-xhf5-2xcq** e estado `RELEASE_NOTES_AND_PACKAGE_PIN_CONFIRMED`.
- **Limite:** ainda não existe verificação da imagem binária nem do pacote instalado num router XFI. Não declarar hardware corrigido sem recolher evidência do equipamento.
- **Próxima prioridade:** continuar a revisão por pacote das restantes correções de LuCI e bibliotecas centrais, preservando a separação entre evidência de release, pin de fonte e evidência de dispositivo.


## Atualização — LuCI Tailscale Community (2026-10-13)

- **Prioridade crítica revista:** GHSA-xwc5-mx58-rh35, CVSS 9.9, injeção de comandos como root através de `tailscale.do_login`.
- A tag OpenWrt `v25.12.5` fixa o feed LuCI no commit `128a7812f4be233c5dd7f7466f534fd888785caf`; o `tailscale.uc` nesse commit usa `shell_quote(login_cmd + ' &')` para o comando completo passado ao shell exterior.
- Registo documental atualizado para `RELEASE_NOTES_AND_FEED_PIN_CONFIRMED`; relatório: [VALIDACAO_LUCI_TAILSCALE_2026-10-13.md](VALIDACAO_LUCI_TAILSCALE_2026-10-13.md).
- A aplicabilidade depende da aplicação instalada, estado do Tailscale e ACLs delegadas. A imagem/dispositivo XFI não foi verificada.
- Próximo: rever as restantes aplicações LuCI listadas nas notas 25.12.5, começando por avançadas/reboot, adblock-fast, samba4 e travelmate.


## Atualização — validação de mais duas correções LuCI (2026-10-13)

- **CVE-2026-55897 / GHSA-vj96-f37g-37f6 — advanced-reboot, High:** a ACL de leitura no feed fixado por `v25.12.5` já não concede `/bin/sh` nem `file.exec`.
- **CVE-2026-55159 / GHSA-ggpf-xrph-wg5v — adblock-fast, High:** o backend no feed fixado usa `syncCron` em vez de `setCronEntry` e valida os campos de agenda antes de escrever o crontab root.
- CSV atualizado com ambos os advisories; relatório: [VALIDACAO_LUCI_ADVANCED_REBOOT_ADBLOCK_FAST_2026-10-13.md](VALIDACAO_LUCI_ADVANCED_REBOOT_ADBLOCK_FAST_2026-10-13.md).
- Confirmação documental/source-pin, não validação de binário ou equipamento. Continuar com Samba4, Travelmate e XSS no estado DHCPv6 do LuCI.


## Atualização — Samba4 e XSS de leases DHCPv6 no LuCI (2026-10-13)

- **GHSA-vx64-mmp7-h36c — Samba4, High:** a ACL na feed LuCI fixada por `v25.12.5` restringe `exec` a `/usr/sbin/smbd -V`, não ao daemon genérico `/usr/sbin/smbd`.
- **GHSA-686p-p8p9-x6fh — DHCPv6/LuCI, High:** a vista de leases na feed pinada usa `%h` para escapar o hostname antes da apresentação; o fecho completo também depende da correção do `odhcpd`.
- CSV atualizado; relatório: [VALIDACAO_LUCI_SAMBA4_DHCPV6_XSS_2026-10-13.md](VALIDACAO_LUCI_SAMBA4_DHCPV6_XSS_2026-10-13.md).
- **Limite:** feed de código-fonte confirmada, mas imagem, pacotes, ACLs e exposição reais não verificados.
- Próximo: Travelmate e restantes correções de aplicação; depois bibliotecas centrais (kernel, OpenSSL, musl, Dropbear).


## Atualização — Travelmate (2026-10-13)

- **GHSA-p35r-3323-6g7g — High:** o pacote `travelmate` na feed packages pinada por OpenWrt `v25.12.5` é `2.4.6-r2`; a função de auto-login canonicaliza o caminho e permite apenas scripts sob `/etc/travelmate/*.login` antes de executar.
- O backend passa a impor a allowlist, mesmo que a ACL LuCI permita escrita UCI na configuração `travelmate`.
- CSV e relatório atualizados: [VALIDACAO_TRAVELMATE_2026-10-13.md](VALIDACAO_TRAVELMATE_2026-10-13.md).
- Limite: não confirma pacote/configuração real em routers XFI.


## Revisão pendente — UPnP stored XSS (2026-10-13)

- **GHSA-8v49-6387-7f89 — High:** as vistas de mapas ativos e estado UPnP na feed LuCI pinada escapam a descrição com `%h`.
- **Pendente de fecho:** `luci-app-upnp/htdocs/.../view/upnp/upnp.js` mantém uma segunda utilização de `rule.descr` sem escaping na linha 118. É necessário confirmar a origem de `data[0].rules` e se o valor é controlável por cliente LAN.
- CSV marcado `SOURCE_PIN_REVIEW_PARTIAL_PENDING_CONTEXT`; relatório: [REVISAO_LUCI_UPNP_XSS_2026-10-13.md](REVISAO_LUCI_UPNP_XSS_2026-10-13.md).
- Não classificar como totalmente corrigido até fechar a análise de proveniência. Sem PoC/teste físico.


## Atualização crítica — UPnP XSS: caminho inicial sem escaping identificado (2026-10-13)

- O backend LuCI UPnP lê a descrição do ficheiro de leases e associa-a às regras ativas; portanto, o valor pode ter origem num cliente da LAN.
- A vista de estado periódico escapa a descrição com `%h`, mas o render inicial em `upnp.js:118` ainda passa `rule.descr` sem escaping. A implementação da tabela acaba por colocar strings não-Node em `innerHTML`.
- O estado do CSV foi elevado para **`FIX_INCOMPLETE_SOURCE_PATH_REMAINS`**. As notas de release dizem que a correção existe, mas o pin de fonte revisto parece manter um caminho vulnerável.
- Relatório atualizado: [REVISAO_LUCI_UPNP_XSS_2026-10-13.md](REVISAO_LUCI_UPNP_XSS_2026-10-13.md).
- Ação proposta: corrigir a vista inicial com escaping HTML ou nó de texto e criar teste de regressão para render inicial e atualização periódica. Não alterar upstream nem router sem processo de aprovação e teste.


## Atualização — bibliotecas centrais (2026-10-13)

- **Prioridade alta: OpenSSL 3.5.7-r1.** O OpenSSL upstream publicou 3.5.8 (25-08-2026) e 3.5.9 (29-09-2026) com correções de segurança. A tag OpenWrt v25.12.5 continua a fixar 3.5.7-r1 e não foi encontrado backport local correspondente aos CVEs de 3.5.8/3.5.9 na árvore de patches. CSV recebeu nove registos de advisories; avaliar update/backports e dependências de DTLS, QUIC, CMS, CMP e EVP.
- **musl 1.2.5:** patches 004/005/006 de qsort estão presentes na release-base; CVE-2026-40200 fica como provável mitigação por backport pendente de diff e arquitetura.
- **Dropbear 2025.89-r3:** CVE-2025-14282 está corrigido pela versão; CVE-2026-3706 é advisory não revisto e o commit upstream afirma que a maleabilidade Ed25519 não tem impacto no uso no protocolo SSH. Manter em triagem, sem declarar vulnerabilidade remota confirmada.
- **Kernel 6.12.94:** pin de versão/hash confirmado; correlação de advisories por target ainda pendente.
- Relatório: [REVISAO_BIBLIOTECAS_CENTRAIS_2026-10-13.md](REVISAO_BIBLIOTECAS_CENTRAIS_2026-10-13.md).
- Não alterar routers; Zabbix continua em pausa.


## Prioridade elevada — kernel estável atrás do upstream (2026-10-13)

- OpenWrt `v25.12.5` fixa Linux `6.12.94`; a listagem oficial kernel.org já mostra `6.12.112` (2026-10-03).
- Estado: `UPSTREAM_STABLE_LAG_REQUIRES_PATCH_DIFF`. Não declarar CVEs concretos sem mapear o changelog e as patches backportadas.
- Comparar `6.12.95–6.12.112` com `target/linux/generic/backport-6.12`, `pending-6.12` e patches por target.
- Manter OpenSSL 3.5.7-r1 como prioridade alta; confirmar correções locais e build features antes de declarar exposição por dispositivo.
- Relatório: [REVISAO_BIBLIOTECAS_CENTRAIS_2026-10-13.md](REVISAO_BIBLIOTECAS_CENTRAIS_2026-10-13.md).


## Continuação da revisão de bibliotecas — 2026-10-13

- **OpenSSL CVE-2026-75803 corrigido no registo:** o patch local AES-GCM-SIV/SIV não é equivalente à correção para ChaCha20-Poly1305/AES-OCB no caminho `EVP_Cipher()`. O pin v25.12.5 (3.5.7-r1) precede a correção 3.5.8. Prioridade alta; confirmar build features e consumidores.
- Matriz CSV ampliada com CVEs adicionais publicados nas releases OpenSSL 3.5.8 e 3.5.9; aplicabilidade individual condicionada a feature/build/uso.
- **musl CVE-2026-40200:** inspeção direta dos patches 004–006 confirma backport da correção qsort e reforços de limites/shift. Fechado ao nível da fonte/tag, não ao nível de imagem instalada.
- Changelog de desenvolvimento posterior lista OpenSSL 3.5.9 e kernel 6.12.112, mas tag `v25.12.6` não foi resolvida como tag oficial no GitHub nesta verificação. Não substituir a release-base estável até existir release/tag verificável.
- Próxima ação: análise diferencial de changelogs Linux 6.12.95–6.12.112 contra patches OpenWrt genéricos e específicos por target; depois concluir triagem Dropbear CVE-2026-3706.
- Sem alterações em routers; Zabbix permanece pausado.


## Kernel — primeira triagem CVE posterior ao pin (2026-10-13)

- Base OpenWrt v25.12.5 fixa Linux 6.12.94; changelog de desenvolvimento mostra bumps até 6.12.112 em alguns targets, mas a tag v25.12.6 não foi confirmada nesta consulta.
- Primeiro cruzamento identificou CVE-2026-63810 (6.12.95), CVE-2026-74665 (6.12.104), CVE-2026-89995 e CVE-2026-90344 (6.12.110), e CVE-2026-98211 (6.12.112). A presença de correção equivalente nos patches OpenWrt ainda precisa de diff de conteúdo; busca por nomes de ficheiro não é conclusiva.
- Relatório: [REVISAO_KERNEL_6.12.94_VS_6.12.112_2026-10-13.md](REVISAO_KERNEL_6.12.94_VS_6.12.112_2026-10-13.md).
- Próximo: verificar os fixes upstream individualmente contra backport/pending e target-specific patches; depois completar Dropbear CVE-2026-3706.
- Sem alterações em routers; Zabbix continua pausado.


## Dropbear — triagem CVE-2026-3706 concluída documentalmente (2026-10-13)

- O advisory permanece não revisto. A lista de patches do OpenWrt v25.12.5 não contém o patch upstream `S < L` em `curve25519.c`.
- O commit do mantenedor Dropbear afirma que a maleabilidade Ed25519 corrigida não tem impacto de segurança na forma como é usada no protocolo SSH. Não há evidência suficiente para classificar o caso como explorável via SSH.
- Estado CSV: `ADVISORY_UNREVIEWED_UPSTREAM_SAYS_NO_SSH_PROTOCOL_IMPACT`. Monitorizar por clarificação upstream; sem ação emergencial em routers com base apenas neste advisory.
- Relatório: [REVISAO_DROPBEAR_CVE-2026-3706_2026-10-13.md](REVISAO_DROPBEAR_CVE-2026-3706_2026-10-13.md).
- Nenhuma alteração de router/build/teste físico; Zabbix continua pausado.
