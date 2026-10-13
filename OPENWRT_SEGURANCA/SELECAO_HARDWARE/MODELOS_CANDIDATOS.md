# Lista preliminar de modelos OpenWrt

**Revisão:** 2026-10-13  
**Uso permitido:** shortlist para diligência técnica e recolha de preços; não comprar em volume nem instalar em clientes com base apenas nesta lista.

## Candidatos identificados em fontes OpenWrt

| Modelo e revisão | Papel potencial | Evidência inicial | Limitações e decisão |
|---|---|---|---|
| **GL.iNet GL-MT6000 (Flint 2)** | Intermédio/avançado; referência para capacidades elevadas e portas 2.5GbE | A ficha técnica OpenWrt indica suporte desde 23.05.3 e release atual na data consultada 25.12.5; CPU quad-core MT7986AV, 1 GB RAM, e duas portas 2.5GbE | **Candidato prioritário para laboratório.** Confirmar método de instalação, imagem apropriada, recuperação, firmware OEM vs upstream, disponibilidade/preço UE, Wi-Fi, throughput com configuração real e status oficial no dia de aquisição. |
| **TP-Link Archer AX23 v1/v1.20** | Possível linha de entrada, se o preço e a revisão forem confirmados | Página OpenWrt indica suporte; ficha técnica indica 128 MB RAM, 16 MB flash e cinco portas 1GbE | **Condicional e com ressalvas importantes.** A página do dispositivo contém aviso de que AX23 v2 tem SoC diferente e RAM insuficiente, e descreve relatos de comportamento irregular em versões posteriores a 23.05.4. Não padronizar sem reproduzir e resolver o problema em teste. |
| **Cudy WR3000 (v1)** | Candidato de orçamento Wi-Fi 6 | A página/índice OpenWrt lista uma ficha do modelo | **Não confirmado para compra.** Rever a página específica, release atual suportada, revisões e comentários técnicos; o índice por marca não é prova suficiente. |
| **Cudy WR3000E / WR3000H / WR3000P / WR3000S** | Alternativas económicas a comparar com o WR3000 | O índice OpenWrt lista páginas individuais para estas variantes | São modelos diferentes, não presumir equivalência. Confirmar ficha e revisão por SKU. |
| **Cudy TR3000** | Router portátil/viagem para casos específicos | A tabela OpenWrt lista variantes TR3000, incluindo uma ficha com distinção de memória | Não é automaticamente um router principal de residência. Confirmar RAM da unidade, cobertura, portas e requisitos do cliente. |
| **Cudy AP3000 Outdoor / outros APs listados** | Cobertura exterior, quando tecnicamente adequada | Índice oficial de dispositivos Cudy lista fichas específicas | Confirmar PoE, impermeabilização, domínio regulatório, radio, release e recuperação. Não extrapolar suporte entre modelos. |
| **Banana Pi BPI-R3 ou outra plataforma BPI suportada** | Laboratório, projeto avançado ou router modular | A investigar na tabela e páginas oficiais por revisão | Não homologado nesta pesquisa inicial. Confirmar disponibilidade atual, custos de caixa/fonte/radios e viabilidade como produto de cliente. |
| **Linksys de modelos/revisões suportados** | Oportunidade se hardware for recente e custo total baixo | Pesquisar individualmente na Tabela de Hardware | Não foi estabelecido nesta fase um modelo padrão aprovado. Validar release mantida, recursos, origem do stock e recuperação. |
| **GL.iNet GL-MT3000 (Beryl AX)** | Router compacto/viagem; possível perfil especial | Página de firmware GL.iNet lista o modelo; requer confirmar separadamente suporte OpenWrt upstream exato e release | Pode ser útil para viagem, acesso remoto ou casos especiais; não assumir que serve como router principal de todos os clientes. |

## Ordem recomendada de diligência

1. **GL-MT6000** — preparar ficha detalhada, custo em Portugal/UE e plano de laboratório, devido às características de hardware e listagem OpenWrt atual.
2. **Cudy WR3000 e variantes** — comparar cada ficha e revisão antes de considerar linha económica.
3. **TP-Link Archer AX23 v1/v1.20** — investigar apenas após rever e testar os avisos identificados. AX23 v2 fica excluído até suporte explícito futuro.
4. Adicionar modelos de outras marcas somente quando a ficha do hardware e uma fonte de disponibilidade confiável estiverem localizadas.

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
