# Super Market Data
## Introducción
En este trabajo se analiza el archivo de "SuperMarketData", con el objetivo de saber qué tan viable es abrir una sucursal de una empresa multinacional en una comunidad similar a la de Juriquilla, Querétaro.
Para esto se analizarán las ganancias de sucursales en comunidades similares, así como sus ratings. El proceso se separará en dos códigos, uno para las ventas y uno para el rating. Esto con el fin de hacer más práctica la lectura.

Para lograr el objetivo se utilizó el método de "Máximum likelihood estimation". Se utilizará la función de densidad de probabilidad beta,  una de las distribuciones más generales y flexibles que existen. 

![image](https://github.com/user-attachments/assets/2775f186-799d-47f6-8871-35718376824a)

Esta función de densidad está definida de 0 a 1. El trabajo a realizar es obtener alpha y beta.

## Pasos a seguir (Ventas)
1. Como la función de densidad está definida de 0 a 1, hay que normalizar los datos para que se encuentren en este intervalo, de modo que:
 
   ![image](https://github.com/user-attachments/assets/08561cc8-dcc1-40c5-8eb2-8cb15856b736)
   
2. A través de python conseguimos alpha y beta, con los cuales calcularemos el promedio (mu) y la desviación estándar (sigma).
3. Determinamos si la suma de las ventas llegará a ser mayor que los gastos de operación y que la ganancia deseada ($1,500,000). Para esto debemos tomar en cuenta que en nuestra sucursal trabajarán 40 almacenistas, 60 empleados de mostrador, 30 cajeros, 20 conserjes, 1 gerente general y 4 subgerentes. También queremos pagarle 15% más del salario mínimo a los almacenistas, conserjes y empleados de mostrador. También habrá que tomar en cuenta los gastos de la luz, los cuales calcularemos a través de la superficie de la de la sucursal (2000 metros cuadrados), donde se gastan 120 kw/hr/m2. La CFE cobra $3.134 por cada kw/hr utilizado. Se utilizará un horario de la sucursal de 24 horas para calcular el gasto de la luz, ya que los supermercados gastan energía durante todo el día, ya sea en letreros, refrigeradores, etc.. Queremos que se cubran los gastos más la ganancia deseada con un 99% de probabilidad.

## Resultados (Ventas)
Graficando en un histograma los datos de las ventas, obtenemos:

![image](https://github.com/user-attachments/assets/a3afac99-c4a6-4b41-88df-09c0847cf843)

Al llevar a cabo los pasos estipulados en python, obtenemos los siguientes resultados:

![image](https://github.com/user-attachments/assets/889c14fe-6efe-434e-8902-85db488bc438)

Lo que más nos interesa de estos resultados es el porcentaje de aprobación de la población. Dado que este porcentaje nos da 60.67%, podemos decir que no no es viable establecer una sucursal en esta comunidad, ya que el porcentaje mencionado es bastante alto, con lo que se necesitaría de una recepción del público abrumadoramente positiva para que el proyecto sea sustentable. Esto se debe mayormente al gasto de la luz, con lo que, al menos que se tenga un contrato especial con la CFE, este gasto vuelve insostenible la implementación de la nueva sucursal.

## Resultados (Ratings)
Graficando en un histograma los datos de las ventas, obtenemos:

![image](https://github.com/user-attachments/assets/b1245730-e1a3-4cfe-a41c-66867025ee74)

En este histograma se puede observar que, aunque no perfectamente, la distribución de los datos del rating es uniforme. Con esto podemos utilizar nuevamente la función de densidad de probabilidad beta.
Utilizando python y la función de densidad de probabilidad de beta obtenemos los siguientes resultados:

![image](https://github.com/user-attachments/assets/6d88050f-3894-4fb2-b79c-ff69e03c1595)

Con lo que la probabilidad de que los ratings sean mayores a los deseados es de aproximadamente 17.31%. Este resultado no es satisfactorio, ya que la probabilidad mencionada no es muy alta, lo que nos dice que nuestros clientes no tienen una preferencia especial por nuestro supermercado. Al momento de establecer una nueva sucursal debemos de tomar esto en cuenta, ya que los posibles clientes no compran en nuestro supermercado por una preferencia especial, lo cual puede llegar a ser un riesgo si se establecen otros supermercados en la zona.

## Referencias
Conserje. (2024). Glassdoor. https://www.glassdoor.com.mx/Sueldos/conserje-sueldo-SRCH_KO0,8.htm
Tarifas Domésticas CFE 2022: ¿Cómo saber en cuál estoy? (2021, January 27). Tarifasdeluz.mx. https://tarifasdeluz.mx/cfe-tarifas
