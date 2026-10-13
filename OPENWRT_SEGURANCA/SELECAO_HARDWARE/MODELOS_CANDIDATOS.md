# Lista preliminar de modelos OpenWrt

**Revisão:** 2026-10-13  
**Uso permitido:** shortlist para diligência técnica e recolha de preços; não comprar em volume nem instalar em clientes com base apenas nesta lista.

## Candidatos identificados em fontes OpenWrt

| Modelo e revisão | Papel potencial | Evidência inicial | Limitações e decisão |
|---|---|---|---|
| **GL.iNet GL-MT6000 (Flint 2)** | Intermédio/avançado; router residencial com maior capacidade e 2.5GbE | [Ficha OpenWrt](https://openwrt.org/toh/hwdata/gl.inet/gl.inet_gl-mt6000) indica suporte desde 23.05.3 e Supported Current Rel 25.12.5 em 2026-10-13; CPU quad-core MT7986AV, 1 GB RAM, eMMC e duas portas 2.5GbE. Preço oficial observado: 165,37 € com IVA indicado como incluído. | **Candidato prioritário para laboratório, mas com risco de firmware OEM.** A matriz oficial GL.iNet indica firmware estável 4.9.1 baseado em OpenWrt 21.02; existe uma linha “op24” baseada em 24.10 e a release upstream 25.12.5 é suportada separadamente. O XFI deve escolher e testar uma linha concreta, incluindo recuperação, antes de oferecer suporte comercial. |
| **OpenWrt One** | Router de referência, laboratório ou instalação modular | [Página europeia do produto](https://banana-pi.eu/produit/openwrt-one-ap-24-xy/) indica 174,24 € com IVA; plataforma concebida para OpenWrt e documentação pública. | **Adicionar à avaliação.** A arquitetura de portas é mais limitada do que em routers residenciais com várias LAN; avaliar switch/AP adicionais, custo instalado, recuperação, disponibilidade e garantia para Portugal. |
| **Cudy WR3000 (v1)** | Possível linha de orçamento Wi-Fi 6 | [Oferta comparadora](https://www.kuantokusta.pt/p/10175380/cudy-router-wireless-ax3000-wr3000-dual-band-wifi-6-gigabit-wr3000) observada perto de 43,21 € com envio; [Leroy Merlin](https://www.leroymerlin.pt/produtos/roteador-sem-fio-cudy-wr3000-gigabit-ethernet-dual-band-2-4-ghz-5-ghz-preto-91037198.html) listava 55,65 €. O catálogo OpenWrt tem páginas de modelos Cudy. | **Candidato de orçamento, não aprovado.** Confirmar que a revisão e SKU comprados correspondem exatamente à página OpenWrt e release mantida; confirmar imagem, recuperação e estabilidade. Preço baixo em marketplace não é prova de suporte. |
| **Cudy WR3000S** | Alternativa económica a comparar | [Worten](https://www.worten.pt/produtos/router-cudy-wr3000s-branco-wi-fi-ethernet-lan-mrkean-6971690793203) listava 58,66 €, vendedor terceiro. | Variante distinta. Confirmar página OpenWrt própria, revisão, imagem e recuperação; não assumir que o suporte de WR3000 se aplica a WR3000S. |
| **TP-Link Archer AX23 v1/v1.20** | Possível linha de entrada, se a revisão e os avisos forem resolvidos | [Página OpenWrt](https://openwrt.org/toh/tp-link/archer_ax23_v1) lista suporte para determinadas revisões; preços observados perto de 67,76–67,99 €. | **Condicional e com ressalvas importantes.** A página alerta que AX23 v2 tem SoC diferente e RAM insuficiente, e descreve relatos de comportamento irregular em versões posteriores a 23.05.4. Ofertas comerciais não garantem revisão v1. Não padronizar sem confirmação escrita do vendedor e teste reproduzível. |
| **GL.iNet GL-MT3000 (Beryl AX)** | Router compacto/viagem; perfil especial | [Loja oficial GL.iNet UE](https://www.gl-inet.com/en-de/products/gl-mt3000) listava 102,85 € com IVA indicado como incluído. | Categoria portátil. Confirmar suporte upstream exato se esse for o firmware escolhido; não tratar como substituto direto de router residencial multiporta. |
| **Cudy WR3000E / WR3000H / WR3000P** | Outras alternativas económicas | O [índice OpenWrt Cudy](https://openwrt.org/toh/cudy/start) referencia páginas distintas para variantes. | Modelos diferentes; sem aprovação transferida. Confirmar ficha e revisão individual, release atual, preço e recuperação. |
| **Cudy TR3000** | Router portátil/viagem para casos específicos | A tabela OpenWrt lista variantes TR3000, incluindo diferenças de memória. | Não é automaticamente router principal de residência. Confirmar RAM da unidade, cobertura, portas e requisitos. |
| **Cudy AP3000 Outdoor / outros APs listados** | Cobertura exterior, quando tecnicamente adequada | Índice oficial de dispositivos Cudy lista fichas específicas. | Confirmar PoE, impermeabilização, domínio regulatório, rádio, release e recuperação. |
| **Banana Pi BPI-R3 ou outra plataforma BPI suportada** | Laboratório, projeto avançado ou router modular | A investigar na tabela e páginas oficiais por revisão. | Não homologado. Confirmar disponibilidade atual, custos de caixa/fonte/radios e viabilidade como produto de cliente. |

## Comparativo comercial preliminar

| Faixa de preço observado | Opção para investigar | Observação |
|---|---|---|
| ~43–59 € | Cudy WR3000 / WR3000S | Melhor faixa de custo observada, mas verificar variantes e revisão exata; os preços incluem canais de terceiros. |
| ~68 € | TP-Link Archer AX23 | Não comprar para OpenWrt sem revisão confirmada; tem alertas técnicos. |
| ~103 € | GL.iNet GL-MT3000 | Router de viagem, não linha residencial geral. |
| ~165–174 € | GL.iNet GL-MT6000 / OpenWrt One | Candidatos para laboratório/intermédio-avançado; comparar firmware, portas, recuperação e custo total instalado. |

Preços, portes, IVA e disponibilidade mudam. Ver [PESQUISA_COMERCIAL_PT.md](PESQUISA_COMERCIAL_PT.md) para fontes e condições.

## Ordem recomendada de diligência

1. **GL-MT6000 e OpenWrt One:** obter uma unidade de laboratório de cada, se o orçamento permitir, e comparar firmware, recuperação, portas, Wi-Fi, VPN, SQM e custo total instalado.
2. **Cudy WR3000:** identificar revisão/SKU e pedir ao vendedor confirmação antes de encomendar uma unidade de teste.
3. **Cudy WR3000S:** só analisar separadamente após confirmar página OpenWrt específica e revisão.
4. **TP-Link AX23 v1/v1.20:** investigar apenas após confirmar revisão física e estudar os avisos. AX23 v2 fica excluído até suporte explícito e adequado.
5. **GL-MT3000:** manter em categoria de viagem, sem misturar com routers residenciais.
6. Adicionar outros modelos apenas com página específica, preço UE e rota de recuperação documentada.

## Campos obrigatórios antes da decisão

- fabricante, nome comercial completo, código do modelo e revisão impressa na etiqueta;
- região do SKU e fotografia da etiqueta (sem números de série/endereços MAC publicados);
- SoC, arquitetura, RAM, flash e chipset Wi-Fi;
- link e estado atual na Table of Hardware;
- release OpenWrt suportada e imagem exata;
- método de primeira instalação, sysupgrade e recuperação;
- VLAN, múltiplos SSIDs, IPv6/firewall, SQM e VPN conforme o perfil;
- throughput medido com e sem VPN/QoS; consumo, temperatura e estabilidade;
- disponibilidade, preço final com IVA, garantia, devolução e lead time;
- relatório de testes, resultado, pendências e aprovador.

## Regra de atualização

Os estados “Supported Current Rel” e versões do firmware mudam. Reconsultar fontes oficiais na data da compra; a versão registada nesta pesquisa não deve ser usada como garantia futura.
