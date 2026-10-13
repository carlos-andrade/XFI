# XFI — Segurança de roteadores com OpenWrt

**Estado:** baseline documental inicial — não homologado para produção.  
**Responsável:** Carlos Andrade  
**Governança:** seguir as regras locais do XFI e a referência normativa central [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA).  
**Fontes primárias:** documentação oficial [OpenWrt](https://openwrt.org/).

## Objetivo
Criar uma base rastreável para recolher, classificar, versionar e aplicar conhecimento público do OpenWrt na parametrização segura de roteadores de clientes. O trabalho deve reduzir a superfície de ataque, isolar redes, proteger a administração, gerir atualizações e permitir auditoria e recuperação.

**Não existe configuração que garanta segurança absoluta.** A postura final depende do modelo e revisão de hardware, suporte upstream, versão e pacotes, desenho da rede, ameaças, operação e validação real.

## Regra obrigatória de monitorização e controlo
Todos os routers OpenWrt fornecidos ou geridos pela XFI devem ser monitorizados e inventariados no Zabbix. O Zabbix será a consola operacional central para métricas, alertas, inventário e acionamento de operações autorizadas. A implementação deve seguir a especificação em [MONITORAMENTO_ZABBIX](../MONITORAMENTO_ZABBIX/README.md).

Não expor LuCI, SSH, SNMP ou outros serviços de gestão à Internet pública para permitir a monitorização. Usar canal privado/proxy, credenciais de menor privilégio e automação restrita com auditoria e rollback para mudanças de configuração.

## Princípios
1. Preferir documentação oficial OpenWrt, páginas do dispositivo, notas de versão, avisos de segurança e repositórios oficiais de código.
2. Nunca aplicar um comando genérico sem validar versão, alvo, arquitetura, driver Wi-Fi e topologia.
3. Guardar perfis sem segredos, com versão, pré-condições, diff, testes, rollback e aprovação.
4. Aplicar menor privilégio e segmentação proporcional ao risco.
5. Antes de firmware/firewall: backup, validação de imagem, janela de manutenção, acesso alternativo e recuperação.
6. Distinguir planeado, implementado, testado, homologado e implantado.
7. Nunca versionar credenciais, chaves privadas ou backups de cliente.
8. Não considerar um router operacionalmente aceite se não estiver registado e monitorizado no Zabbix, com alertas e caminho de gestão seguros validados.

## Navegação
- [Governança e escopo](GOVERNANCA.md)
- [Arquitetura de referência](ARQUITETURA.md)
- [Baseline de segurança](BASELINE_SEGURANCA.md)
- [Inventário de fontes oficiais](FONTES_OFICIAIS.md)
- [Registo inicial de releases/advisories (CSV)](REGISTO_ADVISORIES_RELEASES.csv)
- [Revisão documental de releases e advisories (13/10/2026)](REVISAO_FONTES_OFICIAIS_2026-10-13.md)
- [Inventário de routers](INVENTARIO_ROUTERS.md)
- [Requisitos por perfil de cliente](PERFIL_CLIENTE.md)
- [Seleção de hardware — fabricantes, modelos, critérios e homologação](SELECAO_HARDWARE/README.md)
- [Monitorização e controlo obrigatório via Zabbix](../MONITORAMENTO_ZABBIX/README.md)
- [Ingestão de fontes](INGESTAO_FONTES.md)
- [Verificador de links e workflow agendado](scripts/check_openwrt_sources.py)
- [Validação, testes e rollback](VALIDACAO_E_ROLLBACK.md)
- [Roadmap](ROADMAP.md)
- [Registo de evidências](REGISTO_EVIDENCIAS.md)

## Automação criada
O workflow [XFI — Verificar fontes oficiais OpenWrt](../.github/workflows/openwrt-source-link-check.yml) pode ser executado manualmente ou semanalmente. Verifica URLs HTTPS do catálogo numa allowlist que inclui domínios oficiais OpenWrt, `git.openwrt.org` e caminhos específicos do repositório upstream em GitHub, e produz um relatório JSON normalizado como artefacto. A versão ampliada confirmou 26/26 URLs acessíveis, sem erros HTTP, rate limits ou erros de rede após a migração do histórico de commits para o Git oficial OpenWrt. A acessibilidade HTTP **não** comprova que o conteúdo está correto, atualizado ou seguro.

## Escopo da primeira versão
Inclui levantamento documental, desenho de controlos, ficha de inventário, shortlist preliminar de hardware e uma rotina inicial de verificação de links. Ainda não inclui ingestão semântica abrangente de releases/advisories, deteção de mudanças de conteúdo, perfil UCI pronto para produção, deployment automático, teste em equipamento físico, varredura externa nem homologação de modelos específicos. A monitorização Zabbix está especificada documentalmente, mas ainda não implementada na instância.

## Gate mínimo para produção
Nenhum perfil pode ser chamado de homologado sem modelos/revisões suportados identificados, versão OpenWrt fixada, revisão por pares, backup protegido, teste de firewall e isolamento, verificação de administração remota, teste DNS/conectividade, atualização/recuperação ensaiadas, monitorização Zabbix funcional, alertas testados e aprovação documentada.
