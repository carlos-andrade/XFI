# Matriz de homologação — router, firmware e monitorização

**Estado:** modelo em branco; nenhum router está homologado por este ficheiro.

## 1. Regra
A homologação é específica para **fabricante + modelo + revisão de hardware + firmware + método de monitorização + versão do Zabbix**. Uma alteração material a qualquer componente exige revalidação proporcional ao risco.

## 2. Registo de homologação

| Campo | Valor |
|---|---|
| ID do teste | PENDENTE |
| Fabricante/modelo | PENDENTE |
| Revisão de hardware | PENDENTE |
| Firmware/OpenWrt | PENDENTE |
| Zabbix Server/Frontend | PENDENTE |
| Proxy e versão | PENDENTE / N/A |
| Método | ICMP / SNMPv3 / agente / outro |
| Itens testados | PENDENTE |
| Triggers e recuperação | PENDENTE |
| Segurança do canal | PENDENTE |
| Carga observada | PENDENTE |
| Teste de falha do caminho | PENDENTE |
| Teste de recuperação | PENDENTE |
| Evidência não sensível | PENDENTE |
| Resultado | NÃO TESTADO |
| Aprovador/data | PENDENTE |
| Commit do relatório | PENDENTE |

## 3. Testes mínimos
- [ ] Identidade do equipamento e versão confirmadas.
- [ ] Host no grupo correto, com tags não sensíveis.
- [ ] Comunicação apenas pelo caminho autorizado.
- [ ] Itens obrigatórios recolhem dados coerentes.
- [ ] WAN e interfaces são identificadas corretamente.
- [ ] Falha do router é distinguida de falha do proxy/túnel.
- [ ] Triggers ativam e recuperam nos cenários de teste.
- [ ] Não existem credenciais em macros, logs, tags ou exportações.
- [ ] O router mantém recursos aceitáveis durante a recolha.
- [ ] A configuração pode ser removida/revertida sem perda de acesso.
- [ ] Limitações e itens não suportados ficam registados.

## 4. Estados controlados
- **NÃO TESTADO:** sem execução documentada.
- **EM TESTE:** testes iniciados, sem aprovação final.
- **APROVADO EM LABORATÓRIO:** testes concluídos para a combinação exata; não autoriza automaticamente produção.
- **APROVADO PARA PILOTO:** lote e plano de recuperação aprovados.
- **PRODUÇÃO:** critérios operacionais e de segurança aprovados.
- **SUSPENSO:** falha, mudança material ou evidência de risco exige reavaliação.

## 5. Regra de bloqueio
Um equipamento não está homologado apenas por aparecer no Zabbix ou responder a ping. É necessária evidência dos itens, alertas, recuperação, segurança e limites de recursos aplicáveis.
