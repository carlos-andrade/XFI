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
- **Candidatos iniciais:** GL.iNet GL-MT6000; Cudy WR3000 e variantes; TP-Link Archer AX23 v1/v1.20 apenas com cautela e testes adicionais.
- **Fontes consultadas:** OpenWrt Table of Hardware; página GL-MT6000; índices OpenWrt GL.iNet e Cudy; páginas e dados técnicos OpenWrt do Archer AX23; documentação oficial de hardening, segurança, backup e sysupgrade.
- **Validação realizada:** ficheiros novos criados por commit e leitura posterior confirmada no GitHub.
- **Decisão:** lista preliminar de investigação; nenhum fabricante ou modelo está aprovado/homologado para implantação em clientes.

## 2026-10-13 — Pesquisa comercial Portugal/UE
- **Objetivo:** obter referências públicas de preço e separar custo de aquisição de compatibilidade e segurança.
- **Novo ficheiro:** `OPENWRT_SEGURANCA/SELECAO_HARDWARE/PESQUISA_COMERCIAL_PT.md`.
- **Preços observados:** Cudy WR3000 ~43,21 € com envio numa oferta comparadora e 55,65 € noutra oferta; Cudy WR3000S 58,66 €; TP-Link Archer AX23 ~67,76 €; GL.iNet GL-MT6000 165,37 €; GL.iNet GL-MT3000 102,85 €; OpenWrt One 174,24 € com IVA numa loja europeia.
- **Fontes:** KuantoKusta, Leroy Merlin, Worten, loja oficial GL.iNet UE, Banana Pi EU, documentação OpenWrt e suporte TP-Link Portugal. Preços são fotografia temporal, alguns via marketplace e não cotações vinculativas.
- **Achado material:** a matriz GL.iNet consultada distingue o firmware estável GL-MT6000 4.9.1 baseado em OpenWrt 21.02 da linha “op24” baseada em 24.10 e do OpenWrt upstream 25.12.5 disponível para o hardware. O XFI deve escolher e testar a linha de firmware explicitamente.
- **Candidatos para comparação em laboratório:** GL-MT6000 e OpenWrt One para capacidade/arquitetura; Cudy WR3000 como opção de orçamento após confirmação de revisão. GL-MT3000 é categoria portátil. Archer AX23 permanece condicionado à revisão e aos avisos técnicos.
- **Validação realizada:** pesquisa pública consultada; novo ficheiro criado e documentação técnica/comercial atualizada por commits. A leitura posterior dos ficheiros deve ser concluída para fechar a validação de persistência.
- **Validação pendente:** preço final/stock/envio/garantia para Portugal, revisão física, testes de Wi-Fi/VPN/SQM/firewall, atualização e recuperação. Nenhum produto foi comprado, testado ou homologado.
- **Risco residual:** preços e suporte podem mudar; os vendedores marketplace podem não garantir a revisão correta. Confirmar a documentação e SKU na data de compra.

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
