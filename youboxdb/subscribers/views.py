from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

#Updating user with an image requires form data right?
    def put(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        user = self.get_object(username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UtokenList(APIView):

    def get(self, request):
        token = Utoken.objects.all()
        serializer = UtokenSerializer(token, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostUtokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UtokenFilter(APIView):

    def get_object(self, user_Id):
        try:
            return Utoken.objects.filter(user_Id=user_Id)
        except Utoken.DoesNotExist:
            raise Http404

    def get(self, request, user_Id):
        token = self.get_object(user_Id)
        serializer = UtokenSerializer(token, many=True)
        return Response(serializer.data)


class UtokenDetail(APIView):

    def get_object(self, pk):
        try:
            return Utoken.objects.get(pk=pk)
        except Utoken.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        token = self.get_object(pk)
        serializer = UtokenSerializer(token)
        return Response(serializer.data)

    def delete(self, request, pk):
        token = self.get_object(pk)
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClothingList(APIView):

    def get(self, request):
        clothing = Clothing.objects.all()
        serializer = ClothingSerializer(clothing, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostClothingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClothingDetail(APIView):

    def get_object(self, pk):
        try:
            return Clothing.objects.get(pk=pk)
        except Clothing.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        clothing = self.get_object(pk)
        serializer = ClothingSerializer(clothing)
        return Response(serializer.data)

    def put(self, request, pk):
        clothing = self.get_object(pk)
        serializer = ClothingSerializer(clothing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        clothing = self.get_object(pk)
        clothing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriptionList(APIView):

    def get(self, request):
        subscription = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscription, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionDetail(APIView):

    def get_object(self, pk):
        try:
            return Subscription.objects.get(pk=pk)
        except Subscription.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def put(self, request, pk):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subscription = self.get_object(pk)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderFilter(APIView):

    def get_object(self, user_Id):
        try:
            return Order.objects.filter(user_Id=user_Id)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, user_Id):
        order = self.get_object(user_Id)
        serializer = UtokenSerializer(order, many=True)
        return Response(serializer.data)


class ImageList(APIView):

    def get(self, request):
        image = Image.objects.all()
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(APIView):

    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        image = self.get_object(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def delete(self, request, pk):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageFilterItem(APIView):

    def get_object(self, item_Id):
        try:
            return Image.objects.filter(item_Id=item_Id)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, item_Id):
        image = self.get_object(item_Id)
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)


class ImageFilterUser(APIView):

    def get_object(self, user_Id):
        try:
            return Image.objects.filter(user_Id=user_Id)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, user_Id):
        image = self.get_object(user_Id)
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)
