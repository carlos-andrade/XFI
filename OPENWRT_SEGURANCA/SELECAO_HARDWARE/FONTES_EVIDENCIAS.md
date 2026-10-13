# Fontes e evidências — seleção de hardware

**Data da consulta:** 2026-10-13  
**Prioridade:** documentação oficial OpenWrt e páginas oficiais dos fabricantes. A pesquisa é uma fotografia temporal; consultar de novo antes da compra.

## Fontes principais

| Fonte | O que suporta | Observações/limites |
|---|---|---|
| [OpenWrt Table of Hardware](https://openwrt.org/toh/start) | Índice principal para localizar hardware suportado | A entrada tem de corresponder à revisão e pode conter dados incompletos. Abrir a página individual. |
| [OpenWrt — vista Wi-Fi 6/802.11ax](https://openwrt.org/toh/views/toh_available_16128_ax-wifi) | Filtro de dispositivos disponíveis com Wi-Fi 6 e critérios de RAM/flash | A própria página alerta para limitações de chipsets Broadcom e procedimentos de instalação especiais em alguns equipamentos. |
| [OpenWrt — GL.iNet](https://openwrt.org/toh/gl.inet/start) | Índice de dispositivos GL.iNet documentados | Índice não é uma garantia de suporte atual para todos os modelos. |
| [GL.iNet — Firmware Versions](https://www.gl-inet.com/pages/firmware-versions/) | Versão/estado/suporte declarados pelo fabricante | Firmware GL.iNet deriva de OpenWrt mas pode incorporar software proprietário e basear-se em versões diferentes. Distinguir da release upstream. |
| [OpenWrt — GL-MT6000](https://openwrt.org/toh/hwdata/gl.inet/gl.inet_gl-mt6000) | Dados técnicos do GL-MT6000/Flint 2 | Ficha consultada listou suporte desde 23.05.3 e Supported Current Rel 25.12.5 em 2026-10-13; confirmar novamente antes da compra. |
| [OpenWrt — TP-Link Archer AX23 v1](https://openwrt.org/toh/tp-link/archer_ax23_v1) | Suporte e avisos específicos de revisão para AX23 v1/v1.20 | A página alerta que v2 tem SoC diferente e RAM insuficiente, e menciona relatos de comportamento irregular em versões posteriores a 23.05.4. Exige ensaio antes de qualquer utilização padronizada. |
| [OpenWrt — Techdata Archer AX23 v1](https://openwrt.org/toh/hwdata/tp-link/tp-link_ax23_v1) | CPU, memória, flash, portas e release declarada | Página dinâmica; os dados da revisão não se aplicam automaticamente a v2. |
| [OpenWrt — Cudy](https://openwrt.org/toh/cudy/start) | Existência de páginas para WR3000 e variantes, TR3000, APs e outros | Cada variante tem página própria. Não transferir uma aprovação entre modelos. |
| [OpenWrt — segurança/hardening](https://openwrt.org/docs/guide-user/security/openwrt_security) | Princípios de hardening, firewall WAN e segurança da gestão | A configuração de LAN também importa; firewall WAN por padrão não elimina risco interno. |
| [OpenWrt — funcionalidades de segurança](https://openwrt.org/docs/guide-user/security/security-features) | Assinatura de pacotes e mecanismos de hardening | Não constitui certificação completa do equipamento. |
| [OpenWrt — backup/restauro](https://openwrt.org/docs/guide-user/troubleshooting/backup_restore) | Preparação de backup e restauro de configuração | Backup deve ser testado e protegido. |
| [OpenWrt — sysupgrade](https://openwrt.org/docs/guide-user/installation/generic.sysupgrade) | Efeito de atualização e perda de sistema/pacotes não preservados | Exige imagem correta e planeamento do restauro. |

## Registo de observações

### GL.iNet GL-MT6000 (Flint 2)
- Fonte OpenWrt consultada: ficha hardware específica.
- Evidência encontrada: suporte desde 23.05.3; 25.12.5 aparecia como release atual suportada no momento da consulta; 1 GB RAM, 2x 2.5GbE indicados na ficha.
- Interpretação: candidato técnico a ensaio, não recomendação definitiva para cliente.
- Pendências: instruções de instalação/recovery; preço e garantia UE; versão atual; throughput Wi-Fi, firewall, SQM e VPN em laboratório; diferenças do firmware OEM.

### TP-Link Archer AX23
- Fonte OpenWrt consultada: página da revisão v1 e dados técnicos.
- Evidência: v1/v1.20 listado; a página avisa que v2 utiliza SoC diferente e RAM insuficiente; a ficha técnica indica 128 MB RAM e 16 MB flash para o alvo descrito.
- Interpretação: não usar o nome “AX23” como identificador suficiente. Confirmar etiqueta/revisão e investigar os avisos antes de avançar.

### Cudy
- Fonte OpenWrt consultada: índice Cudy, com páginas separadas para WR3000 e variantes, TR3000 e access points.
- Evidência: suporte documentado para certos itens do catálogo.
- Interpretação: fonte para gerar uma lista de candidatos; não basta para classificação de fiabilidade. Extrair e validar ficheiro/página específica de cada revisão.

## Classificação de evidências

- **A — evidência primária direta:** ficha oficial da revisão/modelo ou documentação do fabricante.
- **B — evidência indireta:** página índice que referencia o dispositivo.
- **C — evidência comunitária/relatos:** útil para descobrir risco, carece de reprodução.
- **T — teste XFI:** requer registo reproduzível com equipamento físico.

Nesta primeira pesquisa, os candidatos têm evidência A ou B para existência/compatibilidade declarada, mas **nenhum possui classificação T nem aprovação final XFI**.

## Política de atualização

Atualizar esta pasta quando: mudar a release OpenWrt, aparecer aviso de segurança relevante, mudar estado de manutenção do fabricante, surgir nova revisão comercial, uma unidade ser ensaiada, ou for realizada cotação local com data e condições.
