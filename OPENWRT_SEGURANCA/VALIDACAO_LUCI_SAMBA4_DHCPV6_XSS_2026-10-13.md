# Validação LuCI — Samba4 ACL e DHCPv6 lease hostname XSS

**Data:** 2026-10-13  
**Feed LuCI pinada por OpenWrt v25.12.5:** `128a7812f4be233c5dd7f7466f534fd888785caf`.

## 1. luci-app-samba4 — GHSA-vx64-mmp7-h36c (High)

- **Risco descrito:** uma ACL de leitura que conceda `file.exec` sobre `/usr/sbin/smbd` permite ao utilizador delegado fornecer argumentos ao daemon e, em determinadas condições, executar comandos como root.
- **Evidência do pin:** [ACL de Samba4](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-samba4/root/usr/share/rpcd/acl.d/luci-app-samba4.json), blob SHA `e911e60e07d3a1e6360b68246dc4ec2a5e4e5ce5`. A ACL já não concede `exec` no caminho genérico `/usr/sbin/smbd`; concede apenas o objeto restrito `/usr/sbin/smbd -V`, conforme indicado nas notas oficiais.
- **Conclusão documental:** a ACL da feed pinada restringe o grant descrito no advisory. Estado `RELEASE_NOTES_AND_FEED_PIN_CONFIRMED`.
- **Aplicabilidade:** requer aplicação Samba4 instalada e conta autenticada com a ACL delegada relevante. Não confirma o estado de um dispositivo específico.

Advisory: https://github.com/openwrt/luci/security/advisories/GHSA-vx64-mmp7-h36c

## 2. luci-mod-status — GHSA-686p-p8p9-x6fh (High), XSS de hostname DHCP/DHCPv6

- **Risco descrito:** um cliente adjacente não autenticado pode fornecer um FQDN DHCPv6 com HTML; o hostname é preservado nas leases e pode alcançar tabelas de estado LuCI, executando JavaScript na origem administrativa se for renderizado como HTML.
- **Evidência do pin:** [vista de leases DHCP](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/modules/luci-mod-status/htdocs/luci-static/resources/view/status/include/40_dhcp.js), blob SHA `7be0eb9046c919230f5f8f99773fc567eef91979`. A apresentação do hostname usa `'%h'.format(host || '-')` na tabela IPv4 (linha 143) e o mesmo padrão de escaping HTML na tabela IPv6. A implementação conjunta com a correção do `odhcpd` para a lease é necessária para fechar o caminho de ponta a ponta.
- **Conclusão documental:** a saída do hostname está escapada na vista de estado da feed pinada e as notas oficiais descrevem a correção conjunta com odhcpd. Estado `RELEASE_NOTES_AND_FEED_PIN_CONFIRMED`.
- **Aplicabilidade:** requer interface LuCI exposta a administradores que visualizem as tabelas e cliente na rede adjacente; não é equivalente a execução remota de comandos no router.

Advisory: https://github.com/openwrt/luci/security/advisories/GHSA-686p-p8p9-x6fh

## Limites

A revisão confirma o código relevante na feed LuCI fixada por `v25.12.5`, não a imagem binária, pacote instalado, ACL efetiva ou configuração de um router XFI. Não foram executados PoCs nem testes físicos. Zabbix continua em pausa.

## Fontes

- https://github.com/openwrt/openwrt/blob/v25.12.5/feeds.conf.default
- https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-samba4/root/usr/share/rpcd/acl.d/luci-app-samba4.json
- https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/modules/luci-mod-status/htdocs/luci-static/resources/view/status/include/40_dhcp.js
- https://github.com/openwrt/luci/security/advisories/GHSA-vx64-mmp7-h36c
- https://github.com/openwrt/luci/security/advisories/GHSA-686p-p8p9-x6fh
- https://openwrt.org/releases/25.12/notes-25.12.5
