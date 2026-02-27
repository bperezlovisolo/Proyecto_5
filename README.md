# Proyecto 5

## Predicción para la optimización de depósitos bancarios

## Objetivo del Proyecto

El objetivo de este proyecto es desarrollar y optimizar un modelo de ML para testear la probabilidad de los clientes den una respuesta afirmativa a abrir un deposito en el banco. 
El dataset presenta un desbalance significativo entre clases, por lo que priorizamos la mejora de Recall y F1-score en la clase minoritaria, en lugar de enfocarse únicamente en la accuracy global.

## Contexto del Negocio

El dataset proviene de una institución bancaria portuguesa que llevó a cabo campañas de marketing directo por teléfono para ofrecer depósitos a plazo. Estas campañas buscan identificar clientes con alta probabilidad de aceptación. Por ello, un modelo predictivo efectivo puede:

- Reducir costos.
- Incrementar la tasa de depósito.
- Optimizar los recursos. 

Este proyecto evalúa diversas estrategias para mejorar la capacidad de predicción de clientes que aceptan el producto ofrecido.

## Dataset

El dataset utilizado es el ank-full.csv, disponible en el *UCI Machine Learning Repository* (https://archive.ics.uci.edu/dataset/222/bank+marketing)

Características del dataset:

- Proviene de campañas de marketing telefónico de una entidad bancaria portuguesa.
- Más de 41k de filas.
- Incluye variables tanto numéricas como categóricas relacionadas con datos demográficos del cliente, detalles de las campañas, y el resultado de la oferta.
- La variable objetivo (`y`) indica si el cliente aceptó el depósito a plazo (`yes`) o no (`no`).

El dataset no contiene valores faltantes y presenta desbalance entre clases, con muchos más casos de “no” que de “yes”.

## Notas de Calidad del Dato

Durante la etapa de análisis verificamos:

- Ausencia de valores nulos.
- Correcta tipificación de variables (numéricas y categóricas).  
- Transformación de variables categóricas mediante One-Hot Encoding.  
- Escalado de variables numéricas con MinMaxScaler.

## Preguntas Clave

1. ¿Es posible mejorar la detección de la clase minoritaria sin afectar la accuracy?
2. ¿Qué técnica de manejo de desbalance resulta más efectiva: class_weight o SMOTE?
3. ¿Qué hiperparámetro podemos utilizar para el funcionamiento correcto del modelo?

## Proceso de Análisis

1. Análisis exploratorio de datos (EDA)
2. Preprocesamiento
   - One-Hot Encoding
   - Escalado con MinMaxScaler
3. División Train-Test
4. Entrenamiento de modelo base (Random Forest)
5. Manejo del desbalance:
   - class_weight='balanced'
   - SMOTE
6. Optimización de hiperparámetros con GridSearchCV
7. Comparación de modelos y evaluación final

## Resultados / Insights

El modelo final seleccionado fue: Random Forest optimizado con GridSearch y class_weight='balanced'

Resultados:

- Clase 0: Precision 0.93, Recall 0.92 y F1 0.93
- Clase 1: Precision 0.45, Recall 0.48 y F1 0.47
- Accuracy global: 0.87. El modelo logró una mejora considerable en la detección de la clase minoritaria, mejorando Recall y F1-score sin generar una gran disminución en accuracy.

## Recomendaciones de Negocio

- Implementar el modelo para priorizar clientes con mayor probabilidad de aceptar el producto.
- Ajustar el umbral de decisión si se desea incrementar aún más el recall de la clase positiva.
- Analizar campañas segmentadas de acuerdo a los "tipos" de cliente (edad, historial, tipo de contacto).

## Limitaciones

- El dataset presenta desbalance significativo.
- No se realizó validación externa con nuevos datos reales.

## Próximos Pasos

- Obtener dataset actualizado para testear el modelo. 
- Dividir por categorias de clientes para luego de trabajado el modelo avanzar en un plan de marketing.
- Analizar resultados para mejorar modelo. 

---

## Cómo Replicar el Proyecto

1. Clonar el repositorio.
2. Instalar las librerías necesarias (ver librerias.txt).
3. Ejecutar el cuaderno a través de github.

## Fuentes de datos
- https://archive.ics.uci.edu/dataset/222/bank+marketing