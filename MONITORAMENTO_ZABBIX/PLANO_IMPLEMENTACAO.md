# Plano de implementação — Zabbix para frota OpenWrt

**Estado:** PLANEADO. Nenhuma configuração Zabbix foi alterada por este documento.

## Política de versão obrigatória
- [ ] Consultar a página oficial de downloads/notas de lançamento imediatamente antes da mudança.
- [ ] Selecionar a versão estável mais recente; não usar alpha, beta ou release candidate em produção.
- [ ] Verificar requisitos e notas de atualização, compatibilidade do sistema operativo, base de dados, PHP, agentes, proxies e templates.
- [ ] Fazer backup verificável e preparar rollback antes de atualizar qualquer componente.
- [ ] Se a instância estiver atrás da versão-alvo, abrir uma etapa de atualização e validar em laboratório antes de mexer em produção.

**Referência consultada em 2026-10-13:** 7.4.15 era a versão estável da série 7.4 indicada no site oficial; 8.0.0rc1 era pré-lançamento. Verificar novamente no momento da execução.

## Política de versão obrigatória
- Consultar os downloads e notas oficiais imediatamente antes da mudança.
- Usar a versão estável mais recente; não usar alpha, beta ou release candidate em produção.
- Verificar compatibilidade de sistema operativo, base de dados, PHP, server, frontend, proxies, agentes e templates.
- Fazer backup verificável, preparar rollback e testar em laboratório antes de atualizar produção.
- Se a instância estiver atrás da versão-alvo, tratar a atualização como etapa própria antes de implementar os templates.

Referência temporal: em 2026-10-13, o site oficial indicava 7.4.15 como release da série 7.4 e 8.0.0rc1 como pré-lançamento. Verificar novamente no momento da execução.

## Fase 1 — levantamento da infraestrutura
- [ ] Confirmar versão exata do Zabbix Server/Frontend e sistema operativo.
- [ ] Confirmar se há proxies, VPNs, segmentação, DNS e armazenamento de segredos disponíveis.
- [ ] Confirmar acesso administrativo autorizado à instância e política de alterações.
- [ ] Definir capacidade, retenção, disponibilidade, backups e recuperação do Zabbix.
- [ ] Identificar um router de laboratório ou equipamento virtual para testes.

**Saída:** inventário da plataforma e desenho de conectividade aprovado.

## Fase 1A — evidência técnica de versão
- [ ] Executar o procedimento em LEVANTAMENTO_DA_INSTANCIA.md no servidor/Frontend real.
- [ ] Registar apenas versões e dados de arquitetura não secretos.
- [ ] Confirmar o método de instalação antes de escolher comandos e artefactos.

**Gate:** não produzir XML/YAML importável nem alterar a instância antes de confirmar versão e método de instalação.

## Fase 2 — modelo de inventário
- [ ] Definir nomenclatura sem dados pessoais.
- [ ] Criar grupos e tags.
- [ ] Definir campos de inventário: fabricante, modelo, revisão, release, método de monitorização, proxy, estado de homologação e criticidade.
- [ ] Criar lista de operações permitidas e perfis de acesso.

**Saída:** padrão de inventário e controlo de acesso.

## Fase 3 — monitorização mínima
- [ ] Criar templates XFI versionados para disponibilidade, WAN, interfaces e sistema.
- [ ] Selecionar SNMPv3 authPriv, agente com TLS ou método alternativo por modelo.
- [ ] Configurar descoberta controlada apenas em redes autorizadas.
- [ ] Criar triggers e mensagens de recuperação.
- [ ] Validar que indisponibilidade do proxy não é confundida com falha do router.

**Saída:** dashboard e alertas úteis sem falsos positivos excessivos.

## Fase 4 — automação controlada
- [ ] Implantar runner dedicado e restrito, apenas se necessário.
- [ ] Implementar validação de host/modelo/revisão/versão e estado de homologação.
- [ ] Separar ações de leitura, mudanças reversíveis e mudanças críticas.
- [ ] Implementar aprovação, registo de auditoria, idempotência, timeout e rollback.
- [ ] Desabilitar shell livre e operações destrutivas em massa por padrão.

**Saída:** demonstração de uma ação segura no laboratório, com evidência e rollback.

## Fase 5 — homologação por modelo
- [ ] Confirmar quais métricas cada router realmente expõe.
- [ ] Testar SNMP/agent, reinício, perda de WAN, perda do proxy e recuperação.
- [ ] Testar alteração de configuração aprovada e rollback.
- [ ] Validar consumo de recursos no router e carga no Zabbix.
- [ ] Documentar exceções por firmware e modelo.

**Saída:** template e perfil homologados para modelo/revisão/versão específicos.

## Fase 6 — piloto e produção
- [ ] Começar com pequeno lote autorizado.
- [ ] Validar alertas, tempos de resposta, manutenção e recuperação.
- [ ] Obter aprovação para expansão.
- [ ] Aplicar política de atualizações e revisão de segurança.
- [ ] Manter plano de saída/contingência se Zabbix ou VPN ficarem indisponíveis.

**Saída:** decisão formal de produção, responsabilidades e runbooks aprovados.

## Critérios de aceitação
Um router só pode ser declarado gerido por Zabbix quando:
- existe host ativo e inventário completo;
- os itens obrigatórios recolhem dados;
- alertas e recuperações foram testados;
- caminho de gestão está protegido;
- ações de escrita estão desativadas ou formalmente autorizadas e limitadas;
- há backup, recuperação e contacto de operação;
- a homologação corresponde ao modelo, revisão e firmware instalados.
