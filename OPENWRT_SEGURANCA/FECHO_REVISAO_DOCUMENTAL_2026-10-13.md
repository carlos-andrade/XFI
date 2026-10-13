# Fecho da sequência de revisão documental — XFI OpenWrt Security

**Data:** 2026-10-13  
**Estado da sequência:** `CONCLUIDO` para triagem documental; análise diferencial final do kernel e validação de imagem continuam como trabalho pendente, explicitamente separado.  
**Base analisada:** OpenWrt `v25.12.5`  
**Repositório:** https://github.com/carlos-andrade/XFI  
**Governança:** https://github.com/carlos-andrade/GOVERNANCA

## 1. O que foi concluído nesta sequência

1. **OpenSSL:** corrigida a interpretação de CVE-2026-75803. O patch local AES-GCM-SIV/SIV não corresponde à falha em ChaCha20-Poly1305/AES-OCB no caminho `EVP_Cipher()`. A base v25.12.5 fixa OpenSSL 3.5.7-r1, anterior à correção upstream 3.5.8. Foram acrescentados registos de advisories das releases 3.5.8/3.5.9, sem inventar severidades individuais quando não validadas.
2. **musl:** confirmada na fonte do tag a presença dos patches 004/005/006 relacionados com CVE-2026-40200 e reforços de limites/shift. Isto não comprova inclusão numa imagem específica.
3. **Dropbear:** concluída a triagem de CVE-2026-3706. O advisory está não revisto e o mantenedor upstream afirma que a maleabilidade corrigida não tem impacto de segurança no uso SSH. A ausência do patch na lista OpenWrt foi registada; exploração via protocolo SSH não demonstrada.
4. **Kernel:** identificados os commits upstream e os ficheiros exatos alterados para cinco CVEs posteriores ao pin. Foi inspecionada a listagem de 414 patches genéricos `backport-6.12` e `pending-6.12`; um filtro por nome não encontrou correspondência direta. Isso **não** equivale a uma comparação de conteúdo completa e não prova ausência de backports.
5. **Integridade do CSV:** 51 registos de dados, 13 campos por registo, zero linhas malformadas e zero IDs duplicados.

## 2. Matriz de decisão atual

| Área | Estado | Decisão |
|---|---|---|
| OpenSSL CVE-2026-75803 | `NOT_FIXED_BY_LOCAL_PATCH_OPENSSL_3_5_8_REQUIRED` | Prioridade alta para atualização/backport e revisão de uso; imagem não verificada |
| Outros CVEs OpenSSL 3.5.8/3.5.9 | `UPSTREAM_FIX_AFTER_OPENWRT_PIN_REQUIRES_FEATURE_REVIEW` | Determinar feature, build, configuração e utilização real antes de declarar aplicabilidade |
| musl CVE-2026-40200 | `BACKPORT_CONFIRMED_IN_TAG_SOURCE` | Backport de fonte confirmado; imagem/arquitetura real ainda não validadas |
| Dropbear CVE-2026-3706 | `ADVISORY_UNREVIEWED_UPSTREAM_SAYS_NO_SSH_PROTOCOL_IMPACT` | Monitorizar; não classificar como explorável via SSH sem evidência adicional |
| Kernel CVE-2026-63810 | `UPSTREAM_FIX_AFTER_KERNEL_PIN_BACKPORT_DIFF_PENDING` | Comparar hunk de `block/bdev.c` com patches OpenWrt e configuração do target |
| Kernel CVE-2026-74665 | `UPSTREAM_FIX_AFTER_KERNEL_PIN_BACKPORT_DIFF_PENDING` | Comparar hunk de `net/core/dev.c`; avaliar generic XDP e fragmentos |
| Kernel CVE-2026-89995 | `UPSTREAM_FIX_AFTER_KERNEL_PIN_BACKPORT_DIFF_PENDING` | Comparar hunk de `kernel/dma/direct.c`; avaliar arquitetura/drivers |
| Kernel CVE-2026-90344 | `TARGET_AND_WIRELESS_FEED_REVIEW_REQUIRED` | Verificar mac80211 no feed wireless específico do target |
| Kernel CVE-2026-98211 | `UPSTREAM_FIX_AFTER_KERNEL_PIN_BACKPORT_DIFF_PENDING` | Comparar hunk de `drivers/mmc/host/mmci.c`; confirmar driver no target |

## 3. Limites e critérios de conclusão operacional

- Não foi provado que qualquer router concreto esteja vulnerável ou corrigido: não existe inventário de modelos/revisões nem imagem instalada identificada.
- Não houve compilação de firmware, teste de laboratório, teste de protocolo, teste físico ou alteração em routers.
- O workflow de verificação de links teve uma execução anterior bem-sucedida (30/30 URLs acessíveis), mas não foi executado novamente após todos os commits desta sequência.
- O changelog de desenvolvimento 25.12.6 não foi tratado como release estável confirmada porque a referência Git `v25.12.6` não foi resolvida como tag nesta consulta.
- Zabbix continua pausado por decisão explícita.

## 4. Próxima fase de trabalho

A próxima fase deve ser um **diff semântico dos cinco commits do kernel contra o conteúdo real dos patches genéricos e específicos de target**, seguido de verificação de mac80211 e inventário de hardware. A classificação de risco por router só poderá ser feita depois de conhecer modelo/revisão, target, imagem, pacotes e configuração.

## 5. Evidência de alterações persistidas

- Matriz: https://github.com/carlos-andrade/XFI/blob/main/OPENWRT_SEGURANCA/REGISTO_ADVISORIES_RELEASES.csv
- Revisão de bibliotecas: https://github.com/carlos-andrade/XFI/blob/main/OPENWRT_SEGURANCA/REVISAO_BIBLIOTECAS_CENTRAIS_2026-10-13.md
- Revisão do kernel: https://github.com/carlos-andrade/XFI/blob/main/OPENWRT_SEGURANCA/REVISAO_KERNEL_6.12.94_VS_6.12.112_2026-10-13.md
- Triagem Dropbear: https://github.com/carlos-andrade/XFI/blob/main/OPENWRT_SEGURANCA/REVISAO_DROPBEAR_CVE-2026-3706_2026-10-13.md
- Roadmap: https://github.com/carlos-andrade/XFI/blob/main/OPENWRT_SEGURANCA/ROADMAP.md
- Evidências: https://github.com/carlos-andrade/XFI/blob/main/OPENWRT_SEGURANCA/REGISTO_EVIDENCIAS.md
