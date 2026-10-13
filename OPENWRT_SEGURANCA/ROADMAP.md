# Roadmap — OpenWrt Security XFI

**Atualização:** 2026-10-13  
**Percentual preliminar:** 32% — estimativa de planeamento documental; não representa segurança validada nem implantação. Reconciliar com a norma central de status do XFI/GOVERNANCA.  
**Estado:** fundação documental, shortlist técnica/comercial e especificação inicial preparadas; sem hardware inventariado ou testes físicos. **Zabbix em pausa por decisão de 2026-10-13; não avançar nessa frente até nova instrução.**

| Fase | Entregável | Critério de saída | Estado |
|---|---|---|---|
| 1. Fundação | Governança, arquitetura, baseline, fontes e teste | Documentação persistida e revista | DOCUMENTADO |
| 2. Inventário | Modelo de ficha de router e requisitos de cliente | Templates criados; falta preencher com hardware real | EM PREPARAÇÃO |
| 3. Ingestão inicial | Verificador agendado de URLs do catálogo | Workflow passa em execução real e relatório é revisto | **EXECUTADO COM SUCESSO — 20/20 URLs acessíveis** |
| 4. Ingestão ampliada | Releases, advisories, commits e páginas de hardware | Dados normalizados, rastreáveis e revistos | **EM IMPLEMENTAÇÃO — catálogo e esquema JSON preparados; nova execução pendente de confirmação** |
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

## Próximas ações — fora da frente Zabbix

1. **Confirmar a execução da versão ampliada do verificador** e rever o relatório JSON; a evidência anterior de 20/20 refere-se à versão inicial do catálogo.
2. **Continuar a diligência de hardware:** verificar SKU e revisão exata, disponibilidade e preço final, garantia, imagem OpenWrt suportada e método de recuperação.
3. **Preparar o inventário inicial** de routers e requisitos por perfil de cliente, sem inventar dados de equipamentos ainda não adquiridos.
4. **Concluir a ingestão ampliada** com validação do relatório normalizado, seguida de revisão semântica das fontes de releases, avisos de segurança e commits.
5. **Detalhar perfis de segurança e matriz de fluxos** para os diferentes perfis de cliente.
6. Retomar laboratório, homologação e deployment apenas depois de haver hardware identificado e evidências técnicas adequadas.

### Frente explicitamente em pausa

A implementação do Zabbix — incluindo levantamento da instância, atualização, templates, configuração de hosts, alertas, proxies e automação operacional — fica suspensa até nova instrução do responsável. A documentação existente mantém-se como referência; não realizar alterações na infraestrutura Zabbix enquanto a pausa estiver ativa.

## Limitação de estado
O percentual é apenas progresso documental e de planeamento. Nenhuma unidade física foi instalada, testada ou homologada. O Zabbix ainda não foi configurado para esta frota.
