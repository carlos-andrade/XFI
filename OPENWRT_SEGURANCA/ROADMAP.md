# Roadmap — OpenWrt Security XFI

**Atualização:** 2026-10-13  
**Percentual preliminar:** 22% — estimativa de planeamento; não representa segurança validada nem implantação. Reconciliar com a norma central de status do XFI/GOVERNANCA.  
**Estado:** fundação documental e primeira automação de catálogo preparadas; sem hardware inventariado ou testes físicos.

| Fase | Entregável | Critério de saída | Estado |
|---|---|---|---|
| 1. Fundação | Governança, arquitetura, baseline, fontes e teste | Documentação persistida e revista | DOCUMENTADO |
| 2. Inventário | Modelo de ficha de router e requisitos de cliente | Templates criados; falta preencher com hardware real | EM PREPARAÇÃO |
| 3. Ingestão inicial | Verificador agendado de URLs do catálogo | Workflow passa em execução real e relatório é revisto | IMPLEMENTADO, primeira execução pendente |
| 4. Ingestão ampliada | Releases, advisories, commits e páginas de hardware | Dados normalizados, rastreáveis e revistos | PLANEADO |
| 5. Perfis | Perfis por classe de cliente e matriz de fluxos | Requisitos e variáveis sem segredos | PLANEADO |
| 6. Configuração reproduzível | Templates UCI/scripts por versão/hardware | Preflight, validação, diff e rollback | PLANEADO |
| 7. Laboratório | Ambiente isolado e testes automatizados | Matriz IPv4/IPv6, firewall, DNS, Wi-Fi, acesso e desempenho aprovada | PLANEADO |
| 8. Homologação | Fichas de hardware/perfil e evidências | Revisão por pares e risco residual aprovado | PLANEADO |
| 9. Operação | Telemetria, alertas, inventário, mudanças e incidentes | Runbooks e metas de serviço definidos | PLANEADO |
| 10. Piloto e escala | Rollout gradual, revisão e manutenção | Critérios de rollback e revisão periódica cumpridos | PLANEADO |

## Próximas ações
1. Identificar marcas, modelos e revisões exatos dos routers disponíveis.
2. Executar manualmente o workflow de verificação de fontes e analisar o artefacto.
3. Implementar ingestão controlada de releases/advisories e alterações de páginas oficiais.
4. Definir perfis de cliente e construir templates por release/target.
5. Iniciar laboratório antes de qualquer deployment.
