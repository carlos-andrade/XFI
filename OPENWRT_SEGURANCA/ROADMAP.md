# Roadmap — OpenWrt Security XFI

**Atualização:** 2026-10-13  
**Percentual preliminar:** 32% — estimativa de planeamento documental; não representa segurança validada nem implantação. Reconciliar com a norma central de status do XFI/GOVERNANCA.  
**Estado:** fundação documental, shortlist técnica/comercial e especificação inicial de monitorização Zabbix preparadas; sem hardware inventariado ou testes físicos.

| Fase | Entregável | Critério de saída | Estado |
|---|---|---|---|
| 1. Fundação | Governança, arquitetura, baseline, fontes e teste | Documentação persistida e revista | DOCUMENTADO |
| 2. Inventário | Modelo de ficha de router e requisitos de cliente | Templates criados; falta preencher com hardware real | EM PREPARAÇÃO |
| 3. Ingestão inicial | Verificador agendado de URLs do catálogo | Workflow passa em execução real e relatório é revisto | IMPLEMENTADO, primeira execução pendente |
| 4. Ingestão ampliada | Releases, advisories, commits e páginas de hardware | Dados normalizados, rastreáveis e revistos | PLANEADO |
| 5. Perfis | Perfis por classe de cliente e matriz de fluxos | Requisitos e variáveis sem segredos | DOCUMENTADO PRELIMINARMENTE |
| 6. Seleção de hardware | Fabricantes, modelos, critérios, preços públicos e plano de homologação | Shortlist técnica/comercial criada; fontes revistas; critérios testáveis definidos | DOCUMENTADO, NÃO HOMOLOGADO |
| 7. Monitorização Zabbix | Templates, métricas, alertas, inventário, proxies e canal seguro | Todos os routers monitorizados; recolha e alertas testados por modelo | ESPECIFICAÇÃO DOCUMENTADA, NÃO IMPLEMENTADA |
| 8. Controlo operacional via Zabbix | Ações autorizadas e runner restrito com auditoria/rollback | Ações críticas protegidas por aprovação, preflight e rollback | PLANEADO |
| 9. Configuração reproduzível | Templates UCI/scripts por versão/hardware | Preflight, validação, diff e rollback | PLANEADO |
| 10. Laboratório | Ambiente isolado e testes automatizados | Matriz IPv4/IPv6, firewall, DNS, Wi-Fi, acesso e desempenho aprovada | PLANEADO |
| 11. Homologação | Fichas de hardware/perfil e evidências | Revisão por pares e risco residual aprovado | PLANEADO |
| 12. Operação, piloto e escala | Telemetria, alertas, inventário, mudanças, incidentes e rollout | Runbooks, rollback, revisão periódica e responsabilidades aprovados | PLANEADO |

## Próximas ações
1. Confirmar versão e topologia da instância Zabbix existente.
2. Definir canal privado, proxies e método seguro de recolha por modelo.
3. Implementar templates mínimos e alertas num equipamento de laboratório.
4. Implementar apenas ações controladas, com runner restrito, aprovação e rollback.
5. Continuar diligência comercial dos modelos e validar a revisão física.
6. Iniciar homologação em laboratório antes de qualquer deployment.

## Limitação de estado
O percentual é apenas progresso documental e de planeamento. Nenhuma unidade física foi instalada, testada ou homologada. O Zabbix ainda não foi configurado para esta frota.
