# Registo de evidências e decisões

Guardar apenas evidências não sensíveis. Dados de clientes e backups devem ficar em armazenamento protegido fora do Git.

## 2026-10-12 — Baseline documental criada
- **Escopo:** espaço no XFI para segurança de routers OpenWrt.
- **Referência normativa:** https://github.com/carlos-andrade/GOVERNANCA e `GOVERNANCA/REGRAS_DO_PROJETO.md`.
- **Alterações:** índice, governança, arquitetura, baseline, catálogo de fontes, plano de validação/rollback, roadmap, registo e ingestão.
- **Validação realizada:** verificação da branch `main`, árvore inicial e leitura dos documentos de governança.
- **Validação não realizada:** sem configuração aplicada em router, laboratório, varredura, homologação de hardware ou prova de segurança em produção.
- **Decisão:** tratar o conteúdo como baseline documental, nunca como garantia absoluta ou perfil de produção.

## 2026-10-13 — Inventário e verificação inicial de fontes
- **Alterações:** criado modelo de inventário de routers, template de requisitos por perfil de cliente, script de verificação de links e workflow GitHub Actions agendado/manual.
- **Catálogo:** ampliado com páginas oficiais sobre firewall, nftables, hardware, Firmware Selector e backup/restauro.
- **Validação realizada:** commits de criação confirmados e ficheiros relidos no GitHub.
- **Validação pendente:** execução real do workflow, revisão do relatório, testes de sintaxe no runner, preenchimento do inventário com modelos reais e teste em laboratório.
- **Limitação:** a verificação HTTP prova apenas acessibilidade aproximada do URL; não valida o conteúdo nem a segurança da recomendação.
- **Risco principal:** ainda não há modelo/revisão de router alvo, requisitos completos de clientes ou evidência de hardware.

## Modelo para registos futuros
### AAAA-MM-DD — Título
- Tipo: decisão / ingestão / alteração / teste / homologação / incidente / release.
- Responsável:
- Equipamento e versão:
- Fonte e data de consulta:
- Contexto e motivo:
- Alterações:
- Testes e ambiente:
- Resultado esperado/observado:
- Evidência não sensível:
- Risco residual:
- Aprovação:
- Commit/artefactos:
