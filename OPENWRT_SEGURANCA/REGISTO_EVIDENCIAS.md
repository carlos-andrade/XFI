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

## 2026-10-13 — Pesquisa inicial de fabricantes e modelos
- **Objetivo:** começar a estruturar uma frota OpenWrt para clientes com diferentes capacidades económicas, sem presumir uma marca/modelo previamente escolhido.
- **Nova pasta:** `OPENWRT_SEGURANCA/SELECAO_HARDWARE/`.
- **Documentos criados:** índice, critérios e pesos de seleção, triagem de fabricantes, shortlist de modelos, matriz de perfis, catálogo de fontes/evidências e plano de homologação.
- **Candidatos prioritários para diligência:** GL.iNet GL-MT6000 (Flint 2); Cudy WR3000 e variantes; TP-Link Archer AX23 v1/v1.20 apenas com cautela e testes adicionais.
- **Fontes consultadas:** OpenWrt Table of Hardware; página GL-MT6000; índices OpenWrt GL.iNet e Cudy; páginas e dados técnicos OpenWrt do Archer AX23; documentação oficial de hardening, segurança, backup e sysupgrade.
- **Achado material:** nomes comerciais podem abranger revisões de hardware incompatíveis; não comprar em lote nem instalar firmware sem identificar modelo e revisão exatos.
- **Validação realizada:** ficheiros novos criados por commit e leitura posterior confirmada no GitHub.
- **Validação pendente:** conferência de preços/garantia Portugal-UE, disponibilidade, revisão física das unidades, teste físico, throughput, Wi-Fi, VPN/SQM, atualização e recuperação.
- **Decisão:** lista preliminar de investigação; nenhum fabricante ou modelo está aprovado/homologado para implantação em clientes.
- **Risco residual:** os estados de release e compatibilidade podem mudar; confirmar a documentação oficial novamente na data da aquisição.
- **Commits principais:** índice `9c4525f33a18abf57dc6119f1f13e34ccf84c861`; critérios `4d9e4caaa0fbf197d72ef5665877a7900ffd167e`; fabricantes `c09197ee961de98f7dbddf7f5232e3742943d05b`; modelos `69d33bb393050420f131186731cce73c9c460981`; matriz `97a1370744ac89c23cb0ded11c044096ed1e0b92`; fontes `29c8d1f6be605489eabf4f8c1d825c3f6f21f13b`; plano `2a248f682fb8f171c8ce2db5809e2392c8ede080`.

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
