# Roadmap — OpenWrt Security XFI

**Data base:** 2026-10-12  
**Percentual preliminar:** 15% — estimativa inicial; a base documental começou nesta etapa, sem hardware inventariado nem testes físicos. Reconciliar com a norma central de status do XFI/GOVERNANCA.  
**Estado:** fase documental iniciada; não homologado para produção.

| Fase | Entregável | Critério de saída | Estado |
|---|---|---|---|
| 1. Fundação | Governança, arquitetura, baseline, fontes, teste | Documentação persistida e revista | DOCUMENTADO nesta etapa |
| 2. Inventário | Modelos/revisões, releases, recursos e necessidades | Cada modelo tem suporte, alvo e recuperação identificados | PLANEADO |
| 3. Ingestão | Catálogo de wiki, releases, advisories, commits e hardware | Metadados/diffs versionados; licenças respeitadas | PLANEADO |
| 4. Perfis | Perfis por classe de cliente e matriz de fluxos | Requisitos e variáveis sem segredos | PLANEADO |
| 5. Configuração reproduzível | Templates UCI/scripts por versão/hardware | Preflight, validação, diff e rollback | PLANEADO |
| 6. Laboratório | Ambiente isolado e testes automatizados | Matriz IPv4/IPv6, firewall, DNS, Wi-Fi, acesso e desempenho aprovada | PLANEADO |
| 7. Homologação | Fichas de hardware/perfil e evidências | Revisão por pares e risco residual aprovado | PLANEADO |
| 8. Operação | Telemetria, alertas, inventário, mudanças e incidentes | Runbooks e metas de serviço definidos | PLANEADO |
| 9. Piloto | Lote reduzido com monitorização | Período e critérios de rollback cumpridos | PLANEADO |
| 10. Escala | Rollout faseado e melhoria contínua | Revisão periódica, patching e suporte | PLANEADO |

## Próximos passos recomendados
1. Identificar marcas, modelos e revisões exatos dos routers.
2. Definir classes de cliente e requisitos de VPN, filtragem, Wi-Fi e telemetria.
3. Automatizar a atualização do catálogo de fontes, releases e advisories.
4. Construir templates por release/target e iniciar laboratório antes de qualquer deployment.
