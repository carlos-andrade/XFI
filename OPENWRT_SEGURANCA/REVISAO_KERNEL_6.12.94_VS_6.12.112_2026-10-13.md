# Revisão inicial do kernel Linux 6.12.94 vs releases estáveis posteriores

**Data:** 2026-10-13  
**Base de fonte:** OpenWrt `v25.12.5`  
**Pin:** Linux `6.12.94`; SHA-256 do tarball `e998a232b9418db3301cb58468e291a4f41d6ab8306029b30d991f56251dc8d2`  
**Estado geral:** `UPSTREAM_STABLE_LAG_REQUIRES_PATCH_DIFF`

## Objetivo e limites

A revisão compara o pin de kernel da tag OpenWrt v25.12.5 com correções upstream posteriores. O changelog público de desenvolvimento da série 25.12 enumera atualizações de kernel até 6.12.112 em alguns targets, mas a referência Git `v25.12.6` não foi resolvida como tag na consulta; portanto, isso não é tratado como release estável publicada. O código OpenWrt v25.12.5 mantém 6.12.94.

O primeiro inventário dos diretórios `target/linux/generic/backport-6.12` e `pending-6.12` encontrou 271 e 143 ficheiros, respetivamente (414 no total). A pesquisa inicial por nomes de ficheiro não encontrou correspondência óbvia para os fixes listados abaixo. Isto **não prova ausência de backport**: nomes podem não conter CVE ou descrição; ainda é necessária comparação do conteúdo/diff e dos patches específicos de cada target.

## Amostra de correções upstream posteriores ao pin

| CVE | Fix upstream | Área | Relevância preliminar para router | Estado XFI |
|---|---|---|---|---|
| CVE-2026-63810 | 6.12.95 | bdev pseudo-filesystem | Dependente de configuração/caminho de bloco; confirmar se existe no target | `UPSTREAM_FIX_AFTER_KERNEL_PIN_BACKPORT_DIFF_PENDING` |
| CVE-2026-74665 | 6.12.104 | Contabilização de comprimento de skb após ajuste de fragmentos generic XDP | Condicional ao uso do caminho generic XDP com fragmentos | `UPSTREAM_FIX_AFTER_KERNEL_PIN_BACKPORT_DIFF_PENDING` |
| CVE-2026-89995 | 6.12.110 | DMA direct allocator | Dependente de arquitetura e drivers que usem o caminho | `UPSTREAM_FIX_AFTER_KERNEL_PIN_BACKPORT_DIFF_PENDING` |
| CVE-2026-90344 | 6.12.110 / 6.18.52 | mac80211, CSA para canal 0 | Verificar a versão do feed wireless separadamente; não inferir só pelo kernel | `TARGET_AND_WIRELESS_FEED_REVIEW_REQUIRED` |
| CVE-2026-98211 | 6.12.112 | driver mmci, use-after-free em busy-timeout | Específico do driver/targets que o incluam | `UPSTREAM_FIX_AFTER_KERNEL_PIN_BACKPORT_DIFF_PENDING` |

Fontes upstream:
- CVE-2026-63810: https://lists.openwall.net/linux-cve-announce/2026/07/19/46
- CVE-2026-74665: https://lists.openwall.net/linux-cve-announce/2026/08/22/88
- CVE-2026-89995: https://lists.openwall.net/linux-cve-announce/2026/09/16/65
- CVE-2026-90344: https://lists.openwall.net/linux-cve-announce/2026/09/17/99
- CVE-2026-98211: https://lists.openwall.net/linux-cve-announce/2026/10/06/47
- Changelog OpenWrt de desenvolvimento: https://openwrt.org/releases/25.12/changelog-25.12.6
- Pin OpenWrt: https://github.com/openwrt/openwrt/blob/v25.12.5/target/linux/generic/kernel-6.12

## Próxima execução técnica

1. Para cada CVE, localizar o commit upstream fix e identificar os ficheiros/funções alterados.
2. Pesquisar os 414 patches genéricos de backport/pending por conteúdo equivalente; procurar também patches em diretórios específicos de target.
3. Conferir se o target usa o subsistema afetado e se a configuração do kernel habilita o caminho.
4. Atualizar o CSV com estados separados: fix presente na fonte, ausência confirmada, não aplicável ao target ou ainda inconclusivo.
5. Não classificar um router como vulnerável sem inventário de modelo/revisão, target, imagem e configuração efetiva.

Nenhuma imagem foi construída, nenhum router foi alterado e nenhum teste físico foi executado. Zabbix continua pausado.


## Verificação por commit upstream — kernel (2026-10-13)

Foram obtidos os commits upstream e os ficheiros exatos alterados para os cinco CVEs triados:
- CVE-2026-63810: commit `197971e6ffc0a6356b2ba2b22beb42bc0f7e412d`, altera `block/bdev.c`.
- CVE-2026-74665: commit `72468efcc089782fa047afddd10856b11a14ef5b`, altera `net/core/dev.c`.
- CVE-2026-89995: commit `c3fdb94da43ff23287f85664174c45c45e881a3f`, altera `kernel/dma/direct.c`.
- CVE-2026-90344: commit `099aadb2012d7490bc584cc5075ef11cbc33f2c3`, altera `net/mac80211/spectmgmt.c` (subsistema/feed wireless deve ser verificado separadamente).
- CVE-2026-98211: commit `af6fbf72e899932f330c4e5d0b84d985c922c633`, altera `drivers/mmc/host/mmci.c`.

A listagem dos 414 patches genéricos `backport-6.12` e `pending-6.12` não apresentou nomes que correspondam diretamente a estes cinco fixes. Isso é apenas um filtro por nome; ainda não equivale a diff de conteúdo, não exclui backport escondido em patch com nome genérico e não cobre diretórios específicos de target. Os cinco registos permanecem pendentes, com condições de aplicabilidade separadas.
