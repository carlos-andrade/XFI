# Roadmap — OpenWrt Security XFI

**Atualização:** 2026-10-13  
**Percentual preliminar:** 30% — estimativa de planeamento documental; não representa segurança validada nem implantação. Reconciliar com a norma central de status do XFI/GOVERNANCA.  
**Estado:** fundação documental, shortlist técnica/comercial inicial e automação de catálogo preparadas; sem hardware inventariado ou testes físicos.

| Fase | Entregável | Critério de saída | Estado |
|---|---|---|---|
| 1. Fundação | Governança, arquitetura, baseline, fontes e teste | Documentação persistida e revista | DOCUMENTADO |
| 2. Inventário | Modelo de ficha de router e requisitos de cliente | Templates criados; falta preencher com hardware real | EM PREPARAÇÃO |
| 3. Ingestão inicial | Verificador agendado de URLs do catálogo | Workflow passa em execução real e relatório é revisto | IMPLEMENTADO, primeira execução pendente |
| 4. Ingestão ampliada | Releases, advisories, commits e páginas de hardware | Dados normalizados, rastreáveis e revistos | PLANEADO |
| 5. Perfis | Perfis por classe de cliente e matriz de fluxos | Requisitos e variáveis sem segredos | DOCUMENTADO PRELIMINARMENTE |
| 6. Seleção de hardware | Fabricantes, modelos, critérios, preços públicos e plano de homologação | Shortlist técnica/comercial criada; fontes revistas; critérios testáveis definidos | DOCUMENTADO, NÃO HOMOLOGADO |
| 7. Configuração reproduzível | Templates UCI/scripts por versão/hardware | Preflight, validação, diff e rollback | PLANEADO |
| 8. Laboratório | Ambiente isolado e testes automatizados | Matriz IPv4/IPv6, firewall, DNS, Wi-Fi, acesso e desempenho aprovada | PLANEADO |
| 9. Homologação | Fichas de hardware/perfil e evidências | Revisão por pares e risco residual aprovado | PLANEADO |
| 10. Operação | Telemetria, alertas, inventário, mudanças e incidentes | Runbooks e metas de serviço definidos | PLANEADO |
| 11. Piloto e escala | Rollout gradual, revisão e manutenção | Critérios de rollback e revisão periódica cumpridos | PLANEADO |

## Próximas ações
1. Pedir confirmação de SKU/revisão aos vendedores antes de comprar; preço de marketplace não comprova compatibilidade.
2. Comparar em laboratório GL-MT6000 e OpenWrt One, incluindo decisão explícita de firmware e custo de switch/AP.
3. Validar a revisão exata e recuperação do Cudy WR3000 antes de o considerar para linha económica.
4. Manter TP-Link Archer AX23 condicionado à confirmação da revisão e à resolução dos avisos técnicos.
5. Executar o workflow de verificação de fontes e analisar o artefacto.
6. Implementar ingestão controlada de releases/advisories e alterações de páginas oficiais.
7. Iniciar laboratório antes de qualquer deployment.

## Limitação de estado
O percentual é apenas progresso documental e de planeamento. Nenhuma unidade física foi instalada, testada ou homologada com base nestes documentos. Os preços públicos podem mudar e não são cotações vinculativas.
