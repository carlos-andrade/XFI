# Especificação do template base XFI OpenWrt

**Estado:** especificação lógica; não é um ficheiro XML/YAML de importação e não foi testada numa instância.  
**Bloqueio de implementação:** confirmar a versão do Zabbix e homologar o método no modelo, revisão e firmware reais.

## Política de compatibilidade
A versão-alvo é sempre a versão estável mais recente disponível na data da implementação. O template deve ser testado nessa versão e não deve declarar compatibilidade com versões não testadas. Versões pré-lançamento não são alvo de produção.

## 1. Objetivo
Definir um conjunto mínimo consistente de itens, triggers, tags e macros para cada router OpenWrt gerido pela XFI.

## 2. Camadas de templates
1. **Disponibilidade:** ICMP/latência e idade da última recolha, conforme a topologia.
2. **Interfaces/SNMP:** IF-MIB e métricas genéricas apenas quando SNMP e OIDs estiverem confirmados.
3. **Sistema/agente:** CPU, memória, uptime e serviços apenas com agente compatível, suportado e protegido.
4. **Modelo específico:** métricas exclusivas de hardware/driver, com dependências explícitas.
5. **Conformidade:** firmware aprovado, estado de backup e resultado de baseline, sem recolher segredos.

Associar apenas camadas homologadas para a combinação modelo + revisão de hardware + firmware + método.

## 3. Inventário mínimo
- Identificador interno pseudonimizado do equipamento.
- Grupo operacional e criticidade.
- Fabricante, modelo e revisão física.
- Release OpenWrt e canal de firmware autorizado.
- Método de monitorização e caminho de gestão.
- Proxy atribuído, quando aplicável.
- Estado de homologação e data da última validação.
- Janela de manutenção e política de escalonamento.
- Estado da conectividade e data da última recolha válida.

Não colocar nome completo, morada, telefone, credenciais, chaves privadas ou tokens em nomes, tags, macros, notas ou inventário do Zabbix.

## 4. Macros e segredos
- Limiares configuráveis por perfil e validados antes de produção.
- Segredos apenas em campos protegidos ou cofre compatível; nunca em Git, texto simples, mensagens de trigger ou logs.
- Sem macros que permitam comandos shell, IPs arbitrários ou destinos não autorizados.
- Ajustar timeout e intervalos ao método, proxy e criticidade.

## 5. Triggers e recuperação
- Separar falha do router, proxy e servidor/caminho de gestão.
- Usar dependências para reduzir alertas em cascata.
- Configurar recuperação explícita e manutenção planeada.
- Aplicar duração sustentada a CPU, memória, latência e erros para reduzir ruído.
- Não tratar ausência de dados como prova isolada de router offline.
- Validar cada trigger com evento simulado e recuperação observada.

Os limiares numéricos de produção devem ser calibrados em laboratório; os valores iniciais no catálogo são hipóteses, não configurações aprovadas.

## 6. Segurança
- SNMPv3 authPriv quando suportado e homologado, com origem restringida ao caminho de gestão.
- Se usado agente, confirmar TLS, versão do pacote e compatibilidade com o Zabbix instalado.
- Preferir recolha read-only.
- Não expor LuCI, SSH, SNMP ou agente à Internet pública.
- Não importar templates externos sem revisão de comandos, macros, itens, descoberta, permissões e ações.
- Não habilitar ações de escrita no template base.

## 7. Testes antes de publicar
1. Importação sem erros na versão-alvo.
2. Associação ao host de laboratório e recolha de cada item.
3. Teste de perda e recuperação de conectividade.
4. Teste de falha de proxy/túnel sem falso diagnóstico do router.
5. Verificação de permissões, macros e ausência de segredos.
6. Verificação de carga no router, proxy e servidor.
7. Exportação e revisão do template resultante.
8. Registo de versão, commit, hash do artefacto, resultados e limitações.

## 8. Critério de publicação
O template só pode ser marcado **HOMOLOGADO** depois de importado e testado na versão Zabbix confirmada e numa combinação específica de router/revisão/firmware. Antes disso, o estado é **ESPECIFICAÇÃO**.
