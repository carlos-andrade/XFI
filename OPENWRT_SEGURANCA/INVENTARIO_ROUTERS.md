# Inventário de routers e compatibilidade OpenWrt

**Estado:** modelo de inventário; nenhum router de produção foi ainda declarado como candidato.  
**Fonte de compatibilidade:** página oficial específica do dispositivo e [Table of Hardware](https://openwrt.org/toh/start).

## Regra de inclusão

Não comprar nem homologar um router apenas porque o fabricante/modelo aparece numa pesquisa. Confirmar o modelo e a revisão física exatos, o estado de suporte na release-alvo, a página individual, a instalação/recuperação e os recursos necessários. O nome comercial pode cobrir revisões incompatíveis.

## Ficha por dispositivo

Copiar esta ficha para cada combinação distinta de modelo e revisão:

- **ID interno não sensível:**
- **Fabricante:**
- **Modelo comercial exato:**
- **Revisão de hardware:**
- **SoC/CPU e arquitetura:**
- **RAM / flash:**
- **Portas Ethernet / switch / VLAN:**
- **Bandas Wi-Fi / chipset / driver:**
- **Target/subtarget OpenWrt:**
- **Release estável suportada verificada:**
- **Página oficial individual:**
- **Entrada na Table of Hardware:**
- **Estado de suporte e data da consulta:**
- **Imagem de instalação correta:**
- **Imagem sysupgrade correta:**
- **Verificação de integridade disponível:**
- **Método de recuperação testado:**
- **Limitações conhecidas / drivers / aceleração:**
- **VPN pretendida e desempenho medido:**
- **VLAN/guest/IoT testados:**
- **Responsável pela revisão:**
- **Estado:** PLANEADO / DOCUMENTADO / TESTADO / HOMOLOGADO / DEPRECADO
- **Evidência e commit:**
- **Risco residual:**

## Decisão de elegibilidade

Marcar **ELEGÍVEL PARA LABORATÓRIO** apenas quando a revisão física exata, release, imagem e método de recuperação estiverem confirmados em fonte oficial. Marcar **HOMOLOGADO** apenas após passar a matriz de testes e aprovação técnica. Se não existir suporte atual ou a recuperação não estiver compreendida, bloquear o uso em novos clientes.

## Lista inicial

| ID | Fabricante/modelo | Revisão | Release/target | Página oficial | Estado |
|---|---|---|---|---|---|
| R-001 | A definir | A definir | A verificar | A verificar | PENDENTE |

**Próxima entrada necessária:** routers efetivamente disponíveis para compra/instalação. Não preencher fabricante/modelo por suposição.
