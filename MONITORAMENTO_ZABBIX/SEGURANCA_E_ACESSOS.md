# Segurança e acessos — Zabbix e routers OpenWrt

**Estado:** requisitos documentais; não implementados.

## Identidade e autorização
- Usar contas individuais, MFA na interface web quando suportado e permissões por função.
- Separar perfis de visualização, operação de diagnóstico, aprovação de mudanças e administração da plataforma.
- Não partilhar contas administrativas.
- Restringir acesso à consola por VPN/rede de gestão, filtragem de origem e TLS.
- Rever periodicamente contas, API tokens, integrações e permissões.

## Transporte e credenciais
- Preferir SNMPv3 com autenticação e privacidade (authPriv) para dados SNMP quando suportado pelo agente/dispositivo.
- Quando usar Zabbix Agent, verificar se o pacote OpenWrt inclui TLS e configurar criptografia/autenticação compatível com a versão.
- Não usar SNMPv1/v2c em redes não confiáveis. Se uma limitação de hardware obrigar a uma exceção, isolar o tráfego, restringir a origem e registar risco, prazo e mitigação.
- Não expor SNMP, SSH, LuCI, ubus/RPC ou agente Zabbix na WAN pública.
- Credenciais únicas por router/cliente; nunca password universal.
- Armazenar segredos em mecanismo próprio, macros secretas ou vault compatível, sem os incluir em exports, commits, parâmetros de comandos ou logs.
- Rotacionar credenciais e testar o processo de rotação.

## Segurança da automação
- Runner de automação em segmento dedicado, com saída e destinos limitados.
- Chaves SSH com permissões mínimas, de preferência comandos restritos ou wrapper que aceite apenas operações predefinidas.
- Validar todos os parâmetros; não concatenar campos Zabbix em comandos shell.
- Usar TLS e verificação de identidade dos endpoints quando aplicável.
- Registar operações sem gravar passwords, tokens, chaves, configurações completas ou dados pessoais.
- Assinar/versionar os artefactos de configuração; rever alterações e manter rollback.
- Separar a credencial de monitorização read-only da credencial de operação.

## Privacidade e retenção
- Minimizar nomes, MACs, IPs públicos, SSIDs e logs que possam identificar clientes.
- Definir retenção de métricas e logs, acesso por função, exportação e eliminação.
- Informar os clientes sobre a monitorização e as finalidades operacionais, de acordo com os contratos e obrigações aplicáveis.
- Não armazenar configurações completas de router no Zabbix; recolher somente os campos necessários para compliance, evitando segredos.

## Resposta a incidentes
- Se o Zabbix, proxy ou runner for comprometido, suspender operações de escrita e preservar evidências.
- Se a credencial de gestão de um router for comprometida, revogar/rotacionar e rever os acessos.
- Se uma ação causar perda de acesso, parar rollout, usar recuperação aprovada e registar causa/rollback.
- Manter caminho de emergência fora do plano de gestão normal, protegido e testado.
