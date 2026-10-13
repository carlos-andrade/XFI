# Fabricantes candidatos a routers OpenWrt

**Data de pesquisa:** 2026-10-13  
**Estado:** triagem inicial baseada em documentação pública; não constitui ranking universal de fiabilidade.

## Síntese executiva

A marca, isoladamente, não prova fiabilidade nem segurança. Para uma oferta comercial XFI, priorizar fabricantes/modelos com ficha OpenWrt clara, revisão de hardware identificada, manutenção demonstrável e recuperação documentada. O ranking abaixo é de **prioridade de investigação**, não de segurança absoluta.

| Prioridade | Fabricante/ecossistema | Avaliação preliminar | Porque investigar | Riscos e condições |
|---|---|---|---|---|
| 1 | **GL.iNet** | Candidato forte para uma linha inicial com menor barreira operacional; modelos específicos devem ser validados | Firmware baseado em OpenWrt, páginas de suporte e lista pública de firmware/estado | Firmware do fabricante pode divergir do upstream e conter componentes proprietários. A página oficial mostra diferenças de versão e estado entre modelos. Decidir por modelo/firmware, não por marca. |
| 2 | **TP-Link** | Candidato condicional, com possibilidade de opções de preço acessível | Alguns modelos e revisões estão explicitamente listados na tabela OpenWrt | A mesma designação comercial pode ter revisões incompatíveis. Exemplos de avisos documentados na página AX23 demonstram que suporte nominal não equivale a ausência de problemas. |
| 3 | **Cudy** | Candidato condicional para ampliar opções de orçamento | A tabela OpenWrt tem páginas para alguns routers, routers de viagem e APs Cudy | Confirmar cada revisão e disponibilidade de suporte da release atual. A listagem da marca não significa suporte de todos os produtos. |
| 4 | **Banana Pi / plataforma BPI** | Candidato para segmentos avançados e laboratório, sobretudo quando se pretende hardware com mais interfaces/expansão | Pode interessar a utilizadores técnicos e implementações específicas | Muitas plataformas são placas/router boards, nem sempre ideais para cliente doméstico. Exigir caixa, alimentação, suporte Wi-Fi, assistência e recuperação. |
| 5 | **Linksys** | Candidato oportunístico, apenas para modelos/revisões com suporte explícito | Há hardware histórico conhecido pela comunidade OpenWrt | Não comprar por fama histórica. Verificar suporte da versão atual, stock, idade, revisão, flash/RAM e recuperação; modelos antigos podem estar fora de uma estratégia de longo prazo. |
| 6 | **Zyxel / outros OEMs** | Avaliar apenas se modelo e função exatos forem suportados | Pode haver equipamento interessante para APs ou segmentos específicos | O suporte OpenWrt é irregular entre famílias e revisões. Exigir prova de suporte antes de shortlist. |
| 7 | **Xiaomi / Redmi** | Investigação caso a caso, não recomendação geral de marca | Existem dispositivos individuais na comunidade OpenWrt | Variantes regionais, revisões e diferenças de hardware tornam arriscado generalizar. Acessibilidade comercial não resolve instalação, recuperação ou manutenção. |
| 8 | **ASUS e routers com Wi-Fi Broadcom** | Não adotar como padrão sem prova detalhada | Muitos produtos comerciais têm boa experiência OEM | A documentação OpenWrt alerta que chipsets Broadcom têm suporte FLOSS limitado. O desempenho Wi-Fi e a compatibilidade podem não corresponder às expectativas. |

## Recomendação prática para começar

- **Linha de entrada:** pesquisar um modelo que tenha documentação OpenWrt inequívoca, preço baixo mas hardware ainda adequado, recuperação acessível e custos de reposição previsíveis. TP-Link/Cudy entram como candidatos condicionais; GL.iNet também pode entrar se o preço final for competitivo.
- **Linha intermédia:** privilegiar hardware recente, RAM/flash confortáveis, suporte Wi-Fi estável e portas gigabit; GL.iNet e modelos upstream suportados de outras marcas devem competir por evidências.
- **Linha avançada:** maior capacidade de CPU/RAM, 2.5GbE quando necessário e desempenho medido com VPN/SQM; custo superior só se justifica por requisitos do cliente.
- **APs e cobertura maior:** avaliar arquitetura com router/firewall separado e pontos de acesso, em vez de exigir que um único equipamento sirva todos os cenários.

## O que significa “fiável” para este projeto

1. Suporte upstream verificável e sustentável.
2. Ausência de dependência de uma revisão incerta ou imagem não oficial.
3. Atualizações frequentes o suficiente para risco e função.
4. Recuperação física/serial/TFTP/dual image quando documentada e testável.
5. Capacidade de executar o perfil planeado com recursos de margem.
6. Reposição e assistência viáveis em Portugal/UE.
7. Repetibilidade de instalação e teste em lote.

## Fontes primárias iniciais

- [OpenWrt Table of Hardware](https://openwrt.org/toh/start)
- [Vista OpenWrt de dispositivos Wi-Fi 6](https://openwrt.org/toh/views/toh_available_16128_ax-wifi)
- [Índice OpenWrt GL.iNet](https://openwrt.org/toh/gl.inet/start)
- [Lista OpenWrt Cudy](https://openwrt.org/toh/cudy/start)
- [Firmware versions & status — GL.iNet](https://www.gl-inet.com/pages/firmware-versions/)
- [OpenWrt — TP-Link Archer AX23 v1](https://openwrt.org/toh/tp-link/archer_ax23_v1)

Ver [FONTES_EVIDENCIAS.md](FONTES_EVIDENCIAS.md) para observações de cada fonte e limitações.
