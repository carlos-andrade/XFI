# Plano de implementação — Zabbix para frota OpenWrt

**Estado:** PLANEADO. Nenhuma configuração Zabbix foi alterada por este documento.

## Fase 1 — levantamento da infraestrutura
- [ ] Confirmar versão exata do Zabbix Server/Frontend e sistema operativo.
- [ ] Confirmar se há proxies, VPNs, segmentação, DNS e armazenamento de segredos disponíveis.
- [ ] Confirmar acesso administrativo autorizado à instância e política de alterações.
- [ ] Definir capacidade, retenção, disponibilidade, backups e recuperação do Zabbix.
- [ ] Identificar um router de laboratório ou equipamento virtual para testes.

**Saída:** inventário da plataforma e desenho de conectividade aprovado.

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
