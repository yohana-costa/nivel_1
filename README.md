# Desafio Nível 1 — PDV com Descontos

## O que o código faz

Este programa simula a lógica de um PDV (Ponto de Venda) que aplica descontos progressivos. Para cada compra, ele recebe o valor e a idade do cliente, aplica as regras de desconto e mostra o valor final em reais. O programa aceita várias compras seguidas e, ao encerrar, exibe um resumo do dia com a quantidade de compras, o total bruto, o total de descontos e o total final.

## Como ele faz

1. O código pede o **valor da compra**. Se for `0`, o loop termina.
2. Se o valor for negativo, mostra um aviso e pede novamente (`if` + `continue`).
3. Pede a **idade do cliente**. Se for negativa, mostra um aviso e pede novamente.
4. **Regra 1:** se a idade for maior ou igual a 65, aplica 20% de desconto.
5. **Regra 2:** se o valor *já descontado pela idade* for maior que 100, aplica mais 10%.
6. Mostra o valor final formatado com duas casas decimais (ex.: `R$ 144.00`).
7. Guarda a compra numa lista com `.append()`.
8. Ao final, percorre a lista com `for`, soma tudo e mostra o resumo do dia.

## Como rodar

```bash
python pdv.py
```

## Tabela de exemplos (casos de teste)

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|-----------|-------|----------------|----------------|----------------------|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

### Casos-limite

- **Caso 5:** 125 × 0.8 = 100. Como 100 não é *maior* que 100, os 10% não se aplicam.
- **Caso 10:** idade 64 não tem desconto por idade; só os 10% por valor.
- **Caso 7:** 101 × 0.9 = 90.90 — o valor é arredondado para duas casas decimais.