# Levantamento da instância Zabbix XFI

**Estado:** procedimento preparado; ainda não executado na infraestrutura.  
**Objetivo:** recolher apenas os dados técnicos necessários para escolher os templates e a arquitetura.  
**Segurança:** não enviar palavras-passe, tokens, chaves, ficheiros de configuração completos, endereços públicos sensíveis ou dados pessoais de clientes.

## Política de versão-alvo
A XFI utiliza sempre a versão mais recente **estável de produção**, não versões alpha, beta ou release candidate. Antes de qualquer instalação/atualização, verificar o estado atual em [downloads oficiais](https://www.zabbix.com/download_sources) e [notas de lançamento](https://www.zabbix.com/release_notes), confirmar compatibilidade e preparar backup/rollback. A versão efetivamente instalada tem de ser recolhida para decidir o caminho de atualização.

Na consulta de 2026-10-13, o site oficial listava Zabbix 7.4.15 como versão 7.4 disponível e 8.0.0rc1 como pré-lançamento. Este registo é uma fotografia temporal, não uma autorização para ignorar versões estáveis publicadas depois.

## Política de versão-alvo
A XFI utiliza a versão estável mais recente de produção, nunca alpha, beta ou release candidate em produção. Antes de qualquer instalação/atualização, verificar os downloads e notas oficiais, confirmar compatibilidade, fazer backup verificável e preparar rollback. A versão atualmente instalada tem de ser recolhida para decidir o caminho de atualização.

Na consulta de 2026-10-13, a página oficial indicava 7.4.15 como release da série 7.4 e 8.0.0rc1 como pré-lançamento. Este é um registo temporal; voltar a verificar antes da mudança.

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
