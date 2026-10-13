# XFI — Monitorização Zabbix de routers OpenWrt

**Estado:** especificação inicial documentada; não implementada nem testada em produção.  
**Regra obrigatória:** todos os routers OpenWrt geridos pela XFI devem estar inventariados e monitorizados pelo Zabbix. O Zabbix será o ponto central de observabilidade, alertas, inventário operacional e acionamento controlado de operações autorizadas.

## Objetivo
Centralizar a gestão operacional da frota: disponibilidade, WAN, interfaces, carga, memória, armazenamento, Wi-Fi, versão de firmware, eventos, alertas, manutenção e execução auditável de ações permitidas.

**Distinção importante:** o Zabbix é a plataforma central de monitorização e o ponto de entrada operacional. Para tarefas de configuração que não sejam nativas do Zabbix, deve chamar uma camada de automação restrita e auditada. Não se deve converter o Zabbix num terminal remoto genérico nem expor interfaces administrativas dos routers à Internet.

## Documentos
- [Arquitetura de monitorização e controlo](ARQUITETURA.md)
- [Inventário de métricas e alertas](METRICAS_E_ALERTAS.md)
- [Modelo de controlo operacional](CONTROLO_OPERACIONAL.md)
- [Segurança, acessos e segredos](SEGURANCA_E_ACESSOS.md)
- [Plano de implementação e aceitação](PLANO_IMPLEMENTACAO.md)
- [Levantamento seguro da instância Zabbix](LEVANTAMENTO_DA_INSTANCIA.md)
- [Especificação lógica do template XFI OpenWrt](ESPECIFICACAO_TEMPLATE_XFI_OPENWRT.md)
- [Modelo CSV de inventário](MODELO_INVENTARIO.csv)
- [Matriz de homologação por router/firmware/versão](MATRIZ_DE_HOMOLOGACAO.md)

## Política de versão Zabbix

**Regra XFI:** utilizar sempre a versão mais recente **estável e de produção** do Zabbix, confirmada na página oficial de downloads/notas de lançamento imediatamente antes da instalação ou atualização. Não adotar versões alpha, beta ou release candidate em produção. A atualização deve seguir as notas oficiais, compatibilidade de sistema operativo/base de dados/PHP, backup verificado e testes de regressão.

**Referência consultada em 2026-10-13:** a página oficial de downloads indica Zabbix 7.4.15 como versão 7.4 disponível e Zabbix 8.0.0rc1 como pré-lançamento; portanto, para produção nesta data, a referência é a linha estável 7.4.15, salvo nova versão estável publicada antes da implementação. Confirmar novamente no momento da instalação. Fontes: [downloads oficiais](https://www.zabbix.com/download_sources), [notas oficiais de lançamento](https://www.zabbix.com/release_notes), [roadmap oficial](https://www.zabbix.com/roadmap).

## Política de versão Zabbix

A XFI utilizará sempre a versão mais recente **estável de produção** do Zabbix. Não usar alpha, beta ou release candidate em produção. Antes de instalar ou atualizar, consultar os downloads e notas oficiais, validar compatibilidade, realizar backup verificável e preparar rollback.

Na consulta de 2026-10-13, a página oficial indicava Zabbix 7.4.15 como release da série 7.4 e Zabbix 8.0.0rc1 como pré-lançamento. Assim, a referência para produção nessa data é 7.4.15, mas deve ser novamente confirmada imediatamente antes da mudança.

Fontes oficiais: https://www.zabbix.com/download_sources · https://www.zabbix.com/release_notes · https://www.zabbix.com/roadmap

## Requisitos obrigatórios
1. Nenhum router entra em serviço sem host no Zabbix, grupo, tags, template aplicável e contacto/escala de alertas.
2. Todos os routers devem reportar, no mínimo, disponibilidade, estado WAN, tráfego das interfaces, uptime, recursos básicos, versão de firmware e sinais de degradação suportados pelo hardware.
3. Usar SNMPv3 com autenticação e privacidade (authPriv) quando o agente e o equipamento o suportarem adequadamente; caso contrário, escolher método alternativo cifrado e documentar a exceção. Não usar a comunidade SNMP pública nem expor SNMP à WAN.
4. Preferir Zabbix Proxy ou túnel privado para redes de clientes atrás de NAT; nunca abrir a interface de administração do router para o servidor Zabbix através da Internet pública.
5. Ações que alterem firewall, firmware, credenciais, interfaces, VPN ou reiniciem um router exigem controlo de acesso, registo, confirmação/aprovação adequada e plano de rollback.
6. O sistema deve detetar perda de monitorização e diferenciar “router offline” de “Zabbix/proxy sem comunicação”.
7. Dados pessoais, credenciais, chaves, tokens e backups de configuração com segredos nunca devem ser guardados neste repositório.
8. Definir retenção de métricas e logs, acesso por função, auditoria e minimização de dados antes de ativar recolha em clientes.

## Fontes oficiais
- [Documentação Zabbix 7.4 — SNMP agent](https://www.zabbix.com/documentation/7.4/pt/manual/config/items/itemtypes/snmp)
- [Documentação Zabbix — descoberta de rede](https://www.zabbix.com/documentation/8.0/en/manual/discovery/network_discovery)
- [Wiki OpenWrt — Zabbix network monitoring](https://openwrt.org/docs/guide-user/services/network_monitoring/zabbix)
- [OpenWrt — segurança e hardening](https://openwrt.org/docs/guide-user/security/openwrt_security)

A política de versão-alvo é a mais recente estável; a versão efetivamente instalada na infraestrutura XFI ainda tem de ser confirmada para decidir se é necessária atualização e para escolher templates, funções e formato de importação definitivos.

## Estado de aceitação
A pasta é DOCUMENTADA, não implementada. Ainda não foram criados hosts, templates, proxies, credenciais, ações ou dashboards na instância Zabbix; não foi efetuado teste com routers físicos.


## Próxima etapa operacional
Executar o levantamento descrito em [LEVANTAMENTO_DA_INSTANCIA.md](LEVANTAMENTO_DA_INSTANCIA.md) e registar a versão/topologia confirmadas. Até essa evidência existir, não gerar nem importar templates específicos de versão, nem ativar ações de escrita. O modelo de inventário e a especificação lógica já podem ser revistos sem acesso à instância.
