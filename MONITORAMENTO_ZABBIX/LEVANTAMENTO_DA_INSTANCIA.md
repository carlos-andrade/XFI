# Levantamento da instância Zabbix XFI

**Estado:** procedimento preparado; ainda não executado na infraestrutura.  
**Objetivo:** recolher apenas os dados técnicos necessários para escolher os templates e a arquitetura.  
**Segurança:** não enviar palavras-passe, tokens, chaves, ficheiros de configuração completos, endereços públicos sensíveis ou dados pessoais de clientes.

## 1. Dados a registar
- Versão exata do Zabbix Server e Frontend.
- Sistema operativo e método de instalação: pacotes, Docker/Compose ou outro.
- Existência e versão de Zabbix Proxy(s), modo ativo/passivo e localização.
- Existência de VPN de gestão e redes de gestão autorizadas.
- Número aproximado de hosts atuais e crescimento esperado.
- Método de alertas e escalonamento.
- Política de backups, retenção, manutenção e acesso por função.
- Disponibilidade de laboratório isolado ou router de teste.

## 2. Ubuntu/Debian instalado por pacotes
Executar no servidor, em sessão administrativa autorizada:

~~~bash
zabbix_server -V 2>/dev/null | head -n 3
zabbix_proxy -V 2>/dev/null | head -n 3
zabbix_agent2 -V 2>/dev/null | head -n 3
zabbix_agentd -V 2>/dev/null | head -n 3
dpkg-query -W -f='\${binary:Package}\\t\${Version}\\n' 'zabbix*' 2>/dev/null
systemctl --no-pager --type=service | grep -Ei 'zabbix|nginx|apache'
~~~

Comandos para componentes não instalados podem não produzir saída; isso não é, isoladamente, uma falha.

## 3. Instalação Docker/Compose
Executar no host que gere os containers:

~~~bash
docker ps --format 'table {{.Names}}\\t{{.Image}}\\t{{.Status}}'
docker compose ps
~~~

Não publicar variáveis de ambiente, ficheiros .env, saída completa de docker inspect ou volumes com configuração. A tag da imagem é uma pista; confirmar a versão efetivamente executada.

## 4. Confirmar no Frontend
Na interface Web do Zabbix, consultar a informação de versão apresentada pela aplicação (por exemplo, página About/Acerca, conforme a versão). Registar a versão completa, incluindo revisão quando disponível.

## 5. Resposta segura
Copiar apenas estes campos técnicos, sem segredos:

| Campo | Valor |
|---|---|
| Versão Server | PENDENTE |
| Versão Frontend | PENDENTE |
| Sistema operativo | PENDENTE |
| Instalação | pacotes / Docker / outra |
| Proxy(s) | não / sim / desconhecido |
| VPN de gestão | não / sim / planeada |
| Hosts atuais (aprox.) | PENDENTE |
| Laboratório disponível | não / sim / por definir |
| Janela de manutenção aprovada | não / sim / por definir |

## 6. Critério de conclusão
O levantamento só fica concluído quando os valores forem confirmados na instância real. Este documento não prova acesso ao servidor nem execução dos comandos. A seleção de templates e ações específicos da versão permanece bloqueada até então.
