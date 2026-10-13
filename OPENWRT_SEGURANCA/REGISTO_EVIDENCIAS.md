# Registo de evidências e decisões

Guardar apenas evidências não sensíveis. Dados de clientes e backups devem ficar em armazenamento protegido fora do Git.

## 2026-10-12 — Baseline documental criada
- **Escopo:** espaço no XFI para segurança de routers OpenWrt.
- **Referência normativa:** https://github.com/carlos-andrade/GOVERNANCA e GOVERNANCA/REGRAS_DO_PROJETO.md.
- **Alterações:** índice, governança, arquitetura, baseline, catálogo de fontes, plano de validação/rollback, roadmap, registo e ingestão.
- **Validação realizada:** verificação da branch main, árvore inicial e leitura dos documentos de governança.
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
- **Nova pasta:** OPENWRT_SEGURANCA/SELECAO_HARDWARE/.
- **Documentos criados:** índice, critérios e pesos de seleção, triagem de fabricantes, shortlist de modelos, matriz de perfis, catálogo de fontes/evidências e plano de homologação.
- **Candidatos iniciais:** GL.iNet GL-MT6000; Cudy WR3000 e variantes; TP-Link Archer AX23 v1/v1.20 apenas com cautela e testes adicionais.
- **Decisão:** lista preliminar de investigação; nenhum fabricante ou modelo está aprovado/homologado para implantação em clientes.

## 2026-10-13 — Pesquisa comercial Portugal/UE
- **Objetivo:** obter referências públicas de preço e separar custo de aquisição de compatibilidade e segurança.
- **Novo ficheiro:** OPENWRT_SEGURANCA/SELECAO_HARDWARE/PESQUISA_COMERCIAL_PT.md.
- **Preços observados:** Cudy WR3000 ~43,21 € com envio numa oferta comparadora e 55,65 € noutra oferta; Cudy WR3000S 58,66 €; TP-Link Archer AX23 ~67,76 €; GL.iNet GL-MT6000 165,37 €; GL.iNet GL-MT3000 102,85 €; OpenWrt One 174,24 € com IVA numa loja europeia.
- **Fontes:** KuantoKusta, Leroy Merlin, Worten, loja oficial GL.iNet UE, Banana Pi EU, documentação OpenWrt e suporte TP-Link Portugal. Preços são fotografia temporal, alguns via marketplace e não cotações vinculativas.
- **Achado material:** a matriz GL.iNet consultada distingue firmware estável GL-MT6000 4.9.1 baseado em OpenWrt 21.02, linha op24 baseada em 24.10 e OpenWrt upstream 25.12.5 disponível para o hardware. O XFI deve escolher e testar a linha de firmware explicitamente.
- **Validação pendente:** preço final/stock/envio/garantia para Portugal, revisão física, testes de Wi-Fi/VPN/SQM/firewall, atualização e recuperação. Nenhum produto foi comprado, testado ou homologado.

## 2026-10-13 — Zabbix obrigatório para a frota OpenWrt
- **Decisão:** todos os routers fornecidos/geridos pela XFI devem ser inventariados e monitorizados pelo Zabbix; o Zabbix é o centro operacional para métricas, alertas e acionamento de operações predefinidas.
- **Pasta criada:** MONITORAMENTO_ZABBIX/.
- **Documentos criados:** README, arquitetura, métricas e alertas, controlo operacional, segurança/acessos e plano de implementação.
- **Fontes oficiais consultadas:** documentação Zabbix sobre SNMP e descoberta de rede; wiki OpenWrt sobre Zabbix monitoring.
- **Regra de segurança:** não expor serviços administrativos na WAN; preferir SNMPv3 authPriv quando suportado, canal privado/proxy e runner restrito para mudanças complexas. Mudanças de alto impacto exigem aprovação, auditoria e rollback.
- **Validação realizada:** seis documentos criados por commits; integração com README raiz e documentação OpenWrt preparada para atualização.
- **Validação pendente:** ler de volta todos os ficheiros alterados, confirmar versão/topologia Zabbix existente, criar templates/hosts reais e testar em laboratório.
- **Estado:** DOCUMENTADO, NÃO IMPLEMENTADO. Nenhum host, template, proxy, ação ou credencial foi alterado na instância Zabbix.

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


