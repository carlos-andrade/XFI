# XFI — Segurança de roteadores com OpenWrt

**Estado:** baseline documental inicial — não homologado para produção.  
**Responsável:** Carlos Andrade  
**Governança:** seguir as regras locais do XFI e a referência normativa central [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA).  
**Fontes primárias:** documentação oficial [OpenWrt](https://openwrt.org/).

## Objetivo
Criar uma base rastreável para recolher, classificar, versionar e aplicar conhecimento público do OpenWrt na parametrização segura de roteadores de clientes. O trabalho deve reduzir a superfície de ataque, isolar redes, proteger a administração, gerir atualizações e permitir auditoria e recuperação.

**Não existe configuração que garanta segurança absoluta.** A postura final depende do modelo e revisão de hardware, suporte upstream, versão e pacotes, desenho da rede, ameaças, operação e validação real.

## Princípios
1. Preferir documentação oficial OpenWrt, páginas do dispositivo, notas de versão, avisos de segurança e repositórios oficiais de código.
2. Nunca aplicar um comando genérico sem validar versão, alvo, arquitetura, driver Wi-Fi e topologia.
3. Guardar perfis sem segredos, com versão, pré-condições, diff, testes, rollback e aprovação.
4. Aplicar menor privilégio e segmentação proporcional ao risco.
5. Antes de firmware/firewall: backup, validação de imagem, janela de manutenção, acesso alternativo e recuperação.
6. Distinguir planeado, implementado, testado, homologado e implantado.
7. Nunca versionar credenciais, chaves privadas ou backups de cliente.

## Navegação
- [Governança e escopo](GOVERNANCA.md)
- [Arquitetura de referência](ARQUITETURA.md)
- [Baseline de segurança](BASELINE_SEGURANCA.md)
- [Inventário de fontes oficiais](FONTES_OFICIAIS.md)
- [Inventário de routers](INVENTARIO_ROUTERS.md)
- [Requisitos por perfil de cliente](PERFIL_CLIENTE.md)
- [Ingestão de fontes](INGESTAO_FONTES.md)
- [Verificador de links e workflow agendado](scripts/check_openwrt_sources.py)
- [Validação, testes e rollback](VALIDACAO_E_ROLLBACK.md)
- [Roadmap](ROADMAP.md)
- [Registo de evidências](REGISTO_EVIDENCIAS.md)

## Automação criada
O workflow [XFI — Verificar fontes oficiais OpenWrt](../.github/workflows/openwrt-source-link-check.yml) pode ser executado manualmente ou semanalmente. Verifica se o catálogo contém URLs HTTPS dentro do domínio oficial OpenWrt e produz um relatório de acessibilidade como artefacto. A acessibilidade HTTP **não** comprova que o conteúdo está correto, atualizado ou seguro. A primeira execução do workflow ainda precisa ser observada.

## Escopo da primeira versão
Inclui levantamento documental, desenho de controlos, ficha de inventário e uma rotina inicial de verificação de links. Ainda não inclui crawler abrangente de releases/advisories, perfil UCI pronto para produção, deployment automático, teste em equipamento físico, varredura externa nem homologação de modelos específicos.

## Gate mínimo para produção
Nenhum perfil pode ser chamado de homologado sem modelos/revisões suportados identificados, versão OpenWrt fixada, revisão por pares, backup protegido, teste de firewall e isolamento, verificação de administração remota, teste DNS/conectividade, atualização/recuperação ensaiadas, monitorização e aprovação documentada.
