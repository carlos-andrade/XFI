# Pesquisa comercial — routers OpenWrt em Portugal/UE

**Data da consulta:** 2026-10-13  
**Âmbito:** preços públicos encontrados online, antes de compra e sujeitos a alteração.  
**Estado:** pesquisa de mercado preliminar; não são cotações comerciais vinculativas nem confirmação de stock, envio, revisão física ou compatibilidade do exemplar.

## Comparativo de preços observados

| Produto | Preço observado | Canal/fonte | Leitura para o XFI |
|---|---:|---|---|
| **Cudy WR3000** | cerca de **43,21 € com envio** numa oferta comparadora; outra oferta na Leroy Merlin a 55,65 € | [KuantoKusta](https://www.kuantokusta.pt/p/10175380/cudy-router-wireless-ax3000-wr3000-dual-band-wifi-6-gigabit-wr3000); [Leroy Merlin](https://www.leroymerlin.pt/produtos/roteador-sem-fio-cudy-wr3000-gigabit-ethernet-dual-band-2-4-ghz-5-ghz-preto-91037198.html) | Candidato de baixo custo, mas a oferta comparadora tem vendedor terceiro. Confirmar SKU/revisão e página OpenWrt específica antes de comprar. |
| **Cudy WR3000S** | **58,66 €** | [Worten](https://www.worten.pt/produtos/router-cudy-wr3000s-branco-wi-fi-ethernet-lan-mrkean-6971690793203), marketplace vendido/enviado por MS2 Digital | Não assumir que WR3000S é equivalente a WR3000. Confirmar revisão exata, compatibilidade e procedimento de instalação. |
| **TP-Link Archer AX23** | cerca de **67,76 €** com envio grátis numa oferta | [KuantoKusta](https://www.kuantokusta.pt/p/6681502/tp-link-wireless-ax1800-archer-ax23-dual-band-wifi-6-gigabit-archerax23); [TP-Link Portugal — suporte v1](https://www.tp-link.com/pt/support/download/archer-ax23/v1/) | O preço é de uma designação comercial genérica; não prova que a unidade é v1/v1.20. Não comprar para OpenWrt sem foto da etiqueta e revisão confirmada pelo vendedor. |
| **GL.iNet GL-MT6000 (Flint 2)** | **165,37 €**, IVA indicado como incluído | [Loja oficial GL.iNet UE](https://www.gl-inet.com/en-de/products/gl-mt6000) | Candidato intermédio/avançado. Confirmar no checkout entrega para Portugal, versão/firmware desejados e condições de garantia. |
| **GL.iNet GL-MT3000 (Beryl AX)** | **102,85 €**, IVA indicado como incluído | [Loja oficial GL.iNet UE](https://www.gl-inet.com/en-de/products/gl-mt3000) | Router portátil; não é substituto direto de um router residencial com múltiplas portas e cobertura para toda a casa. |
| **OpenWrt One** | **174,24 € com IVA** na loja europeia consultada | [Banana Pi EU](https://banana-pi.eu/produit/openwrt-one-ap-24-xy/) | Plataforma desenhada para OpenWrt e com hardware documentado. Avaliar custos adicionais de switch/AP e entrega/garantia em Portugal. |

## Interpretação por segmento

### Orçamento mais baixo
O Cudy WR3000 tem os preços públicos mais baixos encontrados nesta pesquisa. Porém, o preço não basta para o aprovar: verificar a variante/revisão, o estado de suporte na Table of Hardware, imagem e recuperação. Uma poupança de algumas dezenas de euros não compensa se aumentar as horas de assistência ou o risco de brick.

### Intermédio
O GL.iNet GL-MT6000 tem preço público de referência próximo de 165 €. A ficha OpenWrt oficial identifica 1 GB de RAM, eMMC e duas portas 2.5GbE, além de suporte upstream atual na data consultada. É um candidato forte para laboratório, mas há uma distinção crítica entre OpenWrt upstream e firmware do fabricante: a tabela oficial GL.iNet indica que o firmware estável 4.9.1 do MT6000 se baseia em OpenWrt 21.02; existe uma linha “op24” baseada em 24.10 e há firmware upstream 25.12.5 disponível na página OpenWrt. O XFI deve escolher explicitamente qual firmware suportará e testar a recuperação antes de vender o serviço.

### Plataforma orientada para OpenWrt
O OpenWrt One é uma alternativa a considerar pelo desenho voltado para o projeto OpenWrt e hardware documentado. O seu arranjo de portas é menos flexível que o de um router residencial com várias LAN: planeie switch e ponto de acesso, se necessários, e some os custos antes de o comparar com o Flint 2.

### Modelos com revisão crítica
O Archer AX23 pode surgir em torno de 68 €, mas a listagem de venda não identifica necessariamente a revisão. A página oficial TP-Link distingue versões de hardware e região; a página OpenWrt tem ressalvas específicas para AX23 v2. Por isso, o preço baixo não o transforma numa escolha adequada para uma frota padrão.

## Regras para transformar estes preços em orçamento real

1. Obter preço final com IVA, portes, prazo, garantia, devolução e entidade vendedora.
2. Confirmar se a loja é o vendedor real ou marketplace; guardar a entidade que efetivamente fatura.
3. Solicitar ao vendedor confirmação escrita do modelo, revisão e SKU/região antes da compra.
4. Confirmar se o equipamento pode ser devolvido se a etiqueta indicar revisão incompatível.
5. Cotar pelo menos duas unidades do candidato prioritário: uma para laboratório e outra para validar repetibilidade.
6. Incluir no custo total eventuais switch, AP, fonte, cabos, adaptadores de recuperação e horas de suporte.
7. Revalidar todos os preços na data da aquisição; não os usar como valores fixos em propostas a clientes.

## Conclusão comercial provisória

- **Mais barato a investigar:** Cudy WR3000, desde que a revisão específica seja oficialmente suportada e recuperável.
- **Candidato residencial de maior capacidade:** GL.iNet GL-MT6000, com decisão explícita sobre firmware OEM ou OpenWrt upstream.
- **Candidato de referência OpenWrt:** OpenWrt One, considerando o custo de switch/AP e a instalação.
- **Condicional, não padronizar agora:** TP-Link Archer AX23 até confirmar revisão e resolver os avisos técnicos.
- **Uso portátil:** GL.iNet GL-MT3000, como categoria separada.

Nenhum produto está homologado para instalação em clientes. Os preços são evidência comercial pontual, não evidência de segurança ou compatibilidade.
