# XFI — Seleção de hardware OpenWrt

**Data de revisão:** 2026-10-13  
**Estado:** pesquisa documental preliminar; não é certificação, teste laboratorial ou homologação de produção.  
**Governança:** [regras centrais GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) e [governança OpenWrt XFI](../GOVERNANCA.md).

## Objetivo

Identificar fabricantes e modelos candidatos a uma oferta de routers seguros para clientes de várias faixas de rendimento, usando como eixo a compatibilidade demonstrável com OpenWrt, manutenção de firmware, possibilidade de recuperação e custo total de suporte.

## Documentos deste dossier

- [Critérios de seleção e método de pontuação](CRITERIOS_DE_SELECAO.md)
- [Lista preliminar de fabricantes](FABRICANTES_CANDIDATOS.md)
- [Lista preliminar de modelos](MODELOS_CANDIDATOS.md)
- [Matriz para diferentes perfis de cliente](MATRIZ_PERFIS.md)
- [Fontes e registo de pesquisa](FONTES_EVIDENCIAS.md)
- [Plano de homologação](PLANO_HOMOLOGACAO.md)

## Regra central

**Não escolher uma marca apenas pela reputação comercial.** OpenWrt é avaliado por combinação específica de modelo, revisão de hardware, chipset, drivers, imagem suportada, memória, flash, recuperação e manutenção. A tabela oficial de hardware é a referência inicial, mas as instruções e notas da página individual de cada equipamento devem ser lidas antes de comprar ou instalar firmware: [OpenWrt Table of Hardware](https://openwrt.org/toh/start).

## Como interpretar a lista

- **Candidato prioritário:** merece uma análise e teste mais aprofundados, não significa aprovado.
- **Condicional:** pode ser adequado apenas para cenário, revisão ou firmware específico.
- **Não recomendar como padrão:** incerteza, limitações de suporte/firmware ou custo de operação tornam-no inadequado para uma frota padronizada sem prova adicional.
- **Não confirmado:** faltam evidências ou inspeção da revisão exata.

## Regras de segurança comercial

1. Não comprar em volume antes de confirmar a revisão física da unidade, imagem oficial disponível, recuperação e suporte à versão mantida.
2. Não instalar uma imagem de OpenWrt num modelo parecido ou numa revisão diferente.
3. Não confundir firmware do fabricante baseado em OpenWrt com uma versão upstream oficial. GL.iNet publica uma matriz própria de versão, estado e suporte, e alguns modelos usam componentes ou SDKs que diferem do upstream.
4. Não declarar “mais seguro” apenas com base em RAM, velocidade Wi-Fi, preço, avaliações da loja ou popularidade.
5. Cada SKU comercial deve apontar para uma ficha com URL oficial, revisão exata, versão de firmware, hashes/assinaturas quando aplicável, testes, recuperação e decisão aprovada.
6. Considerar custo total: equipamento, fonte de alimentação, garantia, substituição, suporte, horas de configuração, atualização e recuperação.
7. A configuração final deve proteger clientes; a recolha de telemetria deve ser minimizada e transparente.

## Conclusão preliminar

A estratégia recomendada é criar **uma pequena frota padronizada de 2–4 modelos**, e não suportar indiscriminadamente muitas marcas. Começar por um candidato económico e outro de maior capacidade, validar em laboratório e só depois alargar a gama. Não há, nesta fase, uma lista de modelos aprovada para produção.
