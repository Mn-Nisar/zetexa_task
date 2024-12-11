import csv
def custom_middleware(request):
    print(request.user)

    with open("user_data.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow([request.user,])

    return Response({'message': 'Custom middleware executed'})