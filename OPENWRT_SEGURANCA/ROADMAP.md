# Roadmap — OpenWrt Security XFI

**Atualização:** 2026-10-13  
**Percentual preliminar:** 32% — estimativa de planeamento documental; não representa segurança validada nem implantação. Reconciliar com a norma central de status do XFI/GOVERNANCA.  
**Estado:** fundação documental, shortlist técnica/comercial e especificação inicial preparadas; sem hardware inventariado ou testes físicos. **Zabbix em pausa por decisão de 2026-10-13; não avançar nessa frente até nova instrução.**

| Fase | Entregável | Critério de saída | Estado |
|---|---|---|---|
| 1. Fundação | Governança, arquitetura, baseline, fontes e teste | Documentação persistida e revista | DOCUMENTADO |
| 2. Inventário | Modelo de ficha de router e requisitos de cliente | Templates criados; falta preencher com hardware real | EM PREPARAÇÃO |
| 3. Ingestão inicial | Verificador agendado de URLs do catálogo | Workflow passa em execução real e relatório é revisto | IMPLEMENTADO, primeira execução pendente |
| 4. Ingestão ampliada | Releases, advisories, commits e páginas de hardware | Dados normalizados, rastreáveis e revistos | PLANEADO |
| 5. Perfis | Perfis por classe de cliente e matriz de fluxos | Requisitos e variáveis sem segredos | DOCUMENTADO PRELIMINARMENTE |
| 6. Seleção de hardware | Fabricantes, modelos, critérios, preços públicos e plano de homologação | Shortlist técnica/comercial criada; fontes revistas; critérios testáveis definidos | DOCUMENTADO, NÃO HOMOLOGADO |
| 7. Monitorização Zabbix | Templates, métricas, alertas, inventário, proxies e canal seguro | Todos os routers monitorizados; recolha e alertas testados por modelo | **EM PAUSA — especificação documentada; não implementada** |
| 8. Controlo operacional via Zabbix | Ações autorizadas e runner restrito com auditoria/rollback | Ações críticas protegidas por aprovação, preflight e rollback | **EM PAUSA — não iniciar** |
| 9. Configuração reproduzível | Templates UCI/scripts por versão/hardware | Preflight, validação, diff e rollback | PLANEADO |
| 10. Laboratório | Ambiente isolado e testes automatizados | Matriz IPv4/IPv6, firewall, DNS, Wi-Fi, acesso e desempenho aprovada | PLANEADO |
| 11. Homologação | Fichas de hardware/perfil e evidências | Revisão por pares e risco residual aprovado | PLANEADO |
| 12. Operação, piloto e escala | Telemetria, alertas, inventário, mudanças, incidentes e rollout | Runbooks, rollback, revisão periódica e responsabilidades aprovados | PLANEADO |

## Próximas ações — fora da frente Zabbix

1. **Executar e validar o workflow de verificação de URLs** já preparado para o catálogo de fontes oficiais; rever o relatório da primeira execução.
2. **Continuar a diligência de hardware:** verificar SKU e revisão exata, disponibilidade e preço final, garantia, imagem OpenWrt suportada e método de recuperação.
3. **Preparar o inventário inicial** de routers e requisitos por perfil de cliente, sem inventar dados de equipamentos ainda não adquiridos.
4. **Ampliar a ingestão de fontes oficiais** (releases, avisos de segurança, commits e páginas de hardware), com dados normalizados e rastreáveis.
5. **Detalhar perfis de segurança e matriz de fluxos** para os diferentes perfis de cliente.
6. Retomar laboratório, homologação e deployment apenas depois de haver hardware identificado e evidências técnicas adequadas.

### Frente explicitamente em pausa

A implementação do Zabbix — incluindo levantamento da instância, atualização, templates, configuração de hosts, alertas, proxies e automação operacional — fica suspensa até nova instrução do responsável. A documentação existente mantém-se como referência; não realizar alterações na infraestrutura Zabbix enquanto a pausa estiver ativa.

## Limitação de estado
O percentual é apenas progresso documental e de planeamento. Nenhuma unidade física foi instalada, testada ou homologada. O Zabbix ainda não foi configurado para esta frota.
