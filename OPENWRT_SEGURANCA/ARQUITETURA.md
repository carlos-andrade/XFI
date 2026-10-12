# Arquitetura de referência — OpenWrt para clientes XFI

**Estado:** proposta documental; não validada para um cliente específico.

## Zonas lógicas

| Zona | Finalidade | Política de referência |
|---|---|---|
| WAN | Ligação ao operador/Internet | Negar ligações de entrada não solicitadas; abrir apenas o estritamente necessário |
| MANAGEMENT | Administração de routers/APs e serviços de gestão | Acesso por dispositivos e origens autorizados; sem administração exposta à Internet |
| TRUSTED/LAN | Equipamentos pessoais/empresariais confiáveis | Permitir apenas fluxos necessários; restringir acesso ao plano de gestão |
| GUEST | Visitantes | Acesso à Internet; bloquear redes internas e gestão |
| IoT | Equipamentos de confiança reduzida | Bloquear movimento lateral; exceções individualizadas para destinos necessários |
| SERVICES (opcional) | Serviços internos publicados | Fluxos explícitos, logs e publicação mínima |
| VPN (opcional) | Gestão remota ou site-to-site | Autenticação forte, autorização por rede/identidade e rotas mínimas |

Não implementar todas as zonas por defeito; adequar ao hardware e caso de uso.

## Plano de gestão
- Preferir administração por rede de gestão confiável ou VPN.
- Não publicar LuCI, SSH, RPC/ubus nem outros planos administrativos diretamente na WAN.
- Desativar serviços não necessários e remover credenciais padrão.
- Usar passwords únicas, robustas, guardadas em gestor de segredos; preferir chaves SSH individuais quando compatíveis.
- Usar HTTPS/TLS para a interface web quando o desenho o exigir, com confiança de certificados corretamente gerida.
- Restringir origens e serviços administrativos quando suportado; manter acesso de emergência testado.

## Firewall e encaminhamento
- Nas versões com firewall4, gerir regras via UCI em `/etc/config/firewall`; `fw4` gera regras nftables.
- Não adicionar regras nftables avulsas sem entender integração com fw4 e testar reload/reboot.
- Aplicar negação por omissão entre zonas e permitir fluxos documentados.
- Validar IPv4 e IPv6: regras incompletas num protocolo podem criar bypass.
- Rever port forwards, UPnP, NAT-PMP, PCP, DMZ e descoberta; desativar se desnecessários.
- Rever DNS rebinding e documentar exceções.

## Wi-Fi
- Preferir WPA3-SAE quando clientes e drivers forem compatíveis; usar WPA2-AES/CCMP quando necessário.
- Não usar WEP, WPA legado ou TKIP.
- Usar SSIDs/credenciais diferentes por domínio de confiança.
- Isolar convidados e IoT com políticas de rede/firewall; SSID separado, sozinho, não garante isolamento.
- Definir país, canais e potência conforme a jurisdição e capacidades do equipamento.

## DNS e endpoint de rede
- Definir resolvers, privacidade, retenção de logs e política por contrato/jurisdição.
- DoH/DoT podem proteger o trecho até ao resolver, mas não substituem autenticação, firewall ou isolamento.
- DNS filtering não é infalível; VPN, DoH externo, IP direto ou protocolos alternativos podem contorná-lo se não houver controles complementares.
- Definir protocolos de bypass permitidos e política para dispositivos pessoais.

## Firmware e pacotes
- Inventariar fabricante, modelo, revisão, target/subtarget, flash/RAM, rádio/driver, versão e recuperação.
- Instalar imagem destinada exatamente ao dispositivo e verificar integridade conforme a publicação oficial.
- Preparar sysupgrade com backup testado, manifesto de pacotes, compatibilidade, janela e rollback.
- Tratar snapshots/builds personalizados como risco distinto; fixar origem, commit, toolchain e processo de build.
- Acompanhar advisories/releases e definir SLA interno baseado em gravidade e exposição.

## Observabilidade
Recolher o mínimo necessário: versão/uptime, WAN, interfaces, carga, memória, flash, Wi-Fi, estado de serviço e eventos relevantes. Definir métricas, alertas, retenção, acesso e mascaramento antes de ativar a recolha.
