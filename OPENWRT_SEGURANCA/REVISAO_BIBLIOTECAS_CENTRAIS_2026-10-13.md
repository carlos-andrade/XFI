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
