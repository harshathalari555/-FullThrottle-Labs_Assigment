from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import *
from collections import OrderedDict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .custom_paginatiions import CustomPagination

#
class MemberApi(APIView):
    def get(self, request,**kwargs):
        if kwargs.get('pk'):
            pk = kwargs.get('pk')
            obj = get_object_or_404(Member.objects.all(), pk=pk)
            organization = MemberSerializer(obj)
            return Response(organization.data)
        paginator = CustomPagination()
        query_set = Member.objects.all()
        page = paginator.paginate_queryset(query_set, request)
        serializer = MemberSerializer(page, many=True).data
        return paginator.get_paginated_response(serializer)

    def post(self,request,*args,**kwargs):
        data = request.data
        member = Member.objects.create(
            id=data.get('id'),
            real_name=data.get('real_name'),
            tz=data.get('tz')
        )
        if data.get('activity_periods'):
            print(data.get('activity_periods'))
            for b in data.get('activity_periods'):
                activity_period = ActivityPeriod.objects.create(
                    start_time=b['start_time'],
                    end_time=b['end_time']
                )

                member.activity_periods.add(activity_period)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            member.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        queryset=Member.objects.get(pk=pk)

        serializer=MemberSerializer(queryset)
        return Response(serializer.data)


    def put(self, request, pk):
        queryset = Member.objects.get(pk=pk)

        queryset.activity_periods.clear()
        activity_periods = request.data.get('activity_periods', [])
        if isinstance(activity_periods, list):
            for ba in activity_periods:
                obj_ba = ActivityPeriod.objects.filter(id=ba.get('id')).first()
                if not obj_ba:
                    obj_ba = ActivityPeriod.objects.create(
                        start_time=ba.get("start_time")
                    )

                if ba.get('id'):
                    obj_ba.id = ba.get('id')
                if ba.get('start_time'):
                    obj_ba.start_time = ba.get('start_time')
                if ba.get('end_time'):
                    obj_ba.end_time = ba.get('end_time')
                obj_ba.save()
                queryset.organization_address.add(obj_ba)
                queryset.save()

        serializer = MemberSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        queryset=Member.objects.get(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)