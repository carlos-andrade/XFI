# Catálogo de métricas e alertas para routers OpenWrt

**Estado:** requisitos propostos; os itens dependem do modelo, pacote, versão e método de recolha.

## Nível 1 — obrigatório para todos os routers

| Área | Métricas/estado | Alertas mínimos |
|---|---|---|
| Disponibilidade | Reachability pelo caminho de gestão; uptime quando disponível | Router sem resposta; monitorização/proxy indisponível; recuperação após falha |
| WAN | Estado da interface, endereço/rota quando aplicável, perda e latência para alvos definidos | WAN down; perda/latência acima de limiar; flapping |
| Interfaces | Estado operacional, bytes recebidos/enviados, erros/drops | Interface WAN/LAN down inesperadamente; crescimento anormal de erros |
| Sistema | Uptime, CPU/load, memória disponível, temperatura se exposta | CPU ou memória sustentadamente alta; temperatura crítica se suportada |
| Armazenamento | Flash/overlay disponível e uso, quando mensurável | Espaço abaixo de limite; falha de escrita |
| Firmware | Versão OpenWrt, kernel/target quando recolhível, data de última verificação de atualização | Versão não aprovada; suporte expirado; atualização de segurança pendente segundo política XFI |
| Serviços | DHCP/DNS e VPN quando usados; serviço de gestão autorizado | Serviço indisponível; VPN de gestão perdida |
| Estado Zabbix | Última recolha bem-sucedida, proxy, idade dos dados | Dados antigos; falha de coleta; proxy sem ligação |

## Nível 2 — recomendado quando suportado
- SSIDs/rádios e estado dos rádios Wi-Fi;
- número de clientes associados, sem recolher identidades desnecessárias;
- retransmissões, interferência, canais e utilização de rádio se os drivers expuserem dados confiáveis;
- estado de SQM/QoS, WireGuard/OpenVPN e túneis site-to-site;
- falhas de autenticação e alterações de configuração, quando os logs permitirem;
- tentativas de acesso administrativo negadas e mudanças de firewall;
- contagem de reinícios inesperados e eventos de watchdog;
- qualidade do DNS e conectividade a alvos de verificação acordados;
- estado do processo de backup e idade do último backup cifrado;
- compliance da configuração contra a baseline aprovada.

## Alertas iniciais
Os limiares seguintes são pontos de partida para laboratório, não defaults de produção. Calibrar por equipamento e cliente.

- Disponibilidade: 3 verificações consecutivas falhadas, com recuperação separada.
- WAN: down por mais de 60–120 segundos, excluindo janelas de manutenção.
- CPU: acima de 90% durante 5 minutos, se a métrica for fiável.
- Memória disponível: abaixo de 10% por 5 minutos, se suportado.
- Flash/overlay: menos de 15% livre ou menos de 5 MB, aplicando o limite mais conservador conforme o dispositivo.
- Erros de interface: crescimento sustentado acima da linha de base; evitar alertar apenas por contadores históricos.
- Versão/atualização: alerta quando uma versão aprovada deixa de receber suporte ou existe advisory aplicável com prazo excedido.
- Túnel de gestão: down fora de manutenção.
- Dados sem atualização: timeout baseado no intervalo de coleta e no proxy, não um valor único para toda a frota.

## Grupos e tags sugeridos
- Grupos: XFI/OpenWrt/Producao, XFI/OpenWrt/Laboratorio, XFI/OpenWrt/Manutencao, XFI/OpenWrt/Excecoes.
- Tags: vendor, model, hw_revision, openwrt_release, customer_tier, site_id pseudonimizado, management_path, proxy, criticality, firmware_channel, homologation_status.
- Não colocar nome completo, morada, telefone, password, chave ou dados pessoais do cliente em tags.

## Templates
Criar templates separados e versionados, começando por:
1. XFI OpenWrt - ICMP/Availability — disponibilidade e latência.
2. XFI OpenWrt - SNMP Generic — IF-MIB e métricas genéricas, se SNMP suportado.
3. XFI OpenWrt - Agent — recursos e serviços via agente seguro, se suportado.
4. XFI OpenWrt - Model Specific — dados adicionais por família/modelo.
5. XFI OpenWrt - Compliance — estado de baseline e atualizações, sem recolher segredos.

Não importar templates externos sem revisão de itens, macros, permissões, comandos e dependências.
