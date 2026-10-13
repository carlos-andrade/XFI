# Revisão de bibliotecas centrais — OpenSSL, musl, Dropbear e kernel

**Data:** 2026-10-13  
**Release-base:** OpenWrt v25.12.5 (última release estável indicada pela API oficial consultada nesta revisão)  
**Feed packages:** `5caa62e0bc9f7fb9b0c12a23267bceb7724214dd`

## Resumo executivo

| Componente | Pin encontrado | Estado documental | Prioridade |
|---|---|---|---|
| OpenSSL | 3.5.7-r1 | A versão fica atrás de 3.5.8 e 3.5.9; não foram encontradas patches locais correspondentes aos fixes de 3.5.8/3.5.9 na árvore de patches do tag | **Alta — requer atualização/backport** |
| musl | 1.2.5 | A release-base inclui patches locais `004`, `005` e `006` relacionados com qsort/heap Leonardo; a correção CVE-2026-40200 aparenta estar backportada | Confirmar aplicabilidade/patches |
| Dropbear | 2025.89-r3 | Contém o fix de CVE-2025-14282 (introduzido em 2025.89); advisory não oficial/unreviewed CVE-2026-3706 necessita análise de impacto, e o upstream afirma que a maleabilidade Ed25519 em questão não tem impacto na forma como é usada no protocolo SSH | Média/triagem |
| Linux kernel | 6.12.94 | Versão e hash pinados; ainda não foi feita correlação completa de advisories/kernel CVEs nem configuração por target | Pendente |

## 1. OpenSSL — 3.5.7-r1: atualização de segurança prioritária

