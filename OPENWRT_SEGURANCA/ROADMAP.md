# Roadmap — OpenWrt Security XFI

**Atualização:** 2026-10-13  
**Percentual preliminar:** 27% — estimativa de planeamento; não representa segurança validada nem implantação. Reconciliar com a norma central de status do XFI/GOVERNANCA.  
**Estado:** fundação documental, shortlist inicial de hardware e automação de catálogo preparadas; sem hardware inventariado ou testes físicos.

| Fase | Entregável | Critério de saída | Estado |
|---|---|---|---|
| 1. Fundação | Governança, arquitetura, baseline, fontes e teste | Documentação persistida e revista | DOCUMENTADO |
| 2. Inventário | Modelo de ficha de router e requisitos de cliente | Templates criados; falta preencher com hardware real | EM PREPARAÇÃO |
| 3. Ingestão inicial | Verificador agendado de URLs do catálogo | Workflow passa em execução real e relatório é revisto | IMPLEMENTADO, primeira execução pendente |
| 4. Ingestão ampliada | Releases, advisories, commits e páginas de hardware | Dados normalizados, rastreáveis e revistos | PLANEADO |
| 5. Perfis | Perfis por classe de cliente e matriz de fluxos | Requisitos e variáveis sem segredos | DOCUMENTADO PRELIMINARMENTE |
| 6. Seleção de hardware | Fabricantes, modelos, critérios e plano de homologação | Shortlist documental criada; fontes revistas; critérios testáveis definidos | DOCUMENTADO, NÃO HOMOLOGADO |
| 7. Configuração reproduzível | Templates UCI/scripts por versão/hardware | Preflight, validação, diff e rollback | PLANEADO |
| 8. Laboratório | Ambiente isolado e testes automatizados | Matriz IPv4/IPv6, firewall, DNS, Wi-Fi, acesso e desempenho aprovada | PLANEADO |
| 9. Homologação | Fichas de hardware/perfil e evidências | Revisão por pares e risco residual aprovado | PLANEADO |
| 10. Operação | Telemetria, alertas, inventário, mudanças e incidentes | Runbooks e metas de serviço definidos | PLANEADO |
| 11. Piloto e escala | Rollout gradual, revisão e manutenção | Critérios de rollback e revisão periódica cumpridos | PLANEADO |

## Próximas ações
1. Aprofundar diligência técnica e comercial de candidatos (preço com IVA, disponibilidade, garantia e recuperação em Portugal/UE).
2. Escolher 2–4 modelos para a primeira frota padrão, mantendo opções adequadas aos perfis de clientes.
3. Confirmar modelo/revisão exatos e fontes upstream antes de qualquer compra em lote.
4. Executar o workflow de verificação de fontes e analisar o artefacto.
5. Implementar ingestão controlada de releases/advisories e alterações de páginas oficiais.
6. Iniciar laboratório antes de qualquer deployment.

## Limitação de estado
O aumento percentual é apenas progresso de documentação e planeamento. Nenhuma unidade física foi instalada, testada ou homologada com base nestes documentos.
