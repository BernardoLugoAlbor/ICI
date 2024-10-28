# Super Market Data
## Introducción
En este trabajo se analiza el archivo de "SuperMarketData", con el objetivo de saber qué tan viable es abrir una sucursal de una empresa multinacional en una comunidad similar a la de Juriquilla, Querétaro.
Para lograr el objetivo se utilizó el método de "Máximum likelihood estimation". Se utilizará la función de densidad de probabilidad beta,  una de las distribuciones más generales y flexibles que existen. 
![image](https://github.com/user-attachments/assets/2775f186-799d-47f6-8871-35718376824a)
Esta función de densidad está definida de 0 a 1. El trabajo a realizar es obtener alpha y beta.

## Pasos a seguir
1. Como la función de densidad está definida de 0 a 1, hay que normalizar los datos para que se encuentren en este intervalo, de modo que:
   ![image](https://github.com/user-attachments/assets/08561cc8-dcc1-40c5-8eb2-8cb15856b736)
2. A través de python conseguimos alpha y beta, con los cuales calcularemos el promedio (mu) y la desviación estándar (sigma).  