## 2026-10-13 — Validação da pasta Zabbix e integração documental
- **Validação realizada:** leitura posterior confirmou os seis documentos em MONITORAMENTO_ZABBIX/ e as atualizações do README raiz, README OpenWrt, arquitetura, governança, baseline e roadmap.
- **Commits da pasta:** README bebe012173d38c04c2d020c29d8c970cc32606f2; arquitetura 1fe6c0d926f1e1870c5d8b7846a05f4900491472; métricas ea1e81386843015176ac2566ed8c6d318a8161a1; controlo operacional 54c8d43e6b6b0fff6650ef12af161ea9d0329cd8; segurança 0bb618d052f0866c4c95309861f6061752f0b960; plano c0579f481cf39c54151f3cfe8be9a41ed8aaced2.
- **Integração documental:** README raiz 0ba2f13bb84dc2524a0813db7d8eb70efb52e86d; README OpenWrt b42aef154338e29fccfa1150bb298ef7532ee9ab; arquitetura OpenWrt e4c1a8b8a3b6b2bbb06e6b3d270b91d23999d2ed; roadmap 85d9bf5c34cf6e72db07f91093e095cd7473e160; governança b37406974c6cf7ee74966c5dd9f4e09d79cd8809; baseline d61d873a1fafb0749bb3e543c2d16a2482b184a8.
- **Estado final:** DOCUMENTADO. A instância Zabbix não foi alterada; não existem ainda templates, hosts, proxies, ações ou testes de routers implementados.
- **Próximo gate:** confirmar a versão/topologia da instância Zabbix XFI e testar monitorização segura num equipamento de laboratório antes de declarar qualquer modelo homologado.


## 2026-10-13 — Preparação do levantamento e especificação de templates Zabbix
- **Objetivo:** avançar o trabalho sem presumir a versão instalada nem alterar a instância em produção.
- **Ficheiros criados:** MONITORAMENTO_ZABBIX/LEVANTAMENTO_DA_INSTANCIA.md; ESPECIFICACAO_TEMPLATE_XFI_OPENWRT.md; MODELO_INVENTARIO.csv; MATRIZ_DE_HOMOLOGACAO.md.
- **Alterações adicionais:** README Zabbix atualizado com os novos artefactos e plano atualizado com gate de confirmação da versão.
- **Commits de criação:** levantamento 03ae7cf34d31b2c0006fa75126417b7a08454d64; especificação 96b67db381c7a86012f21d010e176145161b8a3e; inventário 9d36d44c015a0175e6089c74391596f50b8562ed; matriz 991aa7985653585366d69d762eb2131ad49b2020.
- **Validação realizada:** commits de criação confirmados pelo GitHub. A validação de conteúdo por leitura posterior ainda será efetuada.
- **Não realizado:** comandos de levantamento não executados; instância Zabbix não acedida; templates, hosts, proxies e ações não foram criados ou alterados.
- **Estado:** DOCUMENTAÇÃO PREPARADA; IMPLEMENTAÇÃO BLOQUEADA ATÉ CONFIRMAR A VERSÃO E A TOPOLOGIA.


