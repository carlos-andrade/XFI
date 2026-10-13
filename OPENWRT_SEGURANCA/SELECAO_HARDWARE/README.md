# XFI — Seleção de hardware OpenWrt

**Data de revisão:** 2026-10-13  
**Estado:** pesquisa documental e comercial preliminar; não é certificação, teste laboratorial ou homologação de produção.  
**Governança:** [regras centrais GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) e [governança OpenWrt XFI](../GOVERNANCA.md).

## Objetivo

Identificar fabricantes e modelos candidatos a uma oferta de routers seguros para clientes de várias faixas de rendimento, usando como eixo a compatibilidade demonstrável com OpenWrt, manutenção de firmware, possibilidade de recuperação e custo total de suporte.

## Documentos deste dossier

- [Critérios de seleção e método de pontuação](CRITERIOS_DE_SELECAO.md)
- [Lista preliminar de fabricantes](FABRICANTES_CANDIDATOS.md)
- [Lista preliminar de modelos](MODELOS_CANDIDATOS.md)
- [Pesquisa comercial Portugal/UE — preços observados](PESQUISA_COMERCIAL_PT.md)
- [Matriz para diferentes perfis de cliente](MATRIZ_PERFIS.md)
- [Fontes e registo de pesquisa](FONTES_EVIDENCIAS.md)
- [Plano de homologação](PLANO_HOMOLOGACAO.md)

## Regra central

**Não escolher uma marca apenas pela reputação comercial.** OpenWrt não recomenda uma marca universalmente: a seleção depende dos requisitos e da combinação específica de modelo, revisão de hardware, chipset, drivers, imagem suportada, memória, flash, recuperação e manutenção. Consultar [OpenWrt Buyers' Guide](https://openwrt.org/toh/buyerguide) e a [Table of Hardware](https://openwrt.org/toh/start).

## Como interpretar a lista

- **Candidato prioritário:** merece uma análise e teste mais aprofundados, não significa aprovado.
- **Condicional:** pode ser adequado apenas para cenário, revisão ou firmware específico.
- **Não recomendar como padrão:** incerteza, limitações de suporte/firmware ou custo de operação tornam-no inadequado para uma frota padronizada sem prova adicional.
- **Não confirmado:** faltam evidências ou inspeção da revisão exata.

## Regras de segurança comercial

1. Não comprar em volume antes de confirmar a revisão física da unidade, imagem oficial disponível, recuperação e suporte à versão mantida.
2. Não instalar uma imagem de OpenWrt num modelo parecido ou numa revisão diferente.
3. Não confundir firmware do fabricante baseado em OpenWrt com uma versão OpenWrt upstream. GL.iNet publica uma matriz própria de versões; alguns modelos usam SDKs ou componentes que diferem do upstream.
4. Não declarar “mais seguro” apenas com base em RAM, velocidade Wi-Fi, preço, avaliações da loja ou popularidade.
5. Cada SKU comercial deve apontar para uma ficha com URL oficial, revisão exata, versão de firmware, hashes/assinaturas quando aplicável, testes, recuperação e decisão aprovada.
6. Considerar custo total: equipamento, fonte de alimentação, switch/AP adicionais, garantia, substituição, suporte, horas de configuração, atualização e recuperação.
7. A configuração final deve proteger clientes; a recolha de telemetria deve ser minimizada e transparente.
8. Os preços na pesquisa comercial são fotografias temporais e não cotações vinculativas. Marketplace, revisão desconhecida e custo de envio devem ficar explícitos.

## Conclusão preliminar

A estratégia recomendada é criar **uma pequena frota padronizada de 2–4 modelos**, e não suportar indiscriminadamente muitas marcas. A shortlist comercial inicial aponta para Cudy WR3000 como opção de orçamento a investigar, GL.iNet GL-MT6000 como candidato residencial de maior capacidade e OpenWrt One como alternativa orientada para o ecossistema OpenWrt. O Archer AX23 fica condicionado à revisão e aos avisos técnicos. Não há, nesta fase, qualquer modelo aprovado para produção.
