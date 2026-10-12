# Especificação inicial — ingestão de dados oficiais OpenWrt

**Estado:** planeado; ainda não existe crawler/workflow automatizado nesta entrega.

## Objetivo
Manter catálogo consultável de fontes públicas relevantes à segurança, compatibilidade e manutenção de routers XFI.

## Domínios de recolha
1. Documentação de configuração e hardening.
2. Table of Hardware e páginas de dispositivo/revisão.
3. Releases, notas de versão, imagens e ferramentas de firmware.
4. Advisories de segurança, issues/commits oficiais e correções.
5. Documentação de pacotes, serviços, firewall, Wi-Fi, DNS/DHCP, VPN, IPv6, gestão e telemetria.
6. Alterações que tornem recomendações obsoletas ou incompatíveis.

## Metadados mínimos
`source_id`, URL canónica, título, categoria, consulta UTC, data upstream se disponível, release aplicável, resumo próprio, hash se apropriado/legal, estado de revisão, última revisão, responsável e relações com perfis.

## Processo proposto
1. Descobrir páginas a partir de índices oficiais e links oficiais.
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
- Fonte e data sempre presentes.
- Conteúdo upstream tratado como dado não confiável; nunca executar comandos recolhidos automaticamente.
- Distinguir release estável, snapshot, versão antiga e página sem compatibilidade declarada.
- Falha de acesso não significa que o recurso deixou de existir.
- Armazenar apenas o que é necessário e legal; em textos longos manter referência, atribuição e resumo próprio.
- Testes para normalização, deduplicação, links, esquema e deteção de mudanças.
- Logs sem tokens, cookies, credenciais ou dados de cliente.

## Critérios de aceitação futura
- Execução reproduzível e idempotente.
- Allowlist explícita de fontes, limites de taxa e respeito às diretivas do site.
- Relatório e artefactos versionados.
- Ingestão não altera nem aplica configuração de router.
- Mudanças de recomendação requerem revisão, teste e aprovação independentes.
