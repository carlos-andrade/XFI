# Ficha de inventário de router — XFI OpenWrt Security

**Estado:** TEMPLATE — nenhum equipamento foi fornecido ou validado  
**Data de criação:** 2026-10-13  
**Governança:** https://github.com/carlos-andrade/GOVERNANCA  
**Repositório:** https://github.com/carlos-andrade/XFI

> Não preencher por inferência. Manter como **NÃO FORNECIDO** até existir evidência do equipamento, etiqueta, firmware ou saída de comandos recolhida com autorização. Não introduzir segredos, chaves Wi-Fi, passwords ou tokens.

## 1. Identificação física

| Campo | Valor |
|---|---|
| Fabricante | NÃO FORNECIDO |
| Modelo comercial exato | NÃO FORNECIDO |
| Revisão de hardware (H/W ver.) | NÃO FORNECIDO |
| Região/SKU | NÃO FORNECIDO |
| Número de série | NÃO REGISTAR NESTE REPOSITÓRIO |
| Origem/fornecedor | NÃO FORNECIDO |
| Estado (por adquirir / disponível / em produção) | NÃO FORNECIDO |
| Responsável pelo inventário | NÃO FORNECIDO |
| Data da recolha | NÃO FORNECIDO |
| Evidência da etiqueta/ficha oficial | NÃO FORNECIDO |

## 2. Firmware e plataforma

| Campo | Valor |
|---|---|
| Target/subtarget OpenWrt | NÃO DETERMINADO |
| Device profile | NÃO DETERMINADO |
| Versão instalada | NÃO DETERMINADA |
| Build ID / revision | NÃO DETERMINADO |
| Hash SHA-256 da imagem | NÃO FORNECIDO |
| Método de instalação/recuperação documentado | NÃO FORNECIDO |
| Firmware OEM de origem | NÃO FORNECIDO |
| Bootloader/recovery mode | NÃO FORNECIDO |
| Acesso serial/console disponível | NÃO FORNECIDO |

## 3. Capacidades relevantes

| Campo | Valor |
|---|---|
| SoC/arquitetura | NÃO DETERMINADO |
| CPU / endianness | NÃO DETERMINADO |
| RAM / flash | NÃO DETERMINADO |
| Ethernet / switch / offload | NÃO DETERMINADO |
| Rádio / chipset / driver | NÃO DETERMINADO |
| Modos Wi-Fi / bandas | NÃO DETERMINADO |
| Modem/USB/PCIe/SDIO | NÃO DETERMINADO |
| Secure boot / assinatura | NÃO DETERMINADO |

## 4. Configuração e exposição (recolher sem segredos)

| Campo | Valor |
|---|---|
| Papel de rede (gateway/AP/bridge/outro) | NÃO DETERMINADO |
| Interfaces e zonas de firewall | NÃO FORNECIDO |
| Acesso administrativo exposto à WAN | NÃO VERIFICADO |
| UPnP habilitado | NÃO VERIFICADO |
| Tailscale / Travelmate / Samba / outras aplicações LuCI | NÃO VERIFICADO |
| NDP relay / DHCPv6 | NÃO VERIFICADO |
| Generic XDP / BPF | NÃO VERIFICADO |
| Driver MMCI presente | NÃO VERIFICADO |
| OpenSSL/odhcpd/LuCI instalados e versões | NÃO VERIFICADO |

## 5. Evidência recolhida

| Evidência | Referência/hash/data |
|---|---|
| Fotografia da etiqueta (guardar fora de repositório público) | NÃO FORNECIDO |
| Ficha oficial do fabricante | NÃO FORNECIDO |
| Saída de `ubus call system board` (redigida) | NÃO FORNECIDO |
| Saída de `cat /etc/openwrt_release` | NÃO FORNECIDO |
| Pacotes instalados relevantes | NÃO FORNECIDO |
| Configuração redigida, sem segredos | NÃO FORNECIDO |
| Backup de configuração cifrado e localização segura | NÃO FORNECIDO |

## 6. Critérios de validação

- [ ] Fabricante, modelo e revisão física confirmados por evidência.
- [ ] Target e device profile confirmados em fontes oficiais OpenWrt.
- [ ] Versão/build e hash da imagem recolhidos.
- [ ] Método de recovery testável e backup verificado.
- [ ] Pacotes e serviços relevantes inventariados.
- [ ] Configuração analisada sem expor credenciais.
- [ ] CVEs correlacionados com o target, configuração e pacotes efetivos.
- [ ] Revisão independente concluída antes de qualquer homologação.

## 7. Decisão

**Estado atual:** BLOQUEADO POR AUSÊNCIA DE INVENTÁRIO REAL.  
Não declarar o equipamento vulnerável, corrigido ou homologado enquanto os campos essenciais não tiverem evidência. Não instalar firmware nem executar mudanças remotas com base apenas nesta ficha.
