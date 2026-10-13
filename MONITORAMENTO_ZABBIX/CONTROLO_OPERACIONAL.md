# Controlo operacional de routers através do Zabbix

**Estado:** especificação; não há ações implementadas.

## Objetivo
Fazer do Zabbix a consola operacional central para incidentes e operações de frota, preservando controlo de acesso, rastreabilidade e recuperação.

## Classes de ação

### Classe A — leitura e diagnóstico
Pode ser automatizada após revisão:
- ping/latência e testes de portas permitidas;
- recolha de versão, uptime e estado das interfaces;
- recolha de logs filtrados e sem segredos;
- diagnóstico de DNS/WAN/VPN;
- validação da configuração contra a baseline;
- geração de relatório de saúde.

### Classe B — mudança reversível de baixo risco
Exige autorização por função e execução pelo runner restrito:
- reiniciar um serviço não crítico;
- atualizar um parâmetro aprovado;
- executar backup cifrado;
- testar ou renovar um túnel de gestão, com caminho de recuperação.

### Classe C — alto impacto
Exige aprovação explícita, janela de manutenção, preflight, backup testado, acesso alternativo e rollback:
- alteração de firewall, VLAN, rotas, DNS, Wi-Fi ou endereço de gestão;
- reinício do router;
- atualização/downgrade de firmware;
- alteração de credenciais, chaves ou método de acesso;
- aplicar ou reverter um perfil de configuração completo.

## Guardrails obrigatórios
1. A ação seleciona um identificador de host registado; não aceitar IP/host arbitrário de um campo livre.
2. O runner valida tags, modelo, revisão, release e estado de homologação antes de agir.
3. Lista de comandos permitidos e parâmetros tipados; proibir shell livre, concatenação de entrada do utilizador e execução arbitrária.
4. Identidade de execução dedicada, privilégios mínimos e segredos fora do Git e dos parâmetros/logs do Zabbix.
5. Guardar quem solicitou, quem aprovou, host, ação, versão de configuração, hora, resultado e rollback.
6. Idempotência, timeout, limite de concorrência e bloqueio de ações em massa por defeito.
7. Canary: aplicar primeiro a um router de laboratório e depois a um lote pequeno.
8. Confirmar conectividade e métricas após a mudança; abortar/rollback se falhar.
9. Firmware só pode ser atualizado por fluxo específico que verifique imagem, assinatura/hash quando publicado, target e instruções oficiais.
10. Nunca usar scripts de descoberta automática para executar alterações destrutivas.

## Estados de uma operação
REQUESTED → VALIDATED → APPROVED → EXECUTING → VERIFYING → SUCCEEDED

Estados alternativos: REJECTED, FAILED, ROLLED_BACK, MANUAL_INTERVENTION_REQUIRED.

## Aprovação
- Diagnóstico read-only: pode ser automático dentro de limites e com registo.
- Mudança reversível: aprovação por operador autorizado, de acordo com política.
- Firewall/firmware/acesso/credenciais/reboot: aprovação explícita e janela de manutenção.
- Operações em lote: aprovação separada, limite por lote e prova de sucesso do canary.

## Limites técnicos
O Zabbix fornece monitorização, triggers, ações e execução de scripts/remote commands conforme a versão e configuração. Não substitui automaticamente um sistema de gestão de configuração. A arquitetura XFI deve usar uma camada de automação estreita e auditável para operações que precisem de lógica, preflight, validação e rollback.
