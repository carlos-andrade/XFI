# Plano de validação, homologação e rollback

**Estado:** plano proposto; nenhum teste físico foi executado nesta entrega documental.

## Pré-condições
- Identificar modelo e revisão de hardware sem ambiguidade.
- Obter imagem/release suportada de fonte oficial e verificar integridade conforme método disponível.
- Criar backup e testar recuperação.
- Ter acesso local ou out-of-band; evitar primeira aplicação remota sem recuperação.
- Usar dados/credenciais fictícios em testes documentados.
- Registar baseline de WAN, Wi-Fi, routing, DNS, DHCP, IPv4 e IPv6.

## Matriz mínima de testes
| ID | Teste | Resultado esperado | Evidência necessária |
|---|---|---|---|
| T-001 | Administração pela WAN | Bloqueada, salvo desenho explicitamente aprovado | Tentativa externa controlada e regra efetiva |
| T-002 | SSH/LuCI desde gestão | Apenas origens autorizadas | Testes positivos e negativos |
| T-003 | Guest para LAN/gestão | Bloqueado | Matriz de conectividade IPv4/IPv6 |
| T-004 | IoT para LAN/gestão | Bloqueado salvo exceções mínimas | Testes de cada exceção |
| T-005 | DNS exposto na WAN | Não acessível como resolver aberto | Testes TCP/UDP e firewall |
| T-006 | DNS rebinding | Proteção conforme política; exceções registadas | Configuração e caso de teste controlado |
| T-007 | WPA3/WPA2 | Modo aprovado funciona; modos inseguros ausentes | Configuração e associação |
| T-008 | Firewall reload/reboot | Política persiste | Diff e retestes |
| T-009 | IPv6 | Sem bypass face à política IPv4 | Testes equivalentes por família IP |
| T-010 | Atualização | Procedimento, backup e imagem compatíveis | Log de upgrade de laboratório |
| T-011 | Recuperação | Configuração/acesso recuperáveis no objetivo definido | Ensaio com duração |
| T-012 | Desempenho | Throughput, latência e recursos cumprem SLO acordado | Medições sob carga representativa |
| T-013 | Logs/monitorização | Eventos chegam sem segredos/dados excessivos | Eventos de teste mascarados |
| T-014 | Port forwards/UPnP | Apenas serviços aprovados publicados | Inventário e verificação externa autorizada |

## Sequência de homologação
1. Fixar hardware, release e pacotes.
2. Exportar config e diff para armazenamento protegido, sem segredos no Git.
3. Aplicar perfil numa bancada isolada.
4. Executar testes e regressões.
5. Rever regras efetivas, não apenas ficheiros de configuração.
6. Testar reinício e persistência.
7. Ensaiar atualização e recuperação.
8. Obter revisão técnica e aprovação de risco residual.
9. Produzir ficha com hashes de imagem/perfil, versões, ambiente e resultados.
10. Autorizar rollout gradual monitorizado apenas após aprovação.

## Rollback
Definir gatilhos como perda de gestão/WAN, falha de DHCP/DNS, violação de isolamento, desempenho insuficiente ou instabilidade. Suspender expansão após falha crítica; utilizar recuperação específica do dispositivo; confirmar gestão, WAN, DHCP, DNS, Wi-Fi e segmentação após rollback; documentar causa, duração, impacto e prevenção.

## Limites
Testes documentais não provam segurança em produção. Scanner e ensaios devem ocorrer apenas em equipamentos/redes sob controlo e com autorização. Não executar testes intrusivos contra clientes/terceiros sem autorização explícita.
