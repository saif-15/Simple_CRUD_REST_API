from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Note 
from .serializers import NoteSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET',])
def getData(request):
		note=Note.objects.all()
		note_serialized=NoteSerializer(note,many=True)
		if(request.method == 'GET'):
			return Response(data=note_serialized.data,status=200)

@api_view(['GET',])
def getDataById(request,id):
		data={}
		try:
			note_serialized=NoteSerializer(Note.objects.get(id=id))
		except Note.DoesNotExist:
			data['result']='resource doestnot Exist'
			return Response(data,status=404)
		if(request.method == 'GET'):
			return Response(data=note_serialized.data,status=200)

@api_view(['POST',])
def post_data(request):
	note=NoteSerializer(data=request.data)
	data={} 
	if request.method=='POST':
		if note.is_valid():
			note.save()
			data['result']='resource created successfully'
			return Response(data,status=201)
		else:
			data['result']='resource not created successfully'
			return Response(data,status=status_404_BAD_REQUEST)

@api_view(['PUT',])
def put_data(request,id):
	data={} 
	try:
		note=Note.objects.get(id=id)
		note_serialized=NoteSerializer(note,data=request.data)
	except Note.DoesNotExist:
		data['result']='resource doestnot Exist'
		return Response(data,status=status_404_BAD_REQUEST)
	if request.method=='PUT':
		if note_serialized.is_valid():
			note_serialized.save()
			data['result']='resource updated successfully'
			return Response(data,status=201)
		else:
			data['result']='resource not updated successfully'
			return Response(data,status=status_404_BAD_REQUEST)

@api_view(['DELETE',])
def delete_data(request,id):
	data={}
	try:
		note=Note.objects.get(id=id)
	except Note.DoesNotExist:
		data['result']="Note doestnot exist"
		return Response(data,status=404)
	operation=note.delete()
	if operation:
		data['result']='note deleted successfully'
		return Response(data,status=200)
	else:
		data['result']='note not deleted successfully'
		return Response(data,status=400)

@api_view(['DELETE'])
def delete_data_all(request):
	data={}
	try:
		operation=Note.objects.all().delete()
	except Note.DoesNotExist:
		data['result']="Note doestnot exist"
		return Response(data,status=404)
	if operation:
		data['result']='all data is deleted'
		return Response(data,status=200)




