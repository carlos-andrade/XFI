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
