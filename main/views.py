from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from .serializer import *
from .models import *

# Create your views here.
class LogoGET(ListAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer

    def list(self, request):
        logo = Logo.objects.last()
        ser = LogoSerializer(logo, many=False)
        return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def LogoPOST(request):
    try:
        serializer = LogoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

class InfoGET(ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def list(request, self):
        info = Info.objects.last()
        ser = InfoSerializer(info, many=False)
        return Response(ser.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def InfoPOST(request):
    try:
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)
        

class SliderGET(ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

    def list(request, self):
        slider = Slider.objects.all().order_by('-id')[0:3]
        ser = SliderSerializer(slider, many=True)
        return Response(ser.data)
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def SliderPOST(request):
    try:
        serializer = SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

class CategoryGET(ListAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def CategoryPOST(request):
    try:
        serializer = CategorieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)


class ProductGET(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def ProductPOST(request):
    try:
        user = request.user
        if user.type == 2:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('success')
            else:
                return Response("unfortunately your request hasn't accepted")
        else:
            return Response("unfortunately your request won't be accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

class WishlistGET(ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def WishlistPOST(request):
    try:
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

class CardGET(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def CardPOST(request):
    try:
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

class FacilitiesGET(ListAPIView):
    queryset = Facilities.objects.all()
    serializer_class = FacilitiesSerializer
    
    def list(request, self):
        facilities = Facilities.objects.all().order_by('-id')[0:3]
        ser = FacilitiesSerializer(facilities, many=True)
        return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def FacilitiesPOST(request):
    try:
        serializer = FacilitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

class ForsaleGET(ListAPIView):
    queryset = Forsale.objects.all()
    serializer_class = ForsaleSerializer
    
    def list(request, self):
        forsale = Forsale.objects.all().order_by('-id')[0:3]
        ser = ForsaleSerializer(forsale, many=True)
        return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def ForsalePOST(request):
    try:
        serializer = ForsaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

# ###################################
# ##################################
# ##################################
# ##################################

class BestsellGET(ListAPIView):
    queryset = Bestsell.objects.all()
    serializer_class = BestsellSerializer
    
    def list(request, self):
        bestsell = Bestsell.objects.all().order_by('-id')[0:4]
        ser = BestsellSerializer(bestsell, many=False)
        return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def BestsellPOST(request):
    try:
        serializer = BestsellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

# ###################################
# ##################################
# ##################################
# ##################################

class LatestblogGET(ListAPIView):
    queryset = Latestblog.objects.all()
    serializer_class = LatestblogSerializer
    
    def list(request, self):
        latestblog = Latestblog.objects.all().order_by('-id')[0:3]
        ser = LatestblogSerializer(latestblog, many=True)
        return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def LatestblogPOST(request):
    try:
        serializer = LatestblogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

class NewsletterPOST(CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def NewsletterGET(request):
    newsletter = Newsletter.objects.all()
    ser = NewsletterSerializer(newsletter, many=True)
    return Response(ser.data)

class TeamMembersGET(ListAPIView):
    queryset = TeamMembers.objects.all()
    serializer_class = TeamMembersSerializer
    
    def list(request, self):
        teammembers = TeamMembers.objects.all().order_by('-id')[0:4]
        ser = TeamMembersSerializer(teammembers, many=True)
        return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def TeamMembersPOST(request):
    try:
        serializer = TeamMembersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

class ClientGET(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def list(request, self):
        client = Client.objects.all().order_by('-id')
        ser = ClientSerializer(client, many=True)
        return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def ClientPOST(request):
    try:
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

class SponsorGET(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    
    def list(request, self):
        sponsor = Sponsor.objects.all().order_by('-id')
        ser = SponsorSerializer(sponsor, many=True)
        return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def SponsorPOST(request):
    try:
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

class LeaveMsgPOST(CreateAPIView):
    queryset = LeaveMsg.objects.all()
    serializer_class = LeaveMsgSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def LeaveMsgGET(request):
    leavemsg = LeaveMsg.objects.all()
    ser = LeaveMsgSerializer(leavemsg, many=True)
    return Response(ser.data)

class MapGET(ListAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    
    def list(request, self):
        map = Map.objects.last()
        ser = MapSerializer(map, many=True)
        return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def MapPOST(request):
    try:
        serializer = MapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('success')
        else:
            return Response("unfortunately your request hasn't accepted")
    except Exception as err:
        data = {
            'error': f"{err}",
            'msg': "unfortunately your request hasn't accepted"
        }
        return Response(data)

@api_view(['GET'])
def Search(request):
    name = request.GET.get('name')
    product = Product.objects.get(name__icontains=name)
    pro = ProductSerializer(product)
    return Response(pro.data)