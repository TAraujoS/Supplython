## REGRAS DE CÓDIGO

- Código totalmente em inglês

### Branches

- **Nomenclatura**
- feat/feature-name
- Sempre criar uma **branch nova** a partir da **develop atualizada**
- **Uma branch** para cada **task/feature**

#

### **COMMITS**

| _Tipo_       | _Significado_              | _Descrição_                                                      |
| ------------ | -------------------------- | ---------------------------------------------------------------- |
| **feat**     | Features                   | Nova feature                                                     |
| **fix**      | Bug Fixes                  | Correção de bug                                                  |
| **refactor** | Code Refact­oring          | Mudança de código que afeta tanto bug como adiciona feature nova |
| **perf**     | Perfor­mance Improv­ements | Mudança para melhorar a performance                              |
| **test**     | Tests                      | Adicionar teste novo ou corrigir um existente                    |

<br>

**Quando for criar uma nova branch:**

1. Vá para a develop, faça um git pull origin develop.
2. Crie a tua branch a partir da develop
3. Trabalhe na sua feature
4. Ao **finalizar**, siga o fluxo:

```javascript
- git add .
- git commit -m "message"
- git pull origin develop
- git push origin nome-da-sua-branch
```