## 2026-10-13 — Política de versão Zabbix mais recente estável
- **Decisão do projeto:** a XFI utilizará sempre a versão estável mais recente do Zabbix para produção; alpha, beta e release candidate ficam excluídos de produção.
- **Verificação oficial nesta data:** a página de downloads indicava Zabbix 7.4.15 como release da série 7.4 e Zabbix 8.0.0rc1 como pré-lançamento. A referência para produção nesta data é 7.4.15, sujeita a nova verificação imediatamente antes da instalação/atualização.
- **Fontes oficiais:** https://www.zabbix.com/download_sources ; https://www.zabbix.com/release_notes ; https://www.zabbix.com/roadmap.
- **Controlos:** verificar compatibilidade e notas de atualização, realizar backup verificável, preparar rollback e testar antes de alterar produção.
- **Estado:** política documental registada. A versão atualmente instalada na infraestrutura XFI continua por confirmar; nenhuma atualização ou alteração da instância foi executada.

## 2026-10-13 — Ingestão ampliada de fontes OpenWrt

- **Alterações:** catálogo ampliado com fontes de advisories, releases, downloads, histórico de versões e repositório Git upstream; verificador passou a produzir metadados normalizados por URL e a separar HTTP 429 (rate_limited) de outros erros HTTP.
- **Correção operacional:** a página de commits do GitHub devolveu HTTP 429. A fonte de commits foi substituída pelo histórico oficial em git.openwrt.org.
- **Validação automática:** execução [GitHub Actions #9](https://github.com/carlos-andrade/XFI/actions/runs/38384970277), resultado sucesso; 26/26 URLs acessíveis, 0 erros HTTP, 0 rate limits, 0 erros de rede. Artefacto: [relatório JSON](https://github.com/carlos-andrade/XFI/actions/runs/38384970277/artifacts/11805091538).
- **Revisão semântica:** consulta às fontes oficiais identificou OpenWrt 25.12.5 como release estável mais recente na página inicial e 24.10 como série antiga, com fim de suporte previsto para setembro de 2026. Advisories e notas de release são fluxos complementares e devem ser acompanhados em paralelo.
- **Ficheiro de análise:** [REVISAO_FONTES_OFICIAIS_2026-10-13.md](REVISAO_FONTES_OFICIAIS_2026-10-13.md).
- **Limites:** o teste verifica acessibilidade no instante da execução; não constitui validação de conteúdo, avaliação de exposição de um router ou homologação.
- **Pendente:** a expansão recente do catálogo com notas específicas de releases requer uma nova execução automática; a revisão humana das vulnerabilidades por modelo/release continua por fazer.
- **Estado:** INGESTÃO DE METADADOS IMPLEMENTADA E EXECUTADA; REVISÃO SEMÂNTICA INICIAL DOCUMENTADA; HOMOLOGAÇÃO NÃO REALIZADA.

## 2026-10-13 — Validação final do catálogo e registo inicial de advisories

- **Validação do catálogo:** [GitHub Actions](https://github.com/carlos-andrade/XFI/actions/runs/38385191297) terminou com sucesso; 30/30 URLs acessíveis, zero erros HTTP, zero rate limits e zero erros de rede.
- **Artefacto:** [openwrt-source-check-report](https://github.com/carlos-andrade/XFI/actions/runs/38385191297/artifacts/11804862674).
- **Revisão documental:** fontes oficiais consultadas indicam OpenWrt 25.12.5 como release estável atual na data da consulta e série 24.10 como série antiga com fim de suporte previsto para setembro de 2026. A seleção de firmware continua condicionada ao modelo/revisão exatos.
- **Registo criado:** REGISTO_ADVISORIES_RELEASES.csv com uma linha de release e cinco exemplos de advisories citados no anúncio 25.12.5. Versões afetadas permanecem pendentes de confirmação em cada advisory individual.
- **Fonte primária:** https://lists.openwrt.org/pipermail/openwrt-announce/2026-June/000088.html
- **Limite:** a validação de links não confirma conteúdo, aplicabilidade, exposição ou homologação.
- **Estado:** catálogo automatizado validado; registo semântico inicial criado; correspondência de CVEs a modelos/firmware ainda não realizada.

## 2026-10-13 — Revisão individual dos cinco advisories odhcpd

- **Escopo:** CVE-2026-53921, CVE-2026-53918, CVE-2026-53920, CVE-2026-53922 e CVE-2026-55606.
- **Fontes primárias:** páginas individuais de security advisory em `github.com/openwrt/odhcpd`; links e detalhes consolidados em `REVISAO_ADVISORIES_ODHCPD_2026-10-13.md`.
- **Alterações:** atualizada a matriz `REGISTO_ADVISORIES_RELEASES.csv` com os intervalos afetados e commits de correção declarados pelas fontes; criado relatório de revisão semântica; roadmap atualizado.
- **Achado de qualidade:** várias páginas apresentam “Patched versions: None” no cabeçalho, mas listam commits de correção no rodapé. O registo mantém a discrepância explícita e não converte commits de ramo em afirmação de release corrigida.
- **Limitação:** inclusão em tags/builds publicadas ainda por confirmar; sem correspondência a modelo/revisão, firmware e pacote odhcpd de router XFI.
- **Não realizado:** não houve testes em routers, PoC contra produção, alteração de configuração nem modificação da instância Zabbix.
- **Estado:** revisão documental dos advisories concluída; validação por tag de release e aplicabilidade a hardware real pendentes.
- **Próxima ação:** inspecionar tags oficiais e `PKG_SOURCE_VERSION` do pacote odhcpd nas releases relevantes, com evidência por release. Zabbix permanece em pausa.

## 2026-10-13 — Cruzamento com notas oficiais OpenWrt 25.12.5

- **Fonte:** [releases oficiais OpenWrt](https://github.com/openwrt/openwrt/releases) e anúncio 25.12.5.
- **Confirmado nas notas de 25.12.5:** CVE-2026-53921 (Critical), CVE-2026-53918 (High), CVE-2026-53920 (High) e CVE-2026-53922 (Moderate) aparecem explicitamente na lista de correções de odhcpd.
- **Não confirmado na lista consultada:** CVE-2026-55606. A página do advisory lista o commit de correção `6907f28` no ramo 25.12, mas isso, isoladamente, não prova a inclusão na tag v25.12.5.
- **Alterações:** CSV, relatório de advisories e roadmap atualizados para distinguir as quatro correções explicitamente listadas da quinta pendente.
- **Limitação:** ainda falta verificar a tag/build concreta e o pin `PKG_SOURCE_VERSION` de odhcpd para fechar a CVE-2026-55606; nenhuma conclusão sobre router XFI sem inventário real.
- **Estado:** quatro CVEs confirmadas nas notas da release; uma pendente de validação por tag/pacote. Zabbix continua em pausa.

## 2026-10-13 — Correção e confirmação do pacote odhcpd em v25.12.5

- **Correção de revisão:** a conclusão anterior de que CVE-2026-55606 não aparecia nas notas de v25.12.5 estava errada. A entrada oficial da release v25.12.5 lista explicitamente CVE-2026-53921, CVE-2026-53918, CVE-2026-53920, CVE-2026-53922 e CVE-2026-55606 como corrigidas.
- **Fonte da release:** https://github.com/openwrt/openwrt/releases.
- **Makefile consultado diretamente na tag:** https://github.com/openwrt/openwrt/blob/v25.12.5/package/network/services/odhcpd/Makefile.
- **Blob SHA do Makefile:** `9353be754fefee82f08dff522258d9131c56f3ce`.
- **Pin observado:** `PKG_SOURCE_DATE=2026-06-29`; `PKG_SOURCE_VERSION=5d7be43f8b9dec0eb47e245cfab81108bb131273`.
- **Interpretação:** as notas da release declaram as cinco correções; o Makefile fornece a revisão do pacote usada pela tag. Não equivale a comprovar o pacote instalado em qualquer router XFI nem a certificar a imagem de cada alvo.
- **Estado:** evidência da release e do pin do pacote registada; validação por modelo/revisão/imagem instalada continua pendente. Zabbix permanece em pausa.
