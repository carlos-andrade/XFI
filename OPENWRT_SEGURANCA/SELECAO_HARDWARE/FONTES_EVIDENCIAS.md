# Fontes e evidências — seleção de hardware

**Data da consulta:** 2026-10-13  
**Prioridade:** documentação oficial OpenWrt, páginas dos fabricantes e ofertas comerciais claramente identificadas. A pesquisa é uma fotografia temporal; consultar de novo antes da compra.

## Fontes técnicas principais

| Fonte | O que suporta | Observações/limites |
|---|---|---|
| [OpenWrt Table of Hardware](https://openwrt.org/toh/start) | Índice principal para localizar hardware suportado | A entrada tem de corresponder à revisão; abrir a página individual. |
| [OpenWrt Buyers' Guide](https://openwrt.org/toh/buyerguide) | Critérios de compra e advertência de que OpenWrt não recomenda uma marca universalmente | Escolha depende de necessidades e do hardware. |
| [OpenWrt — dispositivos suportados](https://openwrt.org/supported_devices) | Requisitos de hardware e alerta contra dispositivos 8 MB flash/64 MB RAM | O mínimo técnico não é necessariamente recomendável para uma frota nova. |
| [OpenWrt — vista Wi-Fi 6/802.11ax](https://openwrt.org/toh/views/toh_available_16128_ax-wifi) | Filtro de dispositivos com Wi-Fi 6 e critérios de RAM/flash | A página alerta para limitações de certos chipsets e procedimentos especiais. |
| [OpenWrt — GL.iNet](https://openwrt.org/toh/gl.inet/start) | Índice de dispositivos GL.iNet documentados | Índice não garante suporte atual a todos os modelos. |
| [GL.iNet — Firmware Versions](https://www.gl-inet.com/pages/firmware-versions/) | Versão/estado e base OpenWrt declarados pelo fabricante | A tabela consultada identifica GL-MT6000 4.9.1 como MTK SDK/OpenWrt 21.02 e uma linha 4.9.0-op24 baseada em OpenWrt 24.10. Distinguir do upstream. |
| [GL.iNet — download center GL-MT6000](https://dl.gl-inet.com/?model=mt6000) | Firmware OEM e versões publicadas | A versão OEM não deve ser presumida equivalente à release upstream. |
| [OpenWrt — GL-MT6000](https://openwrt.org/toh/hwdata/gl.inet/gl.inet_gl-mt6000) | Dados técnicos do Flint 2 | A ficha consultada listou suporte desde 23.05.3 e Supported Current Rel 25.12.5 em 2026-10-13; confirmar novamente antes da compra. |
| [OpenWrt Firmware Selector — GL-MT6000](https://firmware-selector.openwrt.org/?id=glinet_gl-mt6000&target=mediatek%2Ffilogic) | Imagens upstream específicas e hashes | Selecionar a imagem certa e seguir a página de instalação do modelo. |
| [Banana Pi EU — OpenWrt One](https://banana-pi.eu/produit/openwrt-one-ap-24-xy/) | Especificações e preço europeu publicado | Confirmar envio, garantia, stock e custo instalado para Portugal. |
| [OpenWrt — TP-Link Archer AX23 v1](https://openwrt.org/toh/tp-link/archer_ax23_v1) | Suporte e avisos de revisão para AX23 v1/v1.20 | A página alerta que v2 tem SoC diferente e RAM insuficiente; menciona relatos de comportamento irregular em versões posteriores a 23.05.4. |
| [TP-Link Portugal — AX23 v1](https://www.tp-link.com/pt/support/download/archer-ax23/v1/) | Firmware OEM e instruções de identificação de versão/região | A página alerta que firmware errado de versão/região pode danificar o dispositivo. |
| [OpenWrt — Cudy](https://openwrt.org/toh/cudy/start) | Existência de páginas para WR3000 e variantes, TR3000, APs e outros | Cada variante tem página própria. Não transferir uma aprovação entre modelos. |
| [OpenWrt — segurança/hardening](https://openwrt.org/docs/guide-user/security/openwrt_security) | Princípios de hardening, firewall WAN e segurança da gestão | Firewall WAN por padrão não elimina risco interno. |
| [OpenWrt — backup/restauro](https://openwrt.org/docs/guide-user/troubleshooting/backup_restore) | Preparação de backup e restauro | Backup deve ser testado e protegido. |
| [OpenWrt — sysupgrade](https://openwrt.org/docs/guide-user/installation/generic.sysupgrade) | Efeito de atualização e pacotes não preservados | Exige imagem correta e planeamento do restauro. |

## Fontes comerciais consultadas

| Produto | Fonte | Preço observado | Limitação |
|---|---|---:|---|
| Cudy WR3000 | [KuantoKusta](https://www.kuantokusta.pt/p/10175380/cudy-router-wireless-ax3000-wr3000-dual-band-wifi-6-gigabit-wr3000) | ~43,21 € com envio na oferta indicada | Oferta/vendedor terceiro; confirmar stock, revisão e fatura. |
| Cudy WR3000 | [Leroy Merlin](https://www.leroymerlin.pt/produtos/roteador-sem-fio-cudy-wr3000-gigabit-ethernet-dual-band-2-4-ghz-5-ghz-preto-91037198.html) | 55,65 € | Venda online por terceiro; confirmar condições de devolução. |
| Cudy WR3000S | [Worten](https://www.worten.pt/produtos/router-cudy-wr3000s-branco-wi-fi-ethernet-lan-mrkean-6971690793203) | 58,66 € | Marketplace, vendedor MS2 Digital; variante diferente de WR3000. |
| TP-Link Archer AX23 | [KuantoKusta](https://www.kuantokusta.pt/p/6681502/tp-link-wireless-ax1800-archer-ax23-dual-band-wifi-6-gigabit-archerax23) | ~67,76 € | A oferta não garante revisão compatível com OpenWrt. |
| GL.iNet GL-MT6000 | [Loja oficial GL.iNet UE](https://www.gl-inet.com/en-de/products/gl-mt6000) | 165,37 € | IVA indicado como incluído; confirmar entrega/stock para Portugal. |
| GL.iNet GL-MT3000 | [Loja oficial GL.iNet UE](https://www.gl-inet.com/en-de/products/gl-mt3000) | 102,85 € | IVA indicado como incluído; categoria de router de viagem. |
| OpenWrt One | [Banana Pi EU](https://banana-pi.eu/produit/openwrt-one-ap-24-xy/) | 174,24 € com IVA | Confirmar envio, garantia e necessidade de switch/AP. |

Detalhes e interpretação em [PESQUISA_COMERCIAL_PT.md](PESQUISA_COMERCIAL_PT.md). Os preços são observações pontuais, não cotações vinculativas.

## Registo de observações

### GL.iNet GL-MT6000 (Flint 2)
- Evidência upstream: página OpenWrt lista suporte atual 25.12.5 e recuperação U-Boot TFTP/serial e web recovery.
- Evidência do fabricante: matriz de firmware consultada identifica estável 4.9.1 com base OpenWrt 21.02 (SDK MTK) e 4.9.0-op24 baseada em OpenWrt 24.10.
- Interpretação: candidato forte para laboratório se o XFI assumir e testar firmware upstream ou aceitar explicitamente o ciclo de suporte OEM. Não dizer que “firmware estável do fabricante” e “OpenWrt upstream atual” são a mesma coisa.
- Pendências: recuperação ensaiada, preço/garantia UE, desempenho Wi-Fi, firewall, SQM/VPN, atualização e downgrade testados.

### OpenWrt One
- Evidência comercial: loja europeia lista 174,24 € com IVA.
- Interpretação: candidato interessante para uma plataforma voltada para OpenWrt, mas deve ser comparado pelo custo total de instalação e pela arquitetura de portas.
- Pendências: envio/garantia para Portugal, stock, recuperação, desempenho Wi-Fi e necessidade de switch/AP.

### TP-Link Archer AX23
- Evidência: página OpenWrt v1/v1.20 e dados técnicos específicos; preço comercial não identifica a revisão.
- Interpretação: não usar o nome “AX23” como identificador suficiente. Confirmar etiqueta/revisão e investigar avisos antes de avançar.

### Cudy
- Evidência: índice OpenWrt contém páginas distintas para WR3000 e variantes; preço público baixo foi encontrado para WR3000 e WR3000S.
- Interpretação: útil para construir uma linha de orçamento, mas sem extrapolar suporte entre variantes.
- Pendências: revisão/SKU exatos, página de dispositivo, release atual, imagem e recuperação.

## Classificação de evidências

- **A — evidência primária direta:** ficha oficial da revisão/modelo ou documentação do fabricante.
- **B — evidência indireta:** página índice ou comparador comercial.
- **C — evidência comunitária/relatos:** útil para descobrir risco, carece de reprodução.
- **T — teste XFI:** requer registo reproduzível com equipamento físico.

Nenhum candidato tem classificação T nem aprovação final XFI.

## Política de atualização

Atualizar quando mudar release, surgir aviso relevante, mudar o estado do fabricante, aparecer nova revisão, uma unidade ser ensaiada ou for feita nova cotação local.
