# Catálogo de fontes oficiais OpenWrt

**Revisão do catálogo:** 2026-10-13. Inventário inicial, agora incluindo índices de advisories, releases, downloads e repositório upstream; não exaustivo. Os resultados do verificador automático indicam apenas acessibilidade HTTP; não substituem revisão humana de conteúdo, versão ou aplicabilidade.

| Tema | Fonte oficial | Utilização |
|---|---|---|
| Hardening geral | https://openwrt.org/docs/guide-user/security/openwrt_security | Passwords, atualização e práticas gerais |
| Funcionalidades de segurança | https://openwrt.org/docs/guide-user/security/security-features | Mecanismos de segurança e considerações de acesso |
| Acesso seguro | https://openwrt.org/docs/guide-user/security/secure.access | Autenticação e acesso remoto |
| Overview do firewall | https://openwrt.org/docs/guide-user/firewall/overview | Modelo firewall4 e nftables |
| Configuração firewall | https://openwrt.org/docs/guide-user/firewall/firewall_configuration | UCI, zonas, regras e integração fw4 |
| Referência de firewall | https://openwrt.org/docs/guide-user/firewall/start | Índice de regras, IPv4/IPv6, NAT e UPnP |
| Guia avançado nftables | https://openwrt.org/docs/guide-user/firewall/misc/nftables | Uso manual avançado; a própria página alerta para conflito com regras geradas por fw4 |
| Wi-Fi convidado | https://openwrt.org/docs/guide-user/network/wifi/guestwifi/start | Rede convidada e isolamento |
| Exemplo de guest WLAN | https://openwrt.org/docs/guide-user/network/wifi/guestwifi/guest-wlan | Exemplo a validar antes de reutilizar |
| Encriptação Wi-Fi | https://openwrt.org/docs/guide-user/network/wifi/encryption | WPA3/WPA2 e compatibilidade |
| Wi-Fi overview | https://openwrt.org/docs/guide-user/network/wifi/start | Navegação por tópicos Wi-Fi |
| DNS/DHCP | https://openwrt.org/docs/guide-user/base-system/dhcp | Opções UCI/dnsmasq e rebinding |
| DNS sobre HTTPS | https://openwrt.org/docs/guide-user/services/dns/doh_dnsmasq_https-dns-proxy | DoH e implicações operacionais |
| Sysupgrade | https://openwrt.org/docs/guide-user/installation/generic.sysupgrade | Preparação, backup, compatibilidade e atualização |
| Método sysupgrade | https://openwrt.org/docs/guide-user/installation/installation_methods/sysupgrade | Métodos e dispositivos compatíveis; confirmar revisão individual |
| Preservação de pacotes | https://openwrt.org/docs/guide-user/installation/sysupgrade.packages | Pacotes/dados que podem não sobreviver a upgrade |
| Backup e restauro | https://openwrt.org/docs/guide-user/troubleshooting/backup_restore | Procedimentos de backup/restauro |
| Table of Hardware | https://openwrt.org/toh/start | Índice oficial de hardware; confirmar a página do dispositivo e revisão |
| Vista de hardware | https://openwrt.org/toh/views/toh_standard_all | Campos técnicos e limitações de hardware |
| Firmware Selector | https://firmware-selector.openwrt.org/ | Identificar imagens; validar cuidadosamente modelo/revisão e tipo de imagem |

| Advisories de segurança | https://openwrt.org/advisory/start | Índice de avisos de segurança; confirmar CVE, versões afetadas e correções na fonte do aviso |
| Releases OpenWrt | https://openwrt.org/releases/start | Índice de releases e documentação associada |
| Downloads oficiais | https://downloads.openwrt.org/ | Diretório oficial de imagens, checksums e artefactos; confirmar target e revisão |
| Repositório upstream | https://github.com/openwrt/openwrt | Código-fonte upstream e histórico do projeto |
| Repositório Git upstream | https://git.openwrt.org/?p=openwrt/openwrt.git;a=summary | Repositório oficial de código OpenWrt e metadados do projeto |\n| Commits upstream | https://git.openwrt.org/?p=openwrt/openwrt.git;a=shortlog | Acompanhar alterações recentes; commits isolados não são, por si só, avisos de segurança |
| Issues upstream | https://github.com/openwrt/openwrt/issues | Acompanhamento de problemas reportados; verificar estado e confirmação pelos mantenedores |

## Regras de uso das fontes
- Para fontes GitHub, o verificador aceita apenas URLs HTTPS sob `github.com/openwrt/`. O host `git.openwrt.org` também é permitido para o repositório oficial upstream; não ampliar a allowlist sem revisão.
- A Table of Hardware é um índice, não substitui a página individual do dispositivo.
- Não selecionar firmware apenas pelo nome comercial: confirmar revisão física, target/subtarget e tipo de imagem.
- Em OpenWrt 22.03 e posteriores, fw4 gera regras nftables por omissão; não misturar configurações manuais avulsas sem compreender a interação.
- Sysupgrade substitui partes da instalação; pacotes instalados manualmente podem ter de ser reinstalados e configurações podem precisar de migração.
- O estado de suporte e a release mais recente são dinâmicos. Consultar a fonte oficial na data de cada homologação em vez de fixar números de versão neste catálogo.

## Metadados obrigatórios de cada fonte
URL canónica, título, categoria, timestamp de consulta UTC, data upstream se disponível, release aplicável, resumo próprio, estado de revisão, última verificação, responsável e relações com perfis/configuração. Para cópia de conteúdo, registar também licença e atribuição.

## Próxima expansão
Incluir advisories de segurança, releases e changelogs, repositórios/commits oficiais, páginas de dispositivo e dados de compatibilidade de pacotes. Cada fonte adicional precisa de uma allowlist explícita e de critérios de recolha.
