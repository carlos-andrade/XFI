# Governança do domínio OpenWrt Security

## Autoridade normativa
A governança transversal segue o repositório [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA). Este diretório contém procedimentos específicos de segurança de roteadores no XFI e não substitui as normas centrais.

## Regra obrigatória — Zabbix
Todos os routers OpenWrt fornecidos, instalados ou geridos pela XFI têm de estar inventariados e monitorizados no Zabbix. O Zabbix é o ponto central de observabilidade, alertas e acionamento de operações autorizadas.

- Nenhum router deve ser considerado aceite para operação sem host, inventário, template, alertas e caminho de gestão seguro no Zabbix.
- Não expor LuCI, SSH, SNMP ou outros serviços administrativos na WAN pública para permitir a monitorização.
- Preferir SNMPv3 authPriv ou um método alternativo cifrado e suportado pelo modelo.
- Alterações complexas devem ser executadas por automação restrita e auditada, com validação, aprovação e rollback.
- A especificação de execução é mantida em [MONITORAMENTO_ZABBIX](../MONITORAMENTO_ZABBIX/README.md).
- Esta regra está DOCUMENTADA; não significa que a instância Zabbix já esteja configurada.

## Regra de fontes e recolha
- Usar a documentação pública OpenWrt como fonte primária para comportamento, configuração e compatibilidade.
- Preferir URLs e metadados de origem a cópias extensas do wiki. Registar URL, título, data de consulta e relevância.
- Para software, drivers e segurança, consultar também repositórios oficiais, avisos, notas de versão e páginas de suporte do dispositivo.
- “Usar todos os dados possíveis” significa recolha abrangente, legal, seletiva e rastreável — não scraping indiscriminado nem duplicação integral do site.
- Respeitar licenças, atribuição, termos de uso e limites de acesso; não contornar proteções anti-bot.
- Uma página wiki não prova que uma funcionalidade está disponível em qualquer dispositivo.
- Factos operacionais que possam mudar devem conter fonte e data de verificação.

## Estados obrigatórios
- **PLANEADO:** decidido, ainda sem implementação.
- **DOCUMENTADO:** especificação criada e revista.
- **IMPLEMENTADO:** configuração/código existe no caminho indicado.
- **TESTADO:** execução reproduzível realizada, com resultado registado.
- **HOMOLOGADO:** testes aprovados num conjunto definido de modelos e versões.
- **PRODUÇÃO:** implantação autorizada e monitorizada.
- **DEPRECADO:** não usar em novos deployments; plano de migração registado.

Nunca avançar de um estado para outro sem evidência adequada.

## Segredos e dados de clientes
- Nunca guardar passwords, chaves SSH privadas, tokens, credenciais PPPoE, configurações exportadas com segredos ou endereços identificáveis de clientes no Git.
- Usar exemplos sintéticos e valores claramente fictícios.
- Manter backups em armazenamento controlado, cifrado e com retenção definida; no repositório guardar apenas procedimento e checksum não sensível.
- Mascarar IPs públicos, MACs, SSIDs identificáveis, nomes e números de série em logs/evidências públicas.
- Definir acesso por função, registo de mudanças, retenção e resposta a incidentes.

## Gestão de alterações
1. Identificar motivo, impacto, versões e modelos afetados.
2. Rever fontes oficiais e changelogs.
3. Produzir diff antes de aplicar.
4. Validar em laboratório e equipamento não crítico.
5. Definir janela, recuperação e critérios de abortar.
6. Guardar evidências e commit.
7. Monitorizar após implantação e atualizar o registo.

Toda exceção deve ter responsável, justificação, ativos afetados, risco residual, compensações, prazo e data de revisão.
