def checkNumbers(arr):
    maximum = 0
    minimum=arr[0]
    promed = 0

    for i in range(len(arr)):
        if arr[i] > minimum:
             maximum = arr[i]
        if arr[i]<=minimum:
            minimum=arr[i]
        promed+=arr[i]
    print(f"Maximo numero {maximum}")
    print(f"Minimo numero: {minimum}")
    print(f"Promedio: {promed/len(arr)}")