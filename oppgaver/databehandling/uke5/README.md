# Databehandling og algoritmer - øving

## Del 1 - uten hjelpemidler

### 1.1

```python
hallo = [{"b":[4,3,5], "a":[0]}, ["hei", "hallo"]]
print(hallo[1][1][1])
```

Hva printes?

Svar: `a`

### 1.2

```python
hallo = [{"b":[4,3,5], "a":[0]}, ["hei", "hallo"]]
for i in hallo[1]:
    print(i)
```

Hva printes?

Svar:

```
hei
hallo
```

### 1.3

```python
hallo = [{"b":[4,3,5], "a":[0]}, ["hei", "hallo"]]
for i in hallo[1][1]:
    print(i)
```

Hva printes?

Svar:

```
h
a
l
l
o
```


### 1.4

```python
a = {"a": [1,2,-1], "b": [9,-9,1]}
print(max(a["b"]))
```

Hva printes?

Svar: `9`

### 1.5

Skriv koden som Pseudokode.

- `liste` er en liste med tall: `[2, -4, 5, 1]`

```python
høyest = liste[0]
for tall in liste:
    if tall > høyest:
        høyest = tall
print(høyest)
```

Svar:

```
SET høyest TO første tall i lista
FOR EACH tall IN liste
  IF tall GREATER THAN høyest
    SET høyest TO tall
  ENDIF
ENDFOR

DISPLAY høyest
```
