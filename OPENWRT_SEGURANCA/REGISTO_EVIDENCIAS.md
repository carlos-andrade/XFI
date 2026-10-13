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


## 2026-10-13 — Revisão complementar dos fixes OpenWrt 25.12.5

- **Fonte consultada:** [notas oficiais OpenWrt 25.12.5](https://openwrt.org/releases/25.12/notes-25.12.5), consultadas para ampliar a revisão além dos cinco advisories odhcpd já registados.
- **Relatório criado:** `OPENWRT_SEGURANCA/REVISAO_FIXES_ADICIONAIS_25.12.5_2026-10-13.md`.
- **CSV atualizado:** oito registos adicionais (NDP relay, stored XSS DHCPv6/LuCI, três CVEs uhttpd, cgi-io, ead e umdns). Commit CSV: `238592647efeb4dc8fd5e9d1516bf0473cb1d315`.
- **Commit do relatório:** `2816c459827ad4e1991efd3aae28d76485645d0b`.
- **Qualificação de evidência:** os registos novos estão marcados `RELEASE_NOTE_RECORDED_PIN_PENDING`; ainda não foram normalizados intervalos afetados nem confirmados os pins individuais dos pacotes na tag `v25.12.5`.
- **Outros grupos identificados:** apps LuCI, kernel, OpenSSL, musl, Dropbear e serviços de rede/hardening. O relatório separa estes itens e condiciona a aplicabilidade à presença do pacote, configuração e versão da imagem.
- **Validação:** leitura posterior do CSV e do relatório confirmou a persistência dos oito registos e do documento. Esta validação é documental; não houve teste físico, alteração de router, PoC contra produção ou mudança no Zabbix.
- **Estado:** revisão ampliada iniciada e documentada; validação por advisory/pin e mapeamento para hardware real continuam pendentes. Zabbix permanece em pausa.


## 2026-10-13 — Pin uhttpd verificado para três CVEs

- **Fonte:** Makefile de uhttpd na tag oficial OpenWrt `v25.12.5`, blob SHA `915baa07ab9a0cb44f6819d9d09bc2c001ed2eb7`.
- **Pin:** `PKG_SOURCE_DATE=2026-06-16`; `PKG_SOURCE_VERSION=7b1bec45826bd78c8afc993435bdc0f1df2fe399`.
- **Comparação upstream:** `1b624f8f814ed568608d756512892416e0431d77...7b1bec45826bd78c8afc993435bdc0f1df2fe399` confirmou três commits à frente do limiar citado nas páginas dos advisories.
- **Registos atualizados:** CVE-2026-55612, CVE-2026-55614 e CVE-2026-55613 para `RELEASE_NOTES_AND_PACKAGE_PIN_CONFIRMED`; commit CSV `c58a1154ae501d4e4ec92e29065244798352a38b`.
- **Relatório atualizado:** `REVISAO_FIXES_ADICIONAIS_25.12.5_2026-10-13.md`; commit `870fa8e667dacb32e8bbf6a951a7a1787e9c2d80`.
- **Limite:** validação da tag e pin de fonte, não do binário instalado; não houve teste de router nem alteração Zabbix.


## 2026-10-13 — Fecho da validação documental do pin cgi-io

- **Advisory:** GHSA-jw5r-xhf5-2xcq / CVE-2026-62947; baseline afetado até OpenWrt 25.12.4, cgi-io HEAD `658b14b`.
- **Cadeia de pins verificada:** `feeds.conf.default` da tag OpenWrt `v25.12.5` (blob `23962703cf641edd8d4e2ec2eef6725ca9fca396`) aponta o feed packages para `5caa62e0bc9f7fb9b0c12a23267bceb7724214dd`; o Makefile `net/cgi-io/Makefile` nesse commit (blob `e8b6d2fc8ad127277e4cfba94c38bb3c1203a016`) fixa `PKG_SOURCE_VERSION=7314451cb99692c0862a70c3307ee08bd2fbd9c0` e `PKG_SOURCE_DATE=2026-06-28`.
- **Código:** o `main.c` do pin (blob `09792fadfe381240a92c0a5e25f33a330ac926f7`) canonicaliza o caminho antes da autorização ACL. O baseline afetado (blob `806d7153cde28d99f1c4ab9801177adfa61d3d1b`) autorizava e abria o caminho sem canonicalização.
- **Registo:** CSV normalizado para `CVE-2026-62947 / GHSA-jw5r-xhf5-2xcq`; estado `RELEASE_NOTES_AND_PACKAGE_PIN_CONFIRMED`.
- **Fontes:** https://github.com/openwrt/openwrt/blob/v25.12.5/feeds.conf.default ; https://github.com/openwrt/packages/blob/5caa62e0bc9f7fb9b0c12a23267bceb7724214dd/net/cgi-io/Makefile ; https://github.com/openwrt/cgi-io/blob/7314451cb99692c0862a70c3307ee08bd2fbd9c0/main.c ; https://github.com/openwrt/openwrt/security/advisories/GHSA-jw5r-xhf5-2xcq
- **Limite:** confirmação de código-fonte na cadeia de feed, não de binários de todos os targets, builds personalizadas ou pacotes instalados em routers XFI. Sem teste físico ou alterações de routers; Zabbix permanece em pausa.


## 2026-10-13 — Revisão de LuCI Tailscale Community (Critical)

- **Advisory:** GHSA-xwc5-mx58-rh35, severidade Critical, CVSS 9.9; vetor de injeção de comandos root via `tailscale.do_login` com conta ACL delegada, aplicação instalada e Tailscale em estado de logout/NeedsLogin.
- **Pin da feed:** OpenWrt `v25.12.5` fixa LuCI em `128a7812f4be233c5dd7f7466f534fd888785caf`.
- **Código inspecionado:** `applications/luci-app-tailscale-community/root/usr/share/rpcd/ucode/tailscale.uc`, blob SHA `2a30bdbfbadc285133c25b3d50dd6ae4b5317bf4`; a construção do comando usa `shell_quote(login_cmd + ' &')` no shell exterior.
- **Estado:** `RELEASE_NOTES_AND_FEED_PIN_CONFIRMED` no nível das notas e fonte da feed; não prova presença da aplicação nem conteúdo binário num router específico.
- **Relatório:** [VALIDACAO_LUCI_TAILSCALE_2026-10-13.md](VALIDACAO_LUCI_TAILSCALE_2026-10-13.md).
- **Não realizado:** nenhum PoC, build ou teste físico; nenhum router alterado; Zabbix continua em pausa.


## 2026-10-13 — Validação LuCI advanced-reboot e adblock-fast

- **Feed analisada:** LuCI commit `128a7812f4be233c5dd7f7466f534fd888785caf`, fixado por OpenWrt `v25.12.5`.
- **CVE-2026-55897 / GHSA-vj96-f37g-37f6:** a ACL de leitura de `luci-app-advanced-reboot` (blob `281d59c8d24996c4c880c4baf99ce2c3a0f8c089`) não contém grant de `/bin/sh` nem `file.exec`; o vetor específico do advisory não aparece nessa ACL.
- **CVE-2026-55159 / GHSA-ggpf-xrph-wg5v:** o backend `luci-app-adblock-fast` (blob `f7062814454328a5dd0bdbe7d7e724c410c95ae3`) substitui o antigo `setCronEntry` por `syncCron`, valida os campos da agenda e monta uma linha de cron controlada antes de gravar o crontab.
- **Estado CSV:** ambos `RELEASE_NOTES_AND_FEED_PIN_CONFIRMED`; os riscos por equipamento continuam condicionados a presença do pacote, ACLs e imagem real.
- **Relatório:** [VALIDACAO_LUCI_ADVANCED_REBOOT_ADBLOCK_FAST_2026-10-13.md](VALIDACAO_LUCI_ADVANCED_REBOOT_ADBLOCK_FAST_2026-10-13.md).
- **Não realizado:** PoC, build ou teste físico; nenhum router alterado; Zabbix permanece em pausa.


## 2026-10-13 — Validação LuCI Samba4 e XSS de leases DHCPv6

- **Feed LuCI pinada:** `128a7812f4be233c5dd7f7466f534fd888785caf`.
- **GHSA-vx64-mmp7-h36c:** a ACL Samba4 (blob `e911e60e07d3a1e6360b68246dc4ec2a5e4e5ce5`) concede `exec` apenas ao objeto `/usr/sbin/smbd -V`, evitando o grant genérico `/usr/sbin/smbd` descrito no advisory.
- **GHSA-686p-p8p9-x6fh:** a vista de leases DHCP no LuCI (blob `7be0eb9046c919230f5f8f99773fc567eef91979`) usa `%h` para escaping HTML do hostname. A correção do odhcpd continua parte da cadeia de mitigação.
- **Estado CSV:** ambos `RELEASE_NOTES_AND_FEED_PIN_CONFIRMED`; a confirmação por dispositivo permanece pendente.
- **Relatório:** [VALIDACAO_LUCI_SAMBA4_DHCPV6_XSS_2026-10-13.md](VALIDACAO_LUCI_SAMBA4_DHCPV6_XSS_2026-10-13.md).
- Nenhum PoC, build ou teste físico; nenhum router alterado; Zabbix em pausa.


## 2026-10-13 — Validação Travelmate

- **Advisory:** GHSA-p35r-3323-6g7g, High (CVSS 7.5).
- **Pin:** feed packages `5caa62e0bc9f7fb9b0c12a23267bceb7724214dd`; Makefile `net/travelmate/Makefile` (blob `71ca99568bc5377365350ad28d7b6feca0ee95ff`) declara `2.4.6-r2`.
- **Código:** `travelmate-functions.sh` (blob `b72e891632c7cbd0cf6f179f7b4c296eb700f157`) canonicaliza o caminho e só aceita `/etc/travelmate/*.login` antes de executar o script.
- **Estado CSV:** `RELEASE_NOTES_AND_PACKAGE_PIN_CONFIRMED`; pacote/configuração de dispositivo continuam por validar.
- **Relatório:** [VALIDACAO_TRAVELMATE_2026-10-13.md](VALIDACAO_TRAVELMATE_2026-10-13.md).
- Sem PoC, build ou teste físico; routers inalterados; Zabbix em pausa.


## 2026-10-13 — Revisão parcial de XSS LuCI UPnP

- **Advisory:** GHSA-8v49-6387-7f89, High, descrição de mapa UPnP controlável por cliente LAN.
- **Código na feed pinada:** vista de estado `80_upnp.js` (blob `3d6b88d065ed8ad6890a2d269bd3703454f206fc`) e vista principal ativa `upnp.js` (blob `04c870a45e3cfd693a04bd12ebdef2598b9970a3`) escapam a descrição com `%h`.
- **Achado de revisão:** a vista principal também apresenta `rule.descr` sem escaping na linha 118, noutra tabela. A origem e a controlabilidade desse valor ainda precisam de ser estabelecidas.
- **Estado:** `SOURCE_PIN_REVIEW_PARTIAL_PENDING_CONTEXT`; não declarar a correção integralmente fechada.
- **Relatório:** [REVISAO_LUCI_UPNP_XSS_2026-10-13.md](REVISAO_LUCI_UPNP_XSS_2026-10-13.md).
- Sem PoC, tráfego de teste, build ou teste físico; routers inalterados; Zabbix em pausa.


## 2026-10-13 — Achado reforçado: possível caminho XSS residual no LuCI UPnP

- **Origem:** backend `luci.upnp` lê a descrição do ficheiro `upnp_lease_file` (blob `f72b57b7ba84188b9b78854bf7ad0711394a0045`, linhas 24–38) e associa-a às regras ativas (linhas 89–111).
- **Sink:** render inicial em `luci-app-upnp/.../view/upnp/upnp.js:118` passa `rule.descr` sem escaping para `cbi_update_table`. A implementação `L.ui.Table.update` passa a string como filho de `E`; a primitiva DOM coloca strings não-Node em `innerHTML`.
- **Diferença:** o caminho de atualização periódica aplica `%h`, mas o render inicial não.
- **Estado:** `FIX_INCOMPLETE_SOURCE_PATH_REMAINS`; source pin parece deixar um caminho de XSS residual apesar da nota de release.
- **Correção proposta:** aplicar escaping à linha 118 ou passar nó de texto; adicionar teste de regressão para ambos os caminhos. Não foi alterado código upstream nem router.
- **Relatório:** [REVISAO_LUCI_UPNP_XSS_2026-10-13.md](REVISAO_LUCI_UPNP_XSS_2026-10-13.md).


## 2026-10-13 — Revisão inicial de bibliotecas centrais

- **OpenSSL:** OpenWrt `v25.12.5` fixa `3.5.7-r1`; upstream 3.5.8 e 3.5.9, posteriores, incluem correções de segurança. Não foram identificados patches locais específicos para os CVEs desses releases na árvore de patches do tag. Nove CVEs foram registados como exigindo revisão de backport e de funcionalidades ativas.
- **musl:** versão `1.2.5`; patches 004–006 sobre qsort/heap Leonardo estão presentes. CVE-2026-40200 marcado `BACKPORT_PATCH_PRESENT_NEEDS_DIFF_VALIDATION`, não fechado ainda.
- **Dropbear:** versão `2025.89-r3`; CVE-2025-14282 corrigido nessa versão. CVE-2026-3706 permanece como advisory não revisto/impacto contestado; commit upstream diz que a maleabilidade de assinatura não afeta o uso SSH.
- **Kernel:** `6.12.94`, hash `e998a232b9418db3301cb58468e291a4f41d6ab8306029b30d991f56251dc8d2`; pin confirmado, análise de CVEs por target pendente.
- **Relatório:** [REVISAO_BIBLIOTECAS_CENTRAIS_2026-10-13.md](REVISAO_BIBLIOTECAS_CENTRAIS_2026-10-13.md).
- Sem build, testes físicos ou alterações em routers; Zabbix em pausa.


## 2026-10-13 — Kernel 6.12.94 vs upstream 6.12.112

- A tag OpenWrt `v25.12.5` fixa Linux `6.12.94` (SHA-256 `e998a232b9418db3301cb58468e291a4f41d6ab8306029b30d991f56251dc8d2`).
- A listagem oficial kernel.org mostra `ChangeLog-6.12.112` publicado em 2026-10-03. A diferença é de 18 releases de manutenção.
- **Estado:** `UPSTREAM_STABLE_LAG_REQUIRES_PATCH_DIFF`; não é prova de CVE específico, pois ainda é necessário mapear patches backportadas no OpenWrt e configuração por target.
- Próximo: comparar changelogs 6.12.95–6.12.112 com backport/pending e patches de target.
- Fonte: https://www.kernel.org/pub/linux/kernel/v6.x/


## 2026-10-13 — OpenSSL CVE-2026-75803 e musl CVE-2026-40200: validação direta

- OpenSSL v25.12.5 fixa 3.5.7-r1. OpenSSL 3.5.8 documenta CVE-2026-75803: falha de verificação de tag AEAD em ciphertext vazio usando `EVP_Cipher()` para ChaCha20-Poly1305/AES-OCB. O patch OpenWrt 010 é para AES-GCM-SIV/AES-SIV e não é mitigação equivalente. CSV corrigido para `NOT_FIXED_BY_LOCAL_PATCH_OPENSSL_3_5_8_REQUIRED`; aplicação real depende do build e uso do caminho afetado.
- Changelog de desenvolvimento 25.12.6 menciona bump para OpenSSL 3.5.8/3.5.9, remoção da parte AES-GCM-SIV do patch e kernel 6.12.112 em targets. A referência Git `v25.12.6` não foi resolvida como tag; não tratar como release estável confirmada.
- musl: patches 004/005/006 inspecionados diretamente. 004 corrige `pntz()` na causa raiz CVE-2026-40200; 005 protege os limites do array de trabalho; 006 corrige shift UB. CSV atualizado para `BACKPORT_CONFIRMED_IN_TAG_SOURCE`; imagem construída continua por verificar.
- Fontes OpenSSL: https://github.com/openssl/openssl/releases/tag/openssl-3.5.8 ; https://github.com/advisories/GHSA-vr27-9w4v-hjw2
- Fonte changelog: https://openwrt.org/releases/25.12/changelog-25.12.6
- Fontes musl: https://github.com/openwrt/openwrt/tree/v25.12.5/toolchain/musl/patches


## 2026-10-13 — primeira triagem de CVEs do kernel posteriores a 6.12.94

- OpenWrt v25.12.5 fixa kernel 6.12.94. A changelog de desenvolvimento posterior menciona atualizações até 6.12.112 em alguns targets; a tag v25.12.6 não foi confirmada como tag Git nesta consulta.
- Inventariados os diretórios genéricos `backport-6.12` (271 patches) e `pending-6.12` (143 patches). A primeira pesquisa de nomes não encontrou correspondência óbvia para cinco fixes CVE; isso não prova ausência de backport, pois a correspondência exige comparação do conteúdo e patches específicos por target.
- Registados no CSV para revisão: CVE-2026-63810 (fix 6.12.95), CVE-2026-74665 (6.12.104), CVE-2026-89995 (6.12.110), CVE-2026-90344 (wireless/mac80211; 6.12.110/6.18.52) e CVE-2026-98211 (mmci; 6.12.112).
- Relatório: [REVISAO_KERNEL_6.12.94_VS_6.12.112_2026-10-13.md](REVISAO_KERNEL_6.12.94_VS_6.12.112_2026-10-13.md).
- Nenhuma imagem construída ou router alterado; Zabbix pausado.
