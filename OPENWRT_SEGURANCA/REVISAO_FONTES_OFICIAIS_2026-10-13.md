# Revisão inicial de fontes oficiais OpenWrt — 2026-10-13

**Estado:** revisão documental inicial baseada em páginas oficiais consultadas em 2026-10-13. Não é uma auditoria de segurança nem homologação de hardware.

## 1. Estado das releases

- A página inicial oficial OpenWrt identificava a série estável atual como **25.12**, com **25.12.5** como release mais recente, publicada em 1 de julho de 2026.
- A página oficial identifica **24.10** como série antiga; a informação de release apontava fim de suporte previsto para setembro de 2026. Para novas implantações após essa data, não selecionar 24.10 como padrão sem uma justificação formal e confirmação de suporte.
- A versão concreta a instalar deve ser novamente confirmada na data da homologação, assim como o suporte ao modelo/revisão e a imagem disponível no Firmware Selector.

Fontes:
- https://openwrt.org/
- https://openwrt.org/releases/start
- https://openwrt.org/about/history
- https://openwrt.org/releases/25.12/notes-25.12.5
- https://openwrt.org/releases/24.10/notes-24.10.8

## 2. Advisories e notas de release são fluxos distintos

A página oficial de advisories lista avisos próprios do projeto, incluindo advisories de Dropbear, ubusd e outros componentes. As notas de release também documentam correções de segurança integradas em releases estáveis, incluindo correções de componentes upstream.

**Decisão de ingestão:** não usar o índice de advisories como fonte única de segurança. A recolha deve acompanhar em paralelo:
1. índice oficial de OpenWrt Security Advisories;
2. notas e changelogs de cada release estável;
3. anúncios oficiais de release;
4. avisos de segurança dos projetos upstream quando uma dependência crítica o exigir.

Fontes:
- https://openwrt.org/advisory/start
- https://openwrt.org/docs/guide-developer/security
- https://openwrt.org/releases/25.12/notes-25.12.5
- https://lists.openwrt.org/pipermail/openwrt-announce/2026-June/000088.html

## 3. Exemplo de sinal de segurança a normalizar

As notas oficiais de OpenWrt 25.12.5 referem correções de vulnerabilidades em componentes de rede, incluindo problemas em `odhcpd`. A ficha de ingestão deve conservar o identificador CVE/GHSA quando publicado, severidade indicada pela fonte, componente, versões afetadas, release corretiva e URL oficial. Não inferir versões afetadas que a fonte não declara.

Esta referência serve como exemplo do esquema de dados, não como avaliação de exposição de um router específico. A exposição depende da release instalada, configuração, pacote e serviços ativos.

## 4. Regras de decisão para hardware e firmware

- Preferir a série estável atual, desde que o modelo e a revisão exatos tenham imagem suportada e recuperação documentada.
- Não selecionar uma imagem apenas pelo nome comercial do router.
- Antes da homologação, registar versão, target/subtarget, hash ou assinatura disponível, revisão física e método de recuperação.
- Para equipamentos já em operação, tratar fim de suporte como risco de manutenção e preparar migração validada; não atualizar automaticamente com base apenas na data de release.
- Uma URL acessível não é prova de que a recomendação nela contida continua válida.

## 5. Limitações

- Esta revisão não inclui uma análise de cada CVE individual nem a avaliação de impacto em modelos específicos.
- O estado de release e suporte é dinâmico; verificar novamente antes de comprar, instalar ou homologar.
- O verificador automático confirma acessibilidade e metadados básicos. A classificação de vulnerabilidades e recomendações de configuração requer revisão técnica humana.
- Zabbix continua em pausa e não faz parte desta execução.

## 6. Próximos passos

1. Definir esquema de dados de advisory/release com CVE/GHSA, componente, severidade declarada, versões afetadas/corrigidas, data upstream e evidência.
2. Criar um registo por advisory/release, sem copiar artigos completos.
3. Relacionar cada registo com modelos e versões de firmware apenas quando houver evidência explícita.
4. Acrescentar testes de deduplicação e de deteção de alterações.
5. Rever a shortlist de hardware face à série estável atual e às imagens disponíveis por revisão.
