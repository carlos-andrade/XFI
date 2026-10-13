# Roadmap — OpenWrt Security XFI

**Atualização:** 2026-10-13  
**Percentual preliminar:** 32% — estimativa de planeamento documental; não representa segurança validada nem implantação. Reconciliar com a norma central de status do XFI/GOVERNANCA.  
**Estado:** fundação documental, shortlist técnica/comercial e especificação inicial preparadas; sem hardware inventariado ou testes físicos. **Zabbix em pausa por decisão de 2026-10-13; não avançar nessa frente até nova instrução.**

| Fase | Entregável | Critério de saída | Estado |
|---|---|---|---|
| 1. Fundação | Governança, arquitetura, baseline, fontes e teste | Documentação persistida e revista | DOCUMENTADO |
| 2. Inventário | Modelo de ficha de router e requisitos de cliente | Templates criados; falta preencher com hardware real | EM PREPARAÇÃO |
| 3. Ingestão inicial | Verificador agendado de URLs do catálogo | Workflow passa em execução real e relatório é revisto | **EXECUTADO COM SUCESSO — 20/20 URLs acessíveis** |
| 4. Ingestão ampliada | Releases, advisories, commits e páginas de hardware | Dados normalizados, rastreáveis e revistos | **IMPLEMENTADO; execução validada de 26/26 URLs; catálogo expandido novamente e nova execução pendente** |
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
- **Validação após correção:** [execução](https://github.com/carlos-andrade/XFI/actions/runs/38384970277), com 26/26 URLs acessíveis, 0 erros HTTP, 0 rate limits e 0 erros de rede. O relatório foi publicado como artefacto. Esta execução ocorreu antes da adição posterior de quatro URLs específicas de release/segurança.

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

## Próximas ações — fora da frente Zabbix

1. **Confirmar a execução da versão ampliada do verificador** e rever o relatório JSON; a evidência anterior de 20/20 refere-se à versão inicial do catálogo.
2. **Continuar a diligência de hardware:** verificar SKU e revisão exata, disponibilidade e preço final, garantia, imagem OpenWrt suportada e método de recuperação.
3. **Preparar o inventário inicial** de routers e requisitos por perfil de cliente, sem inventar dados de equipamentos ainda não adquiridos.
4. **Reexecutar o verificador** após a inclusão das quatro URLs específicas de release/segurança e confirmar o relatório; depois estruturar registos semânticos de advisories/releases.
5. **Detalhar perfis de segurança e matriz de fluxos** para os diferentes perfis de cliente.
6. Retomar laboratório, homologação e deployment apenas depois de haver hardware identificado e evidências técnicas adequadas.

### Frente explicitamente em pausa

A implementação do Zabbix — incluindo levantamento da instância, atualização, templates, configuração de hosts, alertas, proxies e automação operacional — fica suspensa até nova instrução do responsável. A documentação existente mantém-se como referência; não realizar alterações na infraestrutura Zabbix enquanto a pausa estiver ativa.

## Limitação de estado
O percentual é apenas progresso documental e de planeamento. Nenhuma unidade física foi instalada, testada ou homologada. O Zabbix ainda não foi configurado para esta frota.