Fonte oficial OpenWrt: [Makefile OpenSSL na tag v25.12.5](https://github.com/openwrt/openwrt/blob/v25.12.5/package/libs/openssl/Makefile), blob SHA `76a04b4b5020433a621ec7dd1555cefeb67c22cd`. Declara `PKG_VERSION=3.5.7`, `PKG_RELEASE=1` e source tarball OpenSSL 3.5.7.

A árvore de patches dessa tag contém patches OpenWrt de integração/configuração e um patch de AES-GCM-SIV, mas não contém backports identificados para os fixes de segurança das versões upstream 3.5.8 e 3.5.9. A página oficial OpenSSL lista 3.5.8 (25-08-2026) e 3.5.9 (29-09-2026) como releases de segurança posteriores.

### Advisories posteriores ao pin 3.5.7

- **CVE-2026-84782 — High:** retransmissão DTLS de mensagens handshake a partir de offset de buffer obsoleto; corrigido em OpenSSL 3.5.9. A aplicabilidade depende do uso de DTLS e do código efetivamente compilado.
- **CVE-2026-35189:** alocação de memória excessiva no processamento relativo de CRLDP; corrigido em 3.5.9.
- **CVE-2026-35191:** contabilização excessiva de crédito de amplificação QUIC não validado; corrigido em 3.5.9.
- **CVE-2026-42772:** DoS de CPU por remontagem O(n²) de fragmentos QUIC; corrigido em 3.5.9.
- **CVE-2026-63072:** heap buffer overflow no unwrapping CMS; corrigido em 3.5.8.
- **CVE-2026-63073:** DN Sender não confiável usado como format string em validação de resposta CMP; corrigido em 3.5.8.
- **CVE-2026-63074:** crescimento de cache CMP `extraCerts` sem limite; corrigido em 3.5.8.
- **CVE-2026-63075:** retenção de pacotes ACK-only QUIC pode causar exaustão de memória; corrigido em 3.5.8.
- **CVE-2026-75803:** possibilidade de falsificação AEAD com ciphertext vazio através de `EVP_Cipher()`; corrigido em 3.5.8.

**Decisão XFI:** não declarar todos estes CVEs exploráveis em qualquer router. Registar o pin OpenSSL como atrasado relativamente aos fixes upstream e priorizar atualização do pacote ou backports verificados. Confirmar opções de build (DTLS, QUIC, CMS/CMP e interfaces EVP) e uso dos consumidores antes da avaliação por equipamento. A tag oficial `v25.12.5` não deve ser confundida com prova de que uma imagem de router está instalada ou sem patches locais.

Fontes:
- https://github.com/openwrt/openwrt/blob/v25.12.5/package/libs/openssl/Makefile
- https://github.com/openssl/openssl/releases/tag/openssl-3.5.8
- https://github.com/openssl/openssl/releases/tag/openssl-3.5.9
- https://www.openssl-library.org/news/openssl-3.5-notes/index.html
- https://www.openssl-library.org/news/vulnerabilities-3.5/index.html

## 2. musl — 1.2.5 e CVE-2026-40200

A tag OpenWrt `v25.12.5` fixa musl `1.2.5`, hash upstream `a9a118bbe84d8764da0ea0d28b3ab3fae8477fc7e4085d90102b8596fc7c75e4`. A árvore contém os patches:
- `004-qsort-fix-leonardo-heap-corruption-from-bug-in-doubl.patch` (blob `87b18ecab79a86253372b46a8c8d46922e4ebd99`);
- `005-qsort-hard-preclude-oob-array-writes-independent-of-.patch` (blob `d8ff9803f200fc9056cf0e8541cb99cfac7af607`);
- `006-qsort-fix-shift-UB-in-shl-and-shr.patch` (blob `eab02d200e8de66d130f26d616dd8b16155138df`).

Estes nomes e patches apontam para um backport direcionado à falha qsort/heap Leonardo descrita em CVE-2026-40200. O advisory original limita a condição prática de stack corruption a entradas acima de cerca de 7 milhões em sistemas 32-bit; em 64-bit o limiar é impraticável para memória comum. **Estado:** provável mitigação por patch, mas confirmar conteúdo completo/diff e arquitetura do target antes de fechar.

Fontes:
- https://github.com/openwrt/openwrt/blob/v25.12.5/toolchain/musl/common.mk
- https://github.com/openwrt/openwrt/tree/v25.12.5/toolchain/musl/patches
- https://openwall.com/lists/musl/2026/04/10/3

## 3. Dropbear — 2025.89-r3

A tag `v25.12.5` fixa Dropbear `2025.89-r3`. A release upstream 2025.89 inclui a correção de CVE-2025-14282 (escalada via encaminhamento de sockets Unix), que afetava 2024.84 até 2025.88.

Existe um registo não revisto de CVE-2026-3706 relativo a validação de assinatura Ed25519/`unpackneg` em versões até 2025.89. O commit upstream `fdec3c90a15447bd538641d85e5a3e3ac981011d` adiciona validação `S < L`, mas o próprio commit declara que a maleabilidade da assinatura não tem impacto na forma como é usada no protocolo SSH. Não tratar a entrada não revista como vulnerabilidade remota confirmada sem análise de protocolo e contexto de uso. A patch não aparece como patch Dropbear separado na árvore OpenWrt consultada.

Fontes:
- https://github.com/openwrt/openwrt/blob/v25.12.5/package/network/services/dropbear/Makefile
- https://github.com/mkj/dropbear/releases/tag/DROPBEAR_2025.89
- https://github.com/mkj/dropbear/commit/fdec3c90a15447bd538641d85e5a3e3ac981011d
- https://github.com/advisories/GHSA-87g2-jprq-4cmc

## 4. Kernel — 6.12.94

O ficheiro `target/linux/generic/kernel-6.12` fixa Linux `6.12.94` com SHA-256 `e998a232b9418db3301cb58468e291a4f41d6ab8306029b30d991f56251dc8d2`. A análise aqui confirma apenas o pin de versão/hash, não a ausência de CVEs. O kernel é selecionado por target e configuração; a próxima etapa deve cruzar o changelog 6.12.94, patches OpenWrt e advisories upstream com os targets que o XFI venha a homologar.

Fonte: https://github.com/openwrt/openwrt/blob/v25.12.5/target/linux/generic/kernel-6.12

## Ações seguintes

1. Atualizar o registo de advisories para OpenSSL e priorizar 3.5.9 ou backports verificados; não alterar routers.
2. Inspecionar os patches musl 004–006 para confirmar a correção exata e arquitetura afetada.
3. Validar a natureza e impacto de CVE-2026-3706 contra o código/protocolo SSH, sem elevar advisory não revisto a facto confirmado.
4. Fazer triagem completa do kernel 6.12.94 por target, mantendo o estado de risco dependente de imagem.
5. Só depois, gerar matriz por equipamento quando o inventário real de routers estiver disponível.


## Nota de precisão — patch local OpenSSL 010 (2026-10-13)

A árvore OpenWrt contém `package/libs/openssl/patches/010-fix-aes-gcm-siv-cipher.patch` (blob `deca8f1e569f19508f6121cd543aefef75d0a316`). O patch corrige tratamento de mensagens de comprimento zero em AES-GCM-SIV/AES-SIV. Por isso, o CVE-2026-75803 foi separado do grupo de CVEs sem backport identificado e classificado no CSV como `LOCAL_PATCH_RELEVANT_REQUIRES_CVE_MAPPING`. A correspondência exata entre este patch downstream e o advisory upstream continua pendente; não contar esse CVE como definitivamente não corrigido nem como fechado.


## Atualização do kernel upstream — 2026-10-13

A listagem oficial do kernel.org já apresenta **Linux 6.12.112**, publicado em 2026-10-03, enquanto o pin da tag OpenWrt `v25.12.5` é **6.12.94**, de 2026-06-19. São 18 incrementos de manutenção estável entre o pin e o release upstream listado. Isto não prova automaticamente que cada correção em falta seja aplicável ou não esteja backportada pela árvore OpenWrt, mas aumenta a prioridade da revisão de patches.

**Ação:** comparar os changelogs `6.12.95` a `6.12.112` com `target/linux/generic/backport-6.12`, `pending-6.12` e patches específicos por target. Até essa comparação, classificar o kernel como **`UPSTREAM_STABLE_LAG_REQUIRES_PATCH_DIFF`**, não como vulnerável por CVE específico.

Fonte upstream: https://www.kernel.org/pub/linux/kernel/v6.x/ (listagem oficial com ChangeLog-6.12.112 de 2026-10-03).


## Continuação — correção do mapeamento OpenSSL e confirmação musl (2026-10-13)

### OpenSSL: o patch local 010 NÃO corrige CVE-2026-75803

CVE-2026-75803 diz respeito à verificação de tag AEAD omitida em operações de decifragem com ciphertext vazio para **ChaCha20-Poly1305 e AES-OCB** quando a aplicação usa `EVP_Cipher()`. O patch OpenWrt `010-fix-aes-gcm-siv-cipher.patch` trata mensagens de comprimento zero em **AES-GCM-SIV e AES-SIV**. São algoritmos/caminhos distintos; o patch local não é mitigação equivalente para CVE-2026-75803.

- OpenSSL 3.5.8: https://github.com/openssl/openssl/releases/tag/openssl-3.5.8
- Advisory: https://github.com/advisories/GHSA-vr27-9w4v-hjw2
- Patch local v25.12.5: https://github.com/openwrt/openwrt/blob/v25.12.5/package/libs/openssl/patches/010-fix-aes-gcm-siv-cipher.patch

**Estado no release estável v25.12.5:** OpenSSL 3.5.7-r1, anterior à correção de 3.5.8; não foi encontrado backport específico da correção EVP AEAD na árvore do tag. Prioridade alta para atualização/backport. Aplicabilidade depende de algoritmos compilados e consumidores que usem `EVP_Cipher()` com ciphertext vazio; não declarar exposição por router sem verificar imagem/configuração.

### Desenvolvimento posterior não equivale a release estável

O changelog público de 25.12.6 lista alterações posteriores à tag v25.12.5, incluindo OpenSSL 3.5.8/3.5.9, remoção da parte AES-GCM-SIV do patch local e atualizações do kernel até 6.12.112 em alguns targets. Contudo, a referência Git `v25.12.6` não foi resolvida como tag no GitHub nesta consulta. Estes commits são evidência de desenvolvimento posterior, não prova de release estável publicada. A base desta revisão permanece v25.12.5 até uma tag/release verificável.

Fontes: https://openwrt.org/releases/25.12/changelog-25.12.6 ; https://openwrt.org/releases/25.12/notes-25.12.5 ; https://github.com/openwrt/openwrt/commit/e594c1d ; https://github.com/openwrt/openwrt/commit/c9e33c7 ; https://github.com/openwrt/openwrt/commit/12d27e8

### musl: CVE-2026-40200 — backport confirmado na fonte

Inspeção direta dos patches no tag v25.12.5:
- `004`: corrige `pntz()`, causa raiz da corrupção de stack; a mensagem referencia explicitamente CVE-2026-40200.
- `005`: amplia o array de trabalho para tamanho potência de dois e mascara índices para evitar escritas fora dos limites.
- `006`: evita comportamento indefinido em shifts quando o deslocamento é igual à largura de `size_t`.

**Estado documental:** `BACKPORT_CONFIRMED_IN_TAG_SOURCE`. Isto confirma presença dos patches na fonte do tag, não prova que uma imagem específica os inclua. Fontes: https://github.com/openwrt/openwrt/blob/v25.12.5/toolchain/musl/patches/004-qsort-fix-leonardo-heap-corruption-from-bug-in-doubl.patch ; https://github.com/openwrt/openwrt/blob/v25.12.5/toolchain/musl/patches/005-qsort-hard-preclude-oob-array-writes-independent-of-.patch ; https://github.com/openwrt/openwrt/blob/v25.12.5/toolchain/musl/patches/006-qsort-fix-shift-UB-in-shl-and-shr.patch

### Próximas ações

1. Completar a matriz OpenSSL com todos os CVEs listados nas releases 3.5.8/3.5.9, condicionando a aplicabilidade a feature/build/uso.
2. Comparar changelogs Linux 6.12.95–6.12.112 com backport/pending e patches específicos por target.
3. Concluir a triagem Dropbear CVE-2026-3706 sem classificar o advisory como explorável enquanto o impacto SSH não estiver demonstrado.
