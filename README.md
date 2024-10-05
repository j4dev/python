# Hiring Backend Challenge - EFEX

## Requisitos:
   - Python 3.12.7
   - Docker
   - Nodejs 20.9.0
   - Npm 10.1.0

## Instrucciones

1. **Clona el repositorio** en tu máquina local:
    ```bash
    git clone https://github.com/j4dev/python.git
    ```

## Question - 1 **Adding Two Numbers**:
 Para poder validar la pregunta se debe ejecutar el siguiente comando dentro del repositorio clonado:

    python .\questions\testing\test_1_adding_two_numbers.py

## Question - 2 **The Perfect Arrangement**:
 Para poder validar la pregunta se debe ejecutar el siguiente comando dentro del repositorio clonado:

    python .\questions\testing\test_2_perfect_arrangement.py

## Question - 3 **Django REST Framework: Student management API**:
 Para poder validar la pregunta se debe ejecutar los siguientes comandos:

    cd api
    docker-compose up --build

Esto permitirá el acceso al api en http://localhost:8000/

Para ejecutar los test:

    cd api 
    python manage.py test

## Question - 4 **React:Autocorrection App**:
 Para poder validar la pregunta se debe ejecutar los siguientes comandos:

    cd autocorrection
    npm i
    npm run dev
Esto permitirá el acceso al api en http://localhost:5173/

Para ejecutar los test:
    
    cd autocorrection
    npm run test
  
### Question - 5 **Render Function**:

Which of the following functions gets invoked after the `render()` function on update of `state` or `props`?

- [ ] `componentWillMount()`
- [ ] `componentDidMount()`
- [ ] `componentWillReceiveProps()`
- [✅] `componentDidUpdate()`

### Question - 6 **React: True statements**:

Which of the following statement(s) is true about ReactJS?

1. Only one root element can be returned per component.
2. Both arguments of the useEffect hook are compulsory.
3. The useState hook returns an object.
4. The useState hook cannot be used outside of a functional component.

- [✅] 1
- [ ] 2
- [ ] 3
- [✅] 4

## Preguntas adicionales sobre AWS

1. ¿Cuál de los siguientes servicios AWS NO está relacionado con el almacenamiento?
   - A) S3
   - B) EBS
   - ✅ C) EC2
   - D) Glacier

2. ¿Cuál de las siguientes afirmaciones acerca de la Elasticidad de AWS es correcta?
   - ✅ A) La Elasticidad se refiere a la capacidad de AWS para manejar aumentos rápidos en la demanda.
   - B) AWS no puede escalar automáticamente para satisfacer la demanda.
   - C) AWS requiere que los usuarios prevean la demanda con antelación.
   - D) Todas las anteriores.

3. ¿Qué servicio AWS se utiliza para la transmisión de datos en tiempo real?
   - A) Amazon Athena
   - ✅ B) Amazon Kinesis
   - C) AWS Batch
   - D) Amazon EMR

4. ¿Cómo se conoce a la región geográfica en la que se encuentran los servidores de AWS?
   - A) Zona de Disponibilidad
   - B) Zona de Seguridad
   - C) Área de Almacenamiento
   - ✅ D) Región

## Preguntas sobre microservicios en AWS

1. ¿Cuál de los siguientes es un servicio de AWS que ayuda a administrar microservicios?
   - ✅ A) Amazon Elastic Container Service (ECS)
   - B) Amazon S3
   - C) Amazon DynamoDB
   - D) Amazon EMR

2. Si estás implementando un microservicio en AWS y quieres monitorizar su rendimiento, ¿qué servicio usarías?
   - ✅ A) AWS X-Ray
   - B) AWS Rekognition
   - C) AWS Snowball
   - D) AWS Redshift

3. ¿Qué servicio de AWS sería más apropiado para implementar una arquitectura basada en eventos para tus microservicios?
   - A) Amazon S3
   - B) Amazon SQS
   - ✅ C) Amazon Lambda
   - D) Amazon Route 53

4. ¿Cuál de las siguientes afirmaciones es correcta respecto a la seguridad de los microservicios en AWS?
   - ✅ A) Cada microservicio debería tener su propia política de seguridad.
   - B) Todos los microservicios deben compartir la misma política de seguridad.
   - C) Los microservicios no necesitan políticas de seguridad.
   - D) Las políticas de seguridad son gestionadas por AWS, por lo que los usuarios no necesitan preocuparse por ellas.