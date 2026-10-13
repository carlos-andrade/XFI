# Levantamento de requisitos por perfil de cliente

**Estado:** template de requisitos; não constitui uma configuração pronta para implantação.

## Ficha do perfil

- **ID do perfil:** (ex.: HOME-BASE, PME-SEGMENTADA, HOTSPOT)
- **Classe de cliente:**
- **Número esperado de utilizadores/dispositivos:**
- **Velocidade WAN contratada / throughput real pretendido:**
- **Serviços que têm de funcionar:**
- **Serviços que devem ser bloqueados:**
- **Necessidade de VPN:**
- **Necessidade de Wi-Fi convidado:**
- **Necessidade de VLAN/IoT/serviços internos:**
- **Requisitos IPv6:**
- **Política DNS/filtragem e respetivas limitações:**
- **Requisitos de logging/telemetria e retenção:**
- **Acesso de suporte remoto autorizado:**
- **Janela de manutenção e objetivo de recuperação:**
- **SLA de disponibilidade e patching:**
- **Requisitos de privacidade/contrato:**
- **Aprovação responsável:**

## Matriz mínima de fluxos

| Origem | Destino | Política inicial | Exceção / motivo | Teste |
|---|---|---|---|---|
| WAN | Gestão do router | BLOQUEAR | Nenhuma por omissão | T-001 |
| GUEST | TRUSTED/LAN | BLOQUEAR | Só se explicitamente justificada | T-003 |
| GUEST | MANAGEMENT | BLOQUEAR | Nenhuma por omissão | T-003 |
| IoT | MANAGEMENT | BLOQUEAR | Exceção individual documentada | T-004 |
| TRUSTED/LAN | Internet | PERMITIR conforme política | Serviços e filtros contratados | T-012 |
| MANAGEMENT | Router | PERMITIR apenas origens autorizadas | Administração autenticada | T-002 |

Esta matriz é um ponto de partida. Deve ser adaptada à topologia e implementada com políticas equivalentes em IPv4 e IPv6.

## Princípio comercial

Não vender “segurança total”, “bloqueio de todo o malware” ou “impossibilidade de invasão”. Descrever os controlos concretos, o que cobrem, limitações, processo de atualização e responsabilidades do cliente.
