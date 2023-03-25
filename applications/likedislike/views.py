from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from applications.likedislike.models import LikeDislike
from applications.account.models import Profile

class SetLikeAPIView(APIView):
    '''Установка Like на профиле - recipient user_id'''
    
    @staticmethod
    def post(request, recipient_id):
        try:
            recipient = Profile.objects.get(user_id=recipient_id)
            sender = Profile.objects.get(user_id=request.user.id)

            if not LikeDislike.objects.filter(sender=sender, 
                                            recipient=recipient).exists():
                LikeDislike.objects.create(sender=sender, 
                                        recipient=recipient, 
                                        is_like=True, 
                                        is_dislike=False)
                return Response({'status': 'success', 'message': 'You liked this user'})
            else:
                like = LikeDislike.objects.get(sender=sender, recipient=recipient)
                if like.is_like:
                    return Response({'status': 'error', 'message': 'You already liked this user'})
                else:
                    like.is_like = True
                    like.is_dislike = False
                    like.save()
                    return Response({'status': 'success', 'message': 'You liked this user'})
        except BaseException as e:
            return Response({'status': 'error', 'message': f"{e}"}, status=status.HTTP_400_BAD_REQUEST)    

class SetDisLikeAPIView(APIView):
    '''Установка Dislike на профиле - recipient user_id'''

    @staticmethod
    def post(request, recipient_id):
        try:
            recipient = Profile.objects.get(user_id=recipient_id)
            sender = Profile.objects.get(user_id=request.user.id)
            if not LikeDislike.objects.filter(sender=sender, 
                                          recipient=recipient).exists():
                LikeDislike.objects.create(sender=sender, 
                                       recipient=recipient, 
                                       is_like=False, 
                                       is_dislike=True)
                return Response({'status': 'success', 'message': 'You disliked this user'})
            else:
                like = LikeDislike.objects.get(sender=sender, recipient=recipient)
                if like.is_dislike:
                    return Response({'status': 'error', 'message': 'You already disliked this user'})
                else:
                    like.is_dislike = True
                    like.is_like = False
                    like.save()
                    return Response({'status': 'success', 'message': 'You disliked this user'})
        except BaseException as e:
            return Response({'status': 'error', 'message': f"{e}"}, status=status.HTTP_400_BAD_REQUEST)    


            
class GetLikeDislikeAPIView(APIView): 
    '''Получение статуса Like/Dislike на профиле - recipient user_id
        Формат ответа:
            "is_like": BooleanField,
            "is_dislike": BooleanField
                        
    '''

    @staticmethod
    def get(request, recipient_id):

        try:
            recipient = Profile.objects.get(user_id=recipient_id)
            sender = Profile.objects.get(user_id=request.user.id)
            like_dislake = LikeDislike.objects.filter(sender=sender, 
                                            recipient=recipient).values('is_like', 'is_dislike')
            return Response(like_dislake, status=status.HTTP_200_OK)
        except BaseException:
            return Response({'message': 'По данному запросу нет данных'},status=status.HTTP_204_NO_CONTENT)
    
        
            
            


     

            
                    
        
        