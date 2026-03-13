
# 🧠 Laboratorio – Connect Four AI  
**Curso:** Inteligencia Artificial  
**Universidad:** Universidad del Valle de Guatemala  
**Autoras:** Camila Richter - 23183 y Marinés García - 23391
**Fecha:** 13/02/26

---

## 📌 Descripción

En este laboratorio se implementó una Inteligencia Artificial capaz de jugar **Connect Four (4 en línea)** utilizando algoritmos de búsqueda adversarial.

El objetivo fue:

- Implementar Minimax desde cero.
- Optimizarlo mediante Poda Alfa-Beta.
- Diseñar una heurística estratégica.
- Lograr que el agente juegue a un nivel competitivo.
- Comparar eficiencia entre Minimax puro y Alfa-Beta.

---

## 🎮 Reglas del Juego

- Tablero de 7 columnas × 6 filas.
- Gana quien conecte 4 fichas consecutivas (horizontal, vertical o diagonal).
- Juego de suma cero:
  - Victoria: +1000
  - Derrota: -1000
  - Empate: 0

---

## 📂 Estructura del Proyecto

```bash
├── main.py
├── Connect4.py
├── Minimax.py
├── AlphaBeta.py
├── RandomAgent.py
└── visual_game.py
```

---

## 🧠 Algoritmos Implementados

### 🔹 Minimax
Explora el árbol de juego hasta una profundidad limitada.

### 🔹 Poda Alfa-Beta
Optimización del Minimax que evita explorar ramas innecesarias, permitiendo mayor profundidad sin aumentar significativamente el costo computacional.

---

## 🧮 Función Heurística

Como no siempre es posible llegar a estados terminales, se diseñó una función `evaluate(board)` basada en:

- Control de la columna central  
- Ventanas de 4 posiciones  
- Tres fichas conectadas con un espacio libre  
- Penalización de amenazas del oponente  

Esto permite que el agente juegue estratégicamente aun con profundidad limitada.

---

## 🎥 Demostración

El agente fue evaluado contra:

1. 🤖 Agente Aleatorio  
2. 👤 Jugador humano  

Se utilizó profundidad 5 con Poda Alfa-Beta, mostrando en pantalla:

- Profundidad utilizada  
- Número de nodos explorados  
- Animación visual del tablero  
- Mensaje de victoria  

---

## ⚙️ Requisitos

```bash
pip install pygame numpy
```

---

## ▶️ Cómo Ejecutar

### Comparación Minimax vs Alpha-Beta

```bash
python main.py
```

### Juego visual

```bash
python visual_game.py
```

---

## 🏆 Conclusión

Se logró implementar una IA competitiva para Connect Four combinando búsqueda adversarial, optimización con poda y diseño heurístico estratégico.
