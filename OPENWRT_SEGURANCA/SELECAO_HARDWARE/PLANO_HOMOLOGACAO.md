# Plano de homologação de hardware XFI

**Estado:** planeado; ainda não executado. Não existem equipamentos físicos validados neste registo.

## Fase 1 — diligência documental

- [ ] Confirmar modelo, revisão e variante regional na etiqueta/ficha do fornecedor.
- [ ] Abrir página exata na OpenWrt Table of Hardware.
- [ ] Confirmar release suportada, target/subtarget e imagem de instalação/upgrading.
- [ ] Ler avisos, issues de bloqueio, regressões e comentários na página do dispositivo.
- [ ] Confirmar RAM/flash utilizáveis, driver Wi-Fi, VLANs, portas e requisitos do cliente.
- [ ] Confirmar método de recuperação independente e os materiais necessários.
- [ ] Confirmar disponibilidade/garantia/IVA/devolução em Portugal/UE e custo de unidade suplente.

**Saída obrigatória:** ficha de hardware atualizada e riscos residuais documentados.

## Fase 2 — equipamento isolado

- [ ] Registar número de modelo/revisão sem publicar serial, MAC ou identificadores privados.
- [ ] Guardar firmware original e instruções de recuperação legítimas.
- [ ] Validar assinatura/hash da imagem quando publicado e conferir o target.
- [ ] Fazer backup de configuração inicial e registar a versão.
- [ ] Instalar OpenWrt seguindo apenas instruções específicas do modelo.
- [ ] Testar recuperação a partir de cenário de falha controlado e com método documentado.
- [ ] Medir estabilidade, temperatura, consumo e throughput por cabos e Wi-Fi.

Não aplicar firmware a clientes durante a homologação. Evitar testes que possam afetar redes externas ou equipamentos não autorizados.

## Fase 3 — testes de segurança e função

- [ ] Testar tráfego de entrada WAN IPv4 e IPv6 não solicitado.
- [ ] Confirmar que a gestão não é acessível a partir da WAN.
- [ ] Testar isolamento entre LAN de gestão, rede principal, convidados e IoT.
- [ ] Testar DNS/DHCP/NTP, IPv6, roaming e serviços legítimos.
- [ ] Confirmar regras firewall via UCI/fw4 e ausência de regras manuais conflitantes.
- [ ] Testar Wi-Fi e múltiplos SSIDs no driver/release selecionados.
- [ ] Medir latência sob carga e throughput com SQM, VPN e firewall quando aplicáveis.
- [ ] Confirmar atualizações, restauração de backup e reinstalação de pacotes.
- [ ] Rever logs sem recolher dados pessoais desnecessários.
- [ ] Anotar regressões e repetir o teste em mais de uma unidade quando viável.

## Fase 4 — decisão

Registar uma de quatro decisões:
- **Aprovado para perfil X:** todos os critérios obrigatórios foram cumpridos no modelo/revisão/versão especificados.
- **Aprovado com restrições:** limitações explícitas, perfil e condições registados.
- **Reprovado:** falha ou risco não aceitável.
- **Adiado:** evidência insuficiente ou testes pendentes.

A aprovação expira se houver alteração relevante de revisão de hardware, target, driver, release, firmware OEM, aviso de segurança ou disponibilidade de recuperação. Estabelecer rotina de revisão.

## Fase 5 — implantação controlada

Só após aprovação:
- manter imagens e configurações versionadas, sem segredos;
- atribuir configuração e credenciais únicas por cliente;
- executar preflight e verificação pós-implantação;
- aplicar em lote piloto pequeno antes de expansão;
- manter rollback, contacto do cliente e janela de manutenção;
- definir política para atualizações de firmware, avisos de segurança, incidentes e fim de vida.

## Relatório mínimo por equipamento

Modelo/revisão | SKU/região | OpenWrt release e target | imagem e hash | procedimento de instalação | recuperação testada | testes e resultados | vulnerabilidades/limitações conhecidas | preços/garantia | perfil permitido | decisão | data e responsável.
