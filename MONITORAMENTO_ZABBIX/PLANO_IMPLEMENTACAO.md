# Plano de implementação — Zabbix para frota OpenWrt

**Estado global:** EM PREPARAÇÃO — levantamento da instância real pendente.  
**Limite atual:** não há evidência de que tenham sido criados hosts, importados templates ou alterada qualquer configuração do Zabbix.

## Regra obrigatória de versão

- Consultar os [downloads oficiais](https://www.zabbix.com/download_sources) e as [notas de lançamento](https://www.zabbix.com/release_notes) imediatamente antes de uma mudança.
- Usar sempre a versão estável de produção mais recente; nunca usar alpha, beta ou release candidate em produção.
- Confirmar compatibilidade do sistema operativo, base de dados, PHP, Server, Frontend, Proxy, agentes e templates.
- Fazer backup verificável e preparar rollback antes de atualizar qualquer componente.
- Testar o caminho de atualização em laboratório antes de alterar produção.

**Referência temporal consultada em 2026-10-13:** Zabbix 7.4.15 era a release estável listada para a série 7.4; Zabbix 8.0.0rc1 estava listado como pré-lançamento. Verificar novamente antes da execução.

## Fase 1 — levantamento da infraestrutura

- [ ] Confirmar versão exata do Zabbix Server e Frontend.
- [ ] Confirmar sistema operativo e método de instalação.
- [ ] Confirmar se existem proxies, VPNs, segmentação, DNS e armazenamento de segredos.
- [ ] Confirmar acesso administrativo autorizado à instância e política de alterações.
- [ ] Definir capacidade, retenção, disponibilidade, backups e recuperação do Zabbix.
- [ ] Identificar um router de laboratório ou equipamento virtual para testes.

**Saída:** inventário da plataforma e desenho de conectividade aprovado.

## Fase 1A — recolha de evidência da versão

- [ ] Executar o procedimento em [LEVANTAMENTO_DA_INSTANCIA.md](LEVANTAMENTO_DA_INSTANCIA.md) no servidor/Frontend real.
- [ ] Registar apenas versões e dados de arquitetura não secretos.
- [ ] Confirmar o método de instalação antes de escolher comandos e artefactos.

**Bloqueio atual:** esta fase depende de execução no servidor ou da entrega dos resultados pelo operador. Não existe acesso direto confirmado à instância. Não gerar ficheiros de template importáveis nem alterar a instância antes de confirmar versão e método de instalação.

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
- [ ] Testar SNMP/agente, reinício, perda de WAN, perda do proxy e recuperação.
- [ ] Testar alteração de configuração aprovada e rollback.
- [ ] Validar consumo de recursos no router e carga no Zabbix.
- [ ] Documentar exceções por firmware e modelo.

**Saída:** template e perfil homologados para modelo, revisão e firmware específicos.

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
- o caminho de gestão está protegido;
- ações de escrita estão desativadas ou formalmente autorizadas e limitadas;
- existem backup, recuperação e contacto de operação;
- a homologação corresponde ao modelo, revisão e firmware instalados.
