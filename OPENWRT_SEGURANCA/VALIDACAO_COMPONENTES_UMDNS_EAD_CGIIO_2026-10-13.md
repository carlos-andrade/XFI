# Atualização de revisão — OpenWrt 25.12.5

Data: 2026-10-13

## Evidência confirmada

- **umdns:** Makefile da tag v25.12.5 declara PKG_SOURCE_DATE=2026-06-16 e PKG_SOURCE_VERSION=1b5e7bf1cec775b89f1a6068dc0b9df3593b5986. Blob SHA: 40ee5ed4922e14b72a90100ac43994f20288574e. O commit de atualização 5b2c8f4ff94ef7c339586c8a59a684009f1b7194 liga este pin à correção GHSA-jg8f-fhfw-jg46.
- **ead:** a release 25.12.5 lista CVE-2026-55490; o ficheiro ead.c na tag v25.12.5 valida o comprimento da mensagem antes da subtração. A aplicabilidade depende de o serviço estar presente/ativo na imagem.
- **cgi-io:** o advisory GHSA-jw5r-xhf5-2xcq identifica CVE-2026-62947 e indica versões afetadas até OpenWrt 25.12.4. A normalização do identificador no CSV e a confirmação do pin do feed continuam pendentes.

## Limites

- A evidência é documental e de código-fonte/tag; não comprova a imagem instalada num router.
- Não houve build, teste físico ou alteração de router.
- A frente Zabbix continua em pausa.

## Fontes

- https://openwrt.org/releases/25.12/notes-25.12.5
- https://github.com/openwrt/openwrt/blob/v25.12.5/package/network/services/umdns/Makefile
- https://github.com/openwrt/openwrt/blob/v25.12.5/package/network/services/ead/src/ead.c
- https://github.com/openwrt/openwrt/security/advisories/GHSA-jw5r-xhf5-2xcq


## Fecho da validação do pin cgi-io — 2026-10-13

**Resultado: pin de código-fonte confirmado na cadeia de feed declarada pela tag OpenWrt v25.12.5.**

1. O ficheiro oficial `feeds.conf.default` na tag [v25.12.5](https://github.com/openwrt/openwrt/blob/v25.12.5/feeds.conf.default), blob SHA `23962703cf641edd8d4e2ec2eef6725ca9fca396`, fixa o feed `packages` no commit `5caa62e0bc9f7fb9b0c12a23267bceb7724214dd`.
2. O [Makefile de cgi-io nesse commit do feed](https://github.com/openwrt/packages/blob/5caa62e0bc9f7fb9b0c12a23267bceb7724214dd/net/cgi-io/Makefile), blob SHA `e8b6d2fc8ad127277e4cfba94c38bb3c1203a016`, fixa `PKG_SOURCE_DATE=2026-06-28` e `PKG_SOURCE_VERSION=7314451cb99692c0862a70c3307ee08bd2fbd9c0`.
3. O [main.c do cgi-io no pin de fonte](https://github.com/openwrt/cgi-io/blob/7314451cb99692c0862a70c3307ee08bd2fbd9c0/main.c), blob SHA `09792fadfe381240a92c0a5e25f33a330ac926f7`, canonicaliza o caminho de download antes de autorizar o acesso ACL (`main.c`, por volta da linha 547).
4. Comparação com o baseline afetado `658b14b`: o código afetado fazia a verificação ACL sobre `fields[3]` sem canonicalização e depois chamava `open(fields[3], O_RDONLY)` (linhas 540/557; blob consultado `806d7153cde28d99f1c4ab9801177adfa61d3d1b`). O pin selecionado para a cadeia 25.12.5 contém a correção.

### Decisão de registo

- Identificador normalizado: **CVE-2026-62947 / GHSA-jw5r-xhf5-2xcq**.
- Estado do CSV: `RELEASE_NOTES_AND_PACKAGE_PIN_CONFIRMED`.
- Isto confirma o pin do código-fonte na cadeia de feed declarada pela tag e a presença da correção no código desse pin.
- **Não confirma** o conteúdo binário de cada imagem publicada, uma build personalizada, nem o pacote instalado em qualquer router XFI. A validação de dispositivo exige inventário, versão/imagem e verificação local.
- Fonte do advisory: https://github.com/openwrt/openwrt/security/advisories/GHSA-jw5r-xhf5-2xcq
- Notas da release: https://openwrt.org/releases/25.12/notes-25.12.5
