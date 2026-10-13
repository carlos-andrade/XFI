# Validação LuCI — advanced-reboot e adblock-fast

**Data:** 2026-10-13  
**Base analisada:** feed LuCI fixado por OpenWrt `v25.12.5`, commit `128a7812f4be233c5dd7f7466f534fd888785caf`.

## 1. luci-app-advanced-reboot — CVE-2026-55897 / GHSA-vj96-f37g-37f6

- **Severidade publicada:** High, CVSS 8.8.
- **Risco:** o advisory descreve execução root por uma ACL de leitura que concedia `file.exec` sobre `/bin/sh`.
- **Evidência do pin:** [ACL na feed fixada](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-advanced-reboot/root/usr/share/rpcd/acl.d/luci-app-advanced-reboot.json), blob SHA `281d59c8d24996c4c880c4baf99ce2c3a0f8c089`. A ACL de leitura contém apenas o método ubus `luci.advanced-reboot.obtain_device_info`; não concede `/bin/sh` nem `file.exec`.
- **Conclusão documental:** a condição vulnerável específica descrita no advisory não está presente na ACL da feed fixada por `v25.12.5`. Estado `RELEASE_NOTES_AND_FEED_PIN_CONFIRMED`.
- **Aplicabilidade:** depende da aplicação instalada e de contas ACL delegadas. Não comprova a ACL do binário/pacote de um router XFI.

Fonte advisory: https://github.com/openwrt/luci/security/advisories/GHSA-vj96-f37g-37f6

## 2. luci-app-adblock-fast — CVE-2026-55159 / GHSA-ggpf-xrph-wg5v

- **Severidade publicada:** High.
- **Risco:** o advisory descreve injeção de linhas de cron através de caracteres de nova linha em `setCronEntry`, permitindo execução como root por utilizadores com ACL de escrita da aplicação.
- **Evidência do pin:** [backend ucode na feed fixada](https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-adblock-fast/root/usr/share/rpcd/ucode/luci.adblock-fast), blob SHA `f7062814454328a5dd0bdbe7d7e724c410c95ae3`. O código documenta `syncCron` como método que substitui `setCronEntry`, valida o horário no servidor com `cron_field()` e `CRON_MODES`, e monta a linha de cron a partir de valores validados antes de escrever `/etc/crontabs/root`.
- **Conclusão documental:** o backend da feed fixada contém a abordagem de correção para rejeitar entradas arbitrárias e impedir que input RPC injete linhas cron. Estado `RELEASE_NOTES_AND_FEED_PIN_CONFIRMED`.
- **Aplicabilidade:** depende da aplicação instalada e das ACLs delegadas. Não comprova o binário instalado num router XFI.

Fonte advisory: https://github.com/openwrt/luci/security/advisories/GHSA-ggpf-xrph-wg5v

## Limites e decisão operacional

As notas oficiais de [OpenWrt 25.12.5](https://openwrt.org/releases/25.12/notes-25.12.5) listam ambas as correções. A inspeção acima confirma os elementos de código relevantes na revisão do feed fixada pela tag. Não foram executados PoCs, testes em router ou alterações de produção. Confirmar imagem, pacote, configuração e ACLs reais antes de fechar o risco por equipamento. Zabbix continua em pausa.

## Fontes primárias

- https://github.com/openwrt/openwrt/blob/v25.12.5/feeds.conf.default
- https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-advanced-reboot/root/usr/share/rpcd/acl.d/luci-app-advanced-reboot.json
- https://github.com/openwrt/luci/blob/128a7812f4be233c5dd7f7466f534fd888785caf/applications/luci-app-adblock-fast/root/usr/share/rpcd/ucode/luci.adblock-fast
- https://github.com/openwrt/luci/security/advisories/GHSA-vj96-f37g-37f6
- https://github.com/openwrt/luci/security/advisories/GHSA-ggpf-xrph-wg5v
