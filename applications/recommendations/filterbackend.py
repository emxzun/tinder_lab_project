from rest_framework.filters import BaseFilterBackend

class FilterProfileBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user
        queryset = queryset.filter(interests=user.interests, status=user.status, sexual_orientation=user.sexual_orientation)
        return queryset