from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from StudentApp.models import Profesor, Student,Curso
from .serializers import StudentSerializer,CursoSerializer,ProfesorSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def studentApi(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({"error": "Alumno no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        # Validar si el correo ya está en uso
        email = request.data.get('email')
        if Student.objects.filter(email=email).exists():
            return Response({"error": "El correo electrónico ya está en uso"}, status=status.HTTP_400_BAD_REQUEST)

        # Validar longitud de la identificación
        identificacion = request.data.get('identificacion')
        if len(identificacion) != 10:
            return Response({"error": "La identificación debe tener 10 caracteres"}, status=status.HTTP_400_BAD_REQUEST)

        # Validar si la identificación ya está en uso
        if Student.objects.filter(identificacion=identificacion).exists():
            return Response({"error": "La identificación ya está en uso"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Alumno creado exitosamente", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        if id is None:
            return Response("Insertar un Id valido", status=status.HTTP_400_BAD_REQUEST)
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"error": "alumno no encontrado imposible actualizar"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Alumno actualizado correctamente")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if id is None:
            return Response("Insertar un  ID valido para la eliminacion", status=status.HTTP_400_BAD_REQUEST)
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response("Alumno borrado exitosamente", status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"error": "Alumno no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response("Accion no permitida", status=status.HTTP_405_METHOD_NOT_ALLOWED)



# ---------profesor-----------------

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def profesorApi(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                profesor = Profesor.objects.get(id=id)
                serializer = ProfesorSerializer(profesor)
                return Response(serializer.data)
            except Profesor.DoesNotExist:
                return Response({"error": "Profesor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            profesores = Profesor.objects.all()
            serializer = ProfesorSerializer(profesores, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfesorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Profesor creado exitosamente", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        if id is None:
            return Response("Insertar un ID válido", status=status.HTTP_400_BAD_REQUEST)
        try:
            profesor = Profesor.objects.get(id=id)
        except Profesor.DoesNotExist:
            return Response({"error": "Profesor no encontrado, imposible actualizar"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfesorSerializer(profesor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Profesor actualizado correctamente")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if id is None:
            return Response("Insertar un ID válido para la eliminación", status=status.HTTP_400_BAD_REQUEST)
        try:
            profesor = Profesor.objects.get(id=id)
            profesor.delete()
            return Response("Profesor borrado exitosamente", status=status.HTTP_204_NO_CONTENT)
        except Profesor.DoesNotExist:
            return Response({"error": "Profesor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response("Acción no permitida", status=status.HTTP_405_METHOD_NOT_ALLOWED)




# ---------------Curso ===================
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def cursoApi(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                curso = Curso.objects.get(id=id)
                serializer = CursoSerializer(curso)
                return Response(serializer.data)
            except Curso.DoesNotExist:
                return Response({"error": "Curso no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            cursos = Curso.objects.all()
            serializer = CursoSerializer(cursos, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            # Guardar la imagen si se proporciona
            imagen = request.FILES.get('imagen')
            if imagen:
                serializer.validated_data['imagen'] = imagen
            serializer.save()
            return Response("Curso creado exitosamente", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        if id is None:
            return Response("Insertar un ID válido", status=status.HTTP_400_BAD_REQUEST)
        try:
            curso = Curso.objects.get(id=id)
        except Curso.DoesNotExist:
            return Response({"error": "Curso no encontrado, imposible actualizar"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            # Guardar la imagen si se proporciona
            imagen = request.FILES.get('imagen')
            if imagen:
                serializer.validated_data['imagen'] = imagen
            serializer.save()
            return Response("Curso actualizado correctamente")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if id is None:
            return Response("Insertar un ID válido para la eliminación", status=status.HTTP_400_BAD_REQUEST)
        try:
            curso = Curso.objects.get(id=id)
            curso.delete()
            return Response("Curso borrado exitosamente", status=status.HTTP_204_NO_CONTENT)
        except Curso.DoesNotExist:
            return Response({"error": "Curso no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response("Acción no permitida", status=status.HTTP_405_METHOD_NOT_ALLOWED)
