# Matriz de hardware por perfil de cliente

**Estado:** segmentação comercial e técnica proposta; valores abaixo não são cotação de mercado.

## Perfis de serviço

| Perfil | Contexto típico | Requisitos do router | Estrutura recomendada | Critério de custo |
|---|---|---|---|---|
| Essencial | Cliente sensível ao preço, utilização básica | Firmware suportado; pelo menos 128 MB RAM/16 MB flash como filtro preliminar; firewall stateful, IPv4/IPv6, Wi-Fi e Ethernet compatíveis | Um router simples, perfil gerido e poucas funções adicionais | Minimizar custo total sem usar hardware obsoleto ou com recuperação arriscada |
| Familiar | Vários telemóveis, PCs, TV, IoT e convidados | Mais recursos, VLAN/SSID segmentáveis, DNS seguro, WPA2-AES/WPA3 conforme compatibilidade e monitorização básica | Router único se cobertura e capacidade forem suficientes; separar convidados/IoT quando possível | Pagar por isolamento e margem real, não apenas por velocidade anunciada |
| Potente / trabalho remoto | Muitas ligações, upload/download intensivo, casa grande, videoconferência | CPU e RAM confortáveis, portas gigabit ou 2.5GbE conforme ISP, drivers Wi-Fi mantidos, SQM/VPN se exigido | Router capaz ou router + APs | Validar throughput, latência sob carga e cobertura no local |
| Avançado / profissional | VPN, VLANs, múltiplas redes, regras estritas, maior controlo | CPU/RAM e armazenamento com margem, suporte VPN, logs, backup e recuperação testada | Router/firewall dedicado + APs/switches geridos | TCO inclui suporte e substituição, não só equipamento |
| Especial / viagem | Mobilidade, hotel, Wi-Fi público, pequeno escritório temporário | Form factor pequeno, alimentação adequada, suporte de cliente VPN e políticas de firewall | Router portátil com perfil restrito | Separar da gama residencial e testar bateria/USB/rede conforme o equipamento |

## Controlos comuns em todos os perfis

- alterar credenciais administrativas e usar segredos únicos por cliente, nunca password universal;
- administração só pela rede de gestão, sem acesso de administração da WAN por padrão;
- firewall WAN com entrada não solicitada bloqueada e regras IPv4/IPv6 testadas;
- atualizar para release suportada, com planeamento de manutenção e backup;
- não deixar UPnP, serviços remotos ou portas abertas sem justificação e registo;
- DNS seguro com proteção contra DNS rebinding quando adequada ao uso; não confundir isso com filtragem infalível;
- rede de convidados isolada; IoT segmentada conforme o modelo e as necessidades;
- Wi-Fi com protocolo e cifra fortes, WPS desligado quando disponível e credenciais distintas;
- backup cifrado e fora do router, com política de retenção; nunca enviar backups ou credenciais ao Git;
- testar recuperação, conectividade, DHCP, DNS, IPv6 e acesso aos serviços legítimos após cada mudança;
- política de logs/telemetria minimizada, com privacidade e transparência para o cliente.

## Decisão de compra

O preço de aquisição sozinho não define a classe. Um modelo barato sem suporte contínuo, sem imagem confiável ou sem recuperação verificável é potencialmente mais caro em incidentes e intervenções. Uma família de hardware reduz o custo de suporte, mas nenhum modelo serve automaticamente todos os clientes.

Os perfis comerciais devem ser acompanhados por uma ficha de requisitos, consulta ao cliente e aprovação antes de implementar. Ver [PERFIL_CLIENTE.md](../PERFIL_CLIENTE.md).
