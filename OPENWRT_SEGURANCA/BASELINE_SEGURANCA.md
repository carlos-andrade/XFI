# Baseline de segurança OpenWrt — perfil por homologar

**Estado de todos os itens:** requisitos propostos; não afirmar implementados sem verificação num equipamento.

## A. Identidade, firmware e superfície de ataque
- [ ] Registar fabricante, modelo, revisão, target/subtarget, versão, kernel, pacotes e estado de suporte.
- [ ] Usar release estável suportada adequada ao dispositivo; confirmar que o modelo recebe atualizações.
- [ ] Alterar credenciais iniciais; password única por equipamento/cliente.
- [ ] Remover/desativar serviços, protocolos e pacotes desnecessários.
- [ ] Confirmar ausência de telnet e de serviços de administração expostos na WAN.
- [ ] Rever portas abertas localmente e a partir de rede externa controlada.
- [ ] Inventariar pacotes terceiros, repositórios adicionais e scripts de arranque.

## B. Administração
- [ ] Permitir LuCI/SSH apenas pela zona de gestão ou VPN conforme topologia.
- [ ] Usar SSH com autenticação forte; guardar chaves privadas fora do router e do Git.
- [ ] Validar certificados HTTPS conforme o modo operacional.
- [ ] Restringir origens e serviços administrativos em IPv4 e IPv6.
- [ ] Rever autorização ubus/RPC e permissões dos serviços instalados.
- [ ] Validar recuperação física/remota antes de remover caminhos de gestão.

## C. Firewall e isolamento
- [ ] Rever zonas e políticas WAN/LAN/interfaces adicionais.
- [ ] Confirmar firewall4/nftables quando aplicável; gerir persistência pelo mecanismo recomendado.
- [ ] Bloquear entrada WAN não solicitada, exceto exceções aprovadas.
- [ ] Bloquear GUEST → LAN, MANAGEMENT e IoT salvo exceções justificadas.
- [ ] Bloquear IoT → redes confiáveis/gestão; permitir fluxos mínimos necessários.
- [ ] Rever port forwards, UPnP/NAT-PMP/PCP, DMZ e regras temporárias.
- [ ] Testar cada par de zonas em IPv4 e IPv6.
- [ ] Verificar persistência após reload e reboot.

## D. Wi-Fi
- [ ] Preferir WPA3-SAE; permitir WPA2-AES/CCMP apenas por compatibilidade.
- [ ] Não usar WEP, WPA1 ou TKIP.
- [ ] Usar credenciais fortes, únicas e não reutilizadas.
- [ ] Separar guest e IoT conforme o risco.
- [ ] Confirmar isolamento real L2/L3 e não só SSID distinto.
- [ ] Rever WPS, redes abertas e onboarding.
- [ ] Confirmar domínio regulatório e capacidades dos drivers.

## E. DNS, DHCP e IPv6
- [ ] Documentar DNS upstream, política de logs, privacidade e indisponibilidade.
- [ ] Confirmar DNS rebinding protection e documentar exceções.
- [ ] Restringir DNS/DHCP às interfaces corretas; evitar resolver aberto na WAN.
- [ ] Rever IPv6 RA, DHCPv6, prefix delegation, firewall e administração.
- [ ] Testar fugas DNS e caminhos alternativos permitidos (DoH/DoT/VPN).
- [ ] Não prometer bloqueio absoluto de malware/trackers via DNS.

## F. Atualizações e resiliência
- [ ] Acompanhar advisories, releases e suporte do modelo.
- [ ] Criar backup antes da mudança e testar restauro em equipamento equivalente.
- [ ] Validar imagem e compatibilidade antes de flash/sysupgrade.
- [ ] Guardar versão conhecida funcional se o método e armazenamento permitirem.
- [ ] Definir janela, responsável, tempo máximo, testes pós-update e critérios de abortar.
- [ ] Não atualizar kernel/módulos isoladamente sem compatibilidade suportada.
- [ ] Definir SLA interno por severidade/exposição, distinto dos compromissos oficiais.

## G. Zabbix, logs, monitorização e resposta
- [ ] Registar cada router no Zabbix antes da aceitação operacional.
- [ ] Confirmar host, inventário, template, tags, proxy/canal privado e método cifrado de recolha.
- [ ] Alertar para router offline, falha WAN, flash baixo, falhas de autenticação observáveis, alteração inesperada e atualização pendente.
- [ ] Testar alertas, eventos de recuperação e distinção entre falha do router, proxy, túnel e servidor.
- [ ] Separar credenciais read-only de monitorização das credenciais de operação.
- [ ] Definir eventos, severidade, destino e retenção.
- [ ] Minimizar dados pessoais e mascarar identificadores antes de exportar logs.
- [ ] Definir runbook para credenciais comprometidas, router comprometido, perda de acesso e rollback.
- [ ] Guardar evidências fora do router, com acesso controlado e sincronização temporal.

## H. Critério de aprovação
Classificar cada item como N/A justificado, aprovado com evidência, falhado ou pendente. Um teste deve indicar origem/destino, protocolo/porta, família IP, ferramenta, resultado esperado/observado e data. Aprovação exige revisão de risco residual e monitorização Zabbix funcional.
