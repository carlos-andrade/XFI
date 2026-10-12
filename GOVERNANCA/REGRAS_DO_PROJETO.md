# XFI — Governança do Repositório

**Repositório oficial:** https://github.com/carlos-andrade/XFI  
**Branch principal:** `main`  
**Estado inicial validado em:** 2026-10-12  
**Responsável pelo projeto:** Carlos Andrade

## 1. Finalidade

Este repositório é a fonte oficial de referência, governança e histórico dos materiais produzidos especificamente no âmbito do projeto XFI.

## 2. Regra de persistência

Todo artefacto substancial produzido neste projeto deve ser persistido neste repositório quando tecnicamente compatível, incluindo documentação, especificações, decisões, planos, roadmaps, código, testes e relatórios de validação.

- A entrega na conversa não substitui a gravação no repositório.
- Antes de criar um ficheiro, verificar se já existe conteúdo equivalente.
- Preservar o histórico Git e evitar sobrescrever material existente sem leitura prévia.
- Após cada gravação, confirmar o commit e o caminho do ficheiro.
- Se não for possível gravar devido a permissões, indisponibilidade da integração ou limitações do formato, declarar explicitamente a limitação e não alegar que o material foi salvo.

## 3. Princípios de qualidade

1. **Rastreabilidade:** decisões importantes devem registar data, contexto, alternativas e consequência.
2. **Reprodutibilidade:** procedimentos técnicos devem incluir pré-requisitos, comandos, entradas, saídas esperadas e validação.
3. **Validação antes de publicação:** conferir estrutura, consistência, referências, testes e impacto.
4. **Separação de estados:** distinguir planeado, em desenvolvimento, testado, validado e publicado.
5. **Segurança:** não gravar tokens, palavras-passe, chaves privadas, credenciais ou dados pessoais sensíveis.
6. **Fonte de verdade:** quando houver divergência, verificar o histórico e os artefactos atuais do repositório antes de decidir.
7. **Honestidade operacional:** nunca declarar que um teste, execução, deploy ou publicação ocorreu sem evidência verificável.

## 4. Fluxo de trabalho obrigatório

1. Ler o README e os documentos relevantes antes de iniciar alterações.
2. Identificar o escopo e os artefactos a produzir.
3. Verificar se os caminhos já existem.
4. Criar ou atualizar os ficheiros necessários, preservando material válido.
5. Executar as verificações disponíveis; diferenciar verificações executadas das apenas propostas.
6. Rever o diff e procurar erros, contradições, segredos ou ficheiros desnecessários.
7. Registar as alterações no Git com uma mensagem objetiva.
8. Confirmar os caminhos e o commit resultante.
9. Resumir o resultado, os testes efetuados, as limitações e os próximos passos.

## 5. Estrutura inicial sugerida

```text
XFI/
├── README.md
├── LICENSE
├── GOVERNANCA/
│   └── REGRAS_DO_PROJETO.md
├── DOCUMENTACAO/
├── ROADMAP/
├── ARQUITETURA/
├── TESTES/
└── CHANGELOG.md
```

A estrutura é evolutiva. Criar subpastas adicionais apenas quando houver conteúdo real que justifique a sua existência. O Git não mantém pastas vazias sem ficheiros.

## 6. Limites de escopo

Esta regra cobre os materiais produzidos no âmbito do projeto XFI. Para outros projetos com repositórios oficiais próprios, os artefactos específicos desses projetos devem continuar a ser registados nos respetivos repositórios, salvo decisão explícita em contrário. O XFI pode conter governança transversal e referências para esses projetos, sem duplicar indiscriminadamente dados ou credenciais.

## 7. Critério de conclusão

Uma tarefa só deve ser descrita como **persistida** quando o commit correspondente tiver sido confirmado no GitHub. Deve ser descrita como **validada** apenas na medida das verificações efetivamente executadas e documentadas.
