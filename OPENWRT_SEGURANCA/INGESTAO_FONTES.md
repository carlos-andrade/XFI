# Especificação — ingestão de fontes oficiais OpenWrt

**Estado:** catálogo e verificador automatizado implementados; ingestão semântica, deteção de alterações e revisão humana continuam pendentes.  
**Limite:** o verificador atual verifica a acessibilidade HTTP de URLs explicitamente listadas e produz um relatório JSON normalizado. Não faz crawling geral nem interpreta automaticamente advisories.

## Objetivo

Manter um catálogo rastreável de fontes públicas relevantes à segurança, compatibilidade e manutenção dos routers XFI.

## Domínios de recolha

1. Documentação de configuração e hardening.
2. Table of Hardware e páginas de dispositivo/revisão.
3. Releases, notas de versão, imagens e ferramentas de firmware.
4. Advisories de segurança, issues e commits oficiais.
5. Documentação de pacotes, serviços, firewall, Wi-Fi, DNS/DHCP, VPN, IPv6, gestão e telemetria.
6. Alterações que tornem recomendações obsoletas ou incompatíveis.

## Estado da implementação

- Catálogo de fontes: `OPENWRT_SEGURANCA/FONTES_OFICIAIS.md`.
- Verificador: `OPENWRT_SEGURANCA/scripts/check_openwrt_sources.py`.
- Workflow: `.github/workflows/openwrt-source-link-check.yml`.
- Artefacto produzido: `openwrt-source-check-report.json`, publicado como artefacto do workflow.
- O verificador extrai os registos da tabela Markdown e normaliza categoria, URL, finalidade, linha de catálogo, estado HTTP, URL final e timestamp de verificação.
- Allowlist: HTTPS em `openwrt.org` e subdomínios, `git.openwrt.org` e, no GitHub, apenas caminhos sob `github.com/openwrt/`.
- A primeira execução, anterior à expansão do catálogo, confirmou 20/20 URLs acessíveis. A execução posterior à migração confirmou 26/26 URLs acessíveis, sem erros HTTP, rate limits ou erros de rede. A execução anterior com HTTP 429 ficou registada como evidência histórica e foi resolvida ao usar o Git oficial OpenWrt.

## Registo semântico inicial\n\nO ficheiro [REGISTO_ADVISORIES_RELEASES.csv](REGISTO_ADVISORIES_RELEASES.csv) contém exemplos normalizados de uma release e advisories citados no anúncio oficial. Os campos de versões afetadas continuam marcados para confirmação no advisory individual; não inferir aplicabilidade a equipamentos sem cruzar versão, pacote e configuração.\n\nA execução de 2026-10-13 após a expansão do catálogo verificou 30/30 URLs, sem erros HTTP, rate limits ou erros de rede: [workflow e artefacto](https://github.com/carlos-andrade/XFI/actions/runs/38385191297).\n\n## Contrato do relatório JSON

Campos de topo: `generated_at_utc`, `catalog`, `schema_version`, `total_unique_urls`, `reachable`, `http_errors`, `network_errors`, `note` e `sources`.

Cada registo em `sources` contém:

- `category`: tema indicado no catálogo;
- `url`: URL canónica declarada;
- `purpose`: finalidade/relevância descrita no catálogo;
- `catalog_line`: linha de origem para rastreabilidade;
- `status`, `final_url`, `result`, `detail`: resultado HTTP/rede;
- `checked_at_utc`: timestamp da verificação;
- `review_status`: permanece `reachability_checked_content_review_pending` até revisão humana.

Os registos são deduplicados por URL. A verificação de acessibilidade não prova autenticidade do conteúdo, ausência de vulnerabilidades, atualidade, compatibilidade ou aplicabilidade.

## Metadados futuros

Para a ingestão semântica, acrescentar quando disponível: `source_id`, título, data upstream, release afetada, CVE/advisory ID, versões afetadas, versões corrigidas, resumo próprio, hash de conteúdo, estado de revisão, responsável e relações com perfis de configuração.

Não inventar metadados ausentes. Usar estado explícito `unknown` ou `not_stated`.

## Processo proposto

1. Descobrir fontes a partir de índices oficiais e links autorizados.
2. Respeitar acesso, robots.txt, limites de taxa, termos e licenças.
3. Preferir fontes/endpoints oficiais estruturados quando disponíveis; não contornar proteção anti-bot ou autenticação.
4. Guardar metadados, URL e apenas o resumo/excerto necessário; evitar espelhamento integral sem licença/necessidade.
5. Normalizar URLs, deduplicar e registar mudanças.
6. Comparar versões e alertar para conteúdo novo, alterado ou removido.
7. Encaminhar alterações para revisão humana antes de mudar a baseline.
8. Validar recomendações contra release e hardware; ingestão nunca aplica configuração automaticamente.
9. Publicar relatório determinístico com itens lidos, falhas, fontes ignoradas, data e commit.

## Controlos de qualidade

- Links quebrados/redirecionamentos detetados.
- Fonte e timestamp presentes em cada resultado.
- Conteúdo upstream tratado como dado não confiável; nunca executar comandos recolhidos automaticamente.
- Distinguir release estável, snapshot, versão antiga e página sem compatibilidade declarada.
- Falha de acesso não significa que o recurso deixou de existir.
- Armazenar apenas o que é necessário e legal; em textos longos manter referência, atribuição e resumo próprio.
- Testes para normalização, deduplicação, allowlist, esquema e deteção de mudanças.
- Logs sem tokens, cookies, credenciais ou dados de cliente.

## Critérios de aceitação

- Execução reproduzível e idempotente.
- Allowlist explícita de fontes, limites de taxa e respeito às diretivas do site.
- Relatório e artefactos verificáveis.
- Ingestão não altera nem aplica configuração de router.
- Mudanças de recomendação requerem revisão, teste e aprovação independentes.
