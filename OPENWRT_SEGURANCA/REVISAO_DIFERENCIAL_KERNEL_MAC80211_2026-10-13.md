# Fase técnica — revisão diferencial inicial de kernel e mac80211

**Data:** 2026-10-13  
**Base:** OpenWrt `v25.12.5`; kernel Linux `6.12.94`; pacote mac80211 `6.18.26`  
**Estado:** `EM_REVISAO` — análise upstream realizada; comparação integral contra patches genéricos e de todos os targets não concluída.  
**Governança:** https://github.com/carlos-andrade/GOVERNANCA  
**Repositório XFI:** https://github.com/carlos-andrade/XFI

## 1. Resultado desta fase

Foram consultados os metadados e diffs dos cinco commits upstream associados aos CVEs em triagem e foi consultado o Makefile mac80211 da tag OpenWrt. A comparação confirma a natureza das correções e a necessidade de verificar backports por conteúdo; não autoriza declarar ausentes todos os backports.

O Makefile de `package/kernel/mac80211` fixa `PKG_VERSION:=6.18.26`. A correção upstream para CVE-2026-90344 está identificada na série Linux 6.18.52 e no kernel 6.12.110. A versão 6.18.26 é anterior à release corrigida, mas um patch local equivalente ainda precisa ser descartado por comparação de conteúdo. O inventário inicial de nomes de patches não revelou um nome diretamente associado a CSA/channel 0; isso não é prova suficiente de ausência de correção.

## 2. Matriz dos commits upstream

| CVE | Ficheiro/função afetada | Mudança upstream | O que falta confirmar em OpenWrt |
|---|---|---|---|
| CVE-2026-63810 | `block/bdev.c`, inicialização de bdev pseudo-filesystem | Remove o registo do filesystem para impedir montagem por userspace e o caminho que pode levar a dereference nulo | Comparar o hunk exato com backport/pending genérico e patches por target |
| CVE-2026-74665 | `net/core/dev.c`, `bpf_prog_run_generic_xdp()` | Mantém `skb->len` e `skb->data_len` sincronizados após ajuste de fragmentos XDP | Comparar hunk exato; avaliar configuração e uso de generic XDP com fragmentos |
| CVE-2026-89995 | `kernel/dma/direct.c`, `dma_direct_alloc_from_pool()` | Devolve `struct page *` e transporta o endereço CPU por parâmetro de saída, corrigindo a semântica usada por callers distintos | Comparar hunk exato; avaliar arquitetura e drivers relevantes |
| CVE-2026-90344 | `net/mac80211/spectmgmt.c`, parsing de CSA | Usa valores negativos para distinguir informação ausente de canal/opclass zero e corrige a decisão de desconexão | Comparar patchset mac80211/backports pelo conteúdo; avaliar stack/driver do target |
| CVE-2026-98211 | `drivers/mmc/host/mmci.c`, `mmci_remove()` | Desativa de forma síncrona o trabalho atrasado de busy-timeout durante remoção | Comparar hunk exato; verificar se o target inclui o driver MMCI e o caminho busy-detect |

## 3. Fontes consultadas

- OpenWrt v25.12.5 — Makefile mac80211: https://github.com/openwrt/openwrt/blob/v25.12.5/package/kernel/mac80211/Makefile
- CVE-2026-63810 / commit: https://lists.openwall.net/linux-cve-announce/2026/07/19/46 e https://github.com/gregkh/linux/commit/197971e6ffc0a6356b2ba2b22beb42bc0f7e412d
- CVE-2026-74665 / commit: https://lists.openwall.net/linux-cve-announce/2026/08/22/88 e https://github.com/gregkh/linux/commit/72468efcc089782fa047afddd10856b11a14ef5b
- CVE-2026-89995 / commit: https://lists.openwall.net/linux-cve-announce/2026/09/16/65 e https://github.com/gregkh/linux/commit/c3fdb94da43ff23287f85664174c45c45e881a3f
- CVE-2026-90344 / commit: https://lists.openwall.net/linux-cve-announce/2026/09/17/99 e https://github.com/gregkh/linux/commit/099aadb2012d7490bc584cc5075ef11cbc33f2c3
- CVE-2026-98211 / commit: https://lists.openwall.net/linux-cve-announce/2026/10/06/47 e https://github.com/gregkh/linux/commit/af6fbf72e899932f330c4e5d0b84d985c922c633

## 4. Limites explícitos

- O inventário de 414 patches genéricos feito na fase anterior e a pesquisa por nomes são filtros preliminares, não um diff semântico integral.
- Não foi concluída nesta execução a leitura integral de todos os patches genéricos e específicos por target nem o diff do conteúdo do tarball backports contra o fix mac80211.
- Sem modelo/revisão de router e target selecionados, não se pode determinar aplicabilidade por equipamento.
- Nenhuma imagem foi construída; nenhum router foi alterado; nenhum teste físico ou de laboratório foi executado.
- Zabbix permanece em pausa.

## 5. Critério para fechar a fase

1. Fazer comparação de conteúdo dos hunks upstream com os patches efetivamente aplicados à árvore OpenWrt e ao backports mac80211.
2. Verificar os diretórios de patch específicos dos targets relevantes, depois de o hardware/target ser definido.
3. Registar resultado por CVE como backport confirmado, ausência confirmada, não aplicável ao target ou inconclusivo.
4. Relê-los no GitHub e atualizar o CSV, evidências e roadmap após cada subfase.


## 6. Subfase mac80211 — inspeção de patches overlay

**Estado da subfase:** `CONCLUIDO` para a inspeção do diretório `package/kernel/mac80211/patches/subsys`; avaliação do pacote completo e homologação por target continuam pendentes.

- Confirmado no Makefile da tag que o pacote fixa `PKG_VERSION:=6.18.26`.
- Inspecionados os 13 patches existentes em `package/kernel/mac80211/patches/subsys`, incluindo os patches de 2026 numerados 301–371.
- Nenhum dos 13 patches altera `net/mac80211/spectmgmt.c` ou contém os símbolos `ieee80211_parse_ch_switch_ie`, `new_chan_no` ou `new_op_class` associados ao fix de CVE-2026-90344.
- O patch 350 refere-se a varredura em canal radar e altera `cfg.c`, `chan.c`, `ieee80211_i.h`, `offchannel.c`, `scan.c` e `util.c`; a correspondência lexical com “CSA” foi tratada como falso positivo, não como correção do CVE.
- Como o fix upstream é posterior à versão pinada 6.18.26 e não foi encontrado um overlay equivalente no diretório `subsys`, o estado de risco deve ser elevado para **provável ausência de correção na árvore examinada**, sem o converter ainda em ausência global confirmada: o conteúdo exato do tarball `backports-6.18.26.tar.zst` e a configuração/target de destino não foram inspecionados.
- Referências: [Makefile mac80211 v25.12.5](https://github.com/openwrt/openwrt/blob/v25.12.5/package/kernel/mac80211/Makefile); [commit upstream](https://github.com/gregkh/linux/commit/099aadb2012d7490bc584cc5075ef11cbc33f2c3); [advisory CVE-2026-90344](https://lists.openwall.net/linux-cve-announce/2026/09/17/99).

**Próximo trabalho:** obter/verificar o conteúdo e hash do tarball mac80211 fixado, concluir diff semântico dos cinco fixes contra patches genéricos, e verificar patches por target depois de conhecido o hardware. A pesquisa por nomes, isoladamente, não prova ausência de backport.
