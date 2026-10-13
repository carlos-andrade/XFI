# Critérios de seleção e pontuação

**Revisão:** 2026-10-13  
**Estado:** metodologia proposta; ainda não aplicada através de testes físicos.

## Princípio de elegibilidade

Antes da pontuação, o modelo tem de passar quatro condições eliminatórias:

1. O **modelo e a revisão exatos** constam do OpenWrt Table of Hardware ou de página oficial atualizada de suporte.
2. Existe uma imagem de instalação/upgrading correta e uma versão mantida disponível para o alvo.
3. A instalação e o método de recuperação podem ser documentados, com risco aceitável.
4. O hardware tem recursos suficientes para o objetivo de utilização, incluindo firewall, VLANs/SSID separados e serviços previstos.

Se falhar uma condição eliminatória, não deve ser comprado como modelo padrão até resolução documentada.

## Pesos de avaliação

| Critério | Peso | Evidência necessária |
|---|---:|---|
| Suporte upstream para a revisão exata e release mantida | 25% | Página ToH, release suportada, target/subtarget, imagem disponível |
| Segurança e capacidade de atualização | 20% | histórico de manutenção, avisos, assinatura/integridade e rota de atualização |
| Recuperação e risco de instalação | 15% | método de recuperação ensaiável, instruções oficiais, possibilidade de restauro |
| Capacidades de rede | 15% | VLAN, firewall IPv4/IPv6, WAN/LAN gigabit ou melhor, múltiplos SSIDs, suporte Wi-Fi documentado |
| Recursos e margem de crescimento | 10% | CPU, RAM, flash/armazenamento e desempenho medido para VPN/QoS/serviços |
| Custo total e disponibilidade em Portugal/UE | 10% | preço real, garantia, disponibilidade, fonte e logística de substituição |
| Operabilidade e observabilidade | 5% | gestão local segura, logs, backup, automatização e facilidade de suporte |

Pontuação de 0 a 5 por critério. Converter para 100: soma de (nota/5 × peso).

## Faixas sugeridas (proposta)

- **85–100:** candidato a homologação; continua sujeito aos testes de aceitação.
- **70–84:** candidato condicional; documentar lacunas e cenário limitado.
- **Abaixo de 70:** não usar como padrão.
- **Falha eliminatória:** rejeitado independentemente da soma.

A pontuação é uma ferramenta interna de decisão, não uma certificação de segurança independente. Não preencher notas sem evidência.

## Requisitos mínimos de referência

Para uma nova compra, preferir pelo menos 128 MB de RAM e 16 MB de flash; para serviços adicionais, VPN, listas DNS, métricas e evolução futura, procurar margem substancialmente maior. Estes números são um filtro mínimo aproximado, não garantia de desempenho. A própria tabela OpenWrt informa que o espaço utilizável de flash pode ser inferior ao tamanho físico. Ver [Table of Hardware](https://openwrt.org/toh/start) e [vista de dispositivos Wi-Fi 6](https://openwrt.org/toh/views/toh_available_16128_ax-wifi).

Requisitos adicionais:
- evitar hardware cuja função Wi-Fi dependa de suporte proprietário/driver não mantido quando isso comprometer a experiência OpenWrt;
- validar Wi-Fi real, roaming e múltiplos SSIDs; não inferir qualidade de cobertura pela ficha técnica;
- confirmar aceleração de hardware e desempenho real com firewall, SQM, VPN e IPv6;
- considerar WPA3 e recursos de rádio de acordo com driver e versão;
- confirmar suporte VLAN sem depender de hacks privados;
- preferir atualizações verificáveis e uma rota de recuperação compreendida;
- não expor LuCI, SSH, APIs de gestão ou métricas à WAN por padrão.

## Evidência e incerteza

Cada afirmação deve ser classificada como:
- **Fonte primária:** documentação OpenWrt ou fabricante.
- **Fonte comunitária:** fóruns/issues; útil para detetar problemas, exige validação.
- **Teste XFI:** medições reproduzíveis com equipamento físico.
- **Não verificado:** hipótese ou dado a confirmar.

Uma revisão física pode mudar radicalmente o resultado. A lista de fabricantes nunca substitui verificação por modelo e revisão.
