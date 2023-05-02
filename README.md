# Login-Register-JWT
authentication Login Register JWT 


#Register
 def post(self, request):
         serializer = UserSerializer(data=request.data )
         if not serializer.is_valid():
           return Response({'status': 403, 'message': serializer.errors})
         serializer.save()
         user = User.objects.get(username=serializer.data['username'])
         token = get_tokens_for_user(user)
         return Response({'status': 200, 'token':token,'payload': serializer.data})




#Login JWT Authentication
 def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'message':'please enter valid username or password !!'},status=status.HTTP_400_BAD_REQUEST)
       
        check_user=User.objects.filter(username=username).exists()
        if check_user==False:
            return Response({'message':'Username does not exists!!'},status=status.HTTP_404_NOT_FOUND)
         
        user = authenticate(username=username,password=password)   
        if user is not None:
            token=get_tokens_for_user(user)
            data = {
                'token':token,
                'user_id':user.pk,
                'username':user.username
                }
            return Response({'status': 200, 'message':'success','data':data},status=status.HTTP_200_OK) 
        else:
             return Response({'message':'Invalid username or password !!'},status=status.HTTP_400_BAD_REQUEST)
             
             

{
  "username": "umesd111",
  "password":"opwss232221"
}

{
  "status": 200,
  "message": "success",
  "data": {
    "token": {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MzE0NDU0MywiaWF0IjoxNjgzMDU4MTQzLCJqdGkiOiJiMzgyNTcxNmZhMzI0YjY1OGY5ZjA3NTU4MTcyNDI2YyIsInVzZXJfaWQiOjR9.Q5Z2SHeE9TQHoPA_TaHQrLoSXrPKbafz-uc_6QKmATY",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzMDU4NDQzLCJpYXQiOjE2ODMwNTgxNDMsImp0aSI6ImJiMWVkMDQ4MGU2NjRkMTQ4ZWNhZjllY2RjMjhiYmI4IiwidXNlcl9pZCI6NH0.1ij7oWU5L_3C_R1iBIiNeq6NJ6KeB12Q8earJv3SIOY"
    },
    "user_id": 4,
    "username": "umesd111"
  }
}
