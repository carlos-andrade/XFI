# Arquitetura — Zabbix como centro operacional de routers

**Estado:** proposta documental; requer validação da versão Zabbix e do ambiente de rede.

## Modelo lógico

    Zabbix Server / Frontend
        +-- Zabbix Proxy(s) por site/região/rede, quando necessário
        |       +-- SNMPv3 / agente cifrado / checks permitidos
        |       +-- Routers OpenWrt geridos
        +-- Alertas, dashboards, inventário e auditoria
        +-- Ações autorizadas
                +-- Runner de automação restrito
                        +-- VPN de gestão / canal privado
                                +-- API/SSH restrito do router

O diagrama é conceptual. A topologia final depende do Zabbix já existente, da segmentação e de como cada cliente se liga à XFI.

## Princípios de ligação
- O tráfego de gestão deve passar por VPN/túnel privado ou por uma arquitetura de proxy que evite expor serviços de administração na Internet.
- Preferir Zabbix Proxy para redes remotas/filiais quando a arquitetura o justificar; dimensionar e proteger cada proxy.
- A monitorização deve usar credenciais só de leitura sempre que possível e permissões limitadas por OID/serviço.
- Para Zabbix Agent, preferir canal cifrado suportado pela versão e pacote OpenWrt; confirmar se o pacote tem TLS/OpenSSL/GnuTLS e se a versão instalada suporta a opção.
- Para SNMP, preferir SNMPv3 authPriv, origem limitada ao proxy/servidor autorizado e firewall a bloquear as restantes origens.
- Não permitir acesso público a LuCI, SSH, ubus/RPC ou endpoint de gestão para “facilitar” o Zabbix.
- Não assumir que todos os modelos suportam os mesmos sensores, SNMP, agente ou métricas Wi-Fi. O template deve adaptar-se ao hardware e à versão.

## O que significa “todo o controlo via Zabbix”
O Zabbix é a consola central e o mecanismo de orquestração de operações autorizadas. A monitorização pode ser nativa (SNMP/agent/HTTP). Para alterações complexas, o Zabbix deve invocar ações predefinidas através de um runner controlado, que valida alvo, modelo, versão, autorização e rollback. O runner não pode aceitar comandos arbitrários fornecidos em campos livres do Zabbix.

Ações predefinidas podem incluir:
- recolher diagnóstico não sensível;
- validar estado/configuração contra baseline;
- solicitar backup cifrado para armazenamento aprovado;
- executar teste de conectividade;
- aplicar configuração versionada após aprovação;
- reiniciar serviço específico ou router apenas com autorização e janela definida;
- iniciar atualização de firmware apenas em fluxo separado, com preflight, imagem verificada, backup e recuperação.

## Disponibilidade e isolamento de falhas
- Monitorizar tanto router como caminho de gestão, proxy e servidor Zabbix.
- Criar alertas para falha do router, WAN, proxy e servidor com dependências apropriadas para reduzir alertas em cascata.
- Guardar configuração desejada e evidências fora do router, em armazenamento de acesso controlado.
- Não considerar “sem dados no Zabbix” como prova de que o router está offline até avaliar proxy, túnel e caminho de gestão.

## Requisitos antes de implementar
1. Confirmar versão e arquitetura atual do Zabbix XFI.
2. Definir redes de gestão, VPN, proxies e endereços de origem autorizados.
3. Identificar se cada modelo suporta SNMPv3, agente Zabbix com TLS ou se precisa de checks alternativos.
4. Definir armazenamento de segredos e integração de credenciais.
5. Aprovar lista de operações permitidas, aprovação humana e rollback.
