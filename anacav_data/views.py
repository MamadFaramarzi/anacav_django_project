from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

import pandas as pd
from .serializer import DataSerializer , GetSerializer
from .models import Test


class ImportApiView(APIView):
    serializer_class = DataSerializer
    parser_classes = [MultiPartParser,FormParser]

    def get(self,request):
        queryset = Test.objects.all()
        serializer =GetSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        try :
            data = request.FILES
            serializer = self.serializer_class(data=data)
            if not serializer.is_valid():

                return Response({
                    'status': False,
                    'message': 'Provide a valid file'
                },status=status.HTTP_400_BAD_REQUEST)
            
            excel_file = data.get('file')
            df = pd.read_excel(excel_file,sheet_name=0)
            
            data_list= []
            for index, row in df.iterrows():
                city = row['مدیریت برق شهرستان']
                code= row['کد امور']
                year= row['سال']
                month= row['ماه']
                in_process= row['دردست اجرا']
                condition1= row['تهیه صورت وضعیت']
                condition2= row['صورت وضعیت نزد ستاد']
                Condition3= row['صورت وضعیت نزد مالی']
                total_condition= row['مجموع دستورکارهای باز بهره برداری']
                
                data_obj = Test(
                    city = city,
                    code= code,
                    year= year,
                    month= month,
                    in_process= in_process,
                    condition1= condition1,
                    condition2= condition2,
                    Condition3= Condition3,
                    total_condition= total_condition,
                )
                data_list.append(data_obj)

            Test.objects.bulk_create(data_list)

            return Response({
                'status': True,
                'message': 'data imported successfully'
            }, status=status.HTTP_201_CREATED)


        except Exception as e :
            print(e)
            return Response({
                'status': False,
                'message':'not complete import'
            }, status=status.HTTP_400_BAD_REQUEST)
