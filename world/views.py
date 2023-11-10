from django.http import JsonResponse


def update_location(request):
    if request.method == 'POST':

        # get user location data from request
        latitude = request.POST.get('lat')
        longitude = request.POST.get('lon')

        # update user location in the database
        user = request.user
        user.profile.lat = latitude
        user.profile.lon = longitude
        user.profile.save()

        # JSON response.
        response_data = {'message': 'Location updated successfully'}

        return JsonResponse(response_data)

    # error handling
    return JsonResponse({'error': 'Invalid request'}, status=400)